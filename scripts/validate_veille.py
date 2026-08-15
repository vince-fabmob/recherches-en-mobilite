#!/usr/bin/env python3
import csv
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
VEILLE = ROOT / "veille-strategique"
TAXONOMY = VEILLE / "taxonomie.yml"
CATALOGUE = VEILLE / "catalogue_signaux.csv"
FICHES = VEILLE / "fiches"
REFERENCE_CATALOGUES = {
    "donnees": ROOT / "referentiels/donnees/catalogue_donnees.csv",
    "operateurs": ROOT / "referentiels/operateurs/catalogue_operateurs.csv",
    "solutions": ROOT / "referentiels/solutions/catalogue_solutions.csv",
}

REQUIRED_TOP_LEVEL = {
    "id", "titre", "dates", "classification", "geographie", "preuve",
    "signal", "scenarios_affectes", "tipping_points", "dynamic_pathway",
    "relations", "impacts_potentiels", "suivi"
}
REQUIRED_SECTIONS = [
    "## 1. Signal factuel",
    "## 2. Niveau de preuve et limites",
    "## 3. Mécanismes et implications prospectives",
    "## 4. Scénarios affectés",
    "## 5. Points de bascule",
    "## 6. Dynamic pathway et options réelles",
    "## 7. Indicateurs de suivi",
    "## 8. Relations avec données, solutions et opérateurs",
    "## 9. Sources",
]


def load_front_matter(path: Path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("front matter YAML manquant")
    end = text.find("\n---", 4)
    if end == -1:
        raise ValueError("front matter YAML non fermé")
    metadata = yaml.safe_load(text[4:end])
    if not isinstance(metadata, dict):
        raise ValueError("front matter YAML invalide")
    return metadata, text[end + 4:]


def load_reference_ids():
    ids = {}
    for relation_type, path in REFERENCE_CATALOGUES.items():
        if not path.exists():
            raise FileNotFoundError(f"catalogue référentiel manquant: {path}")
        with path.open(newline="", encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle))
        ids[relation_type] = {row.get("id", "") for row in rows if row.get("id")}
    return ids


def validate_fiche(path: Path, taxonomy: dict, reference_ids: dict):
    errors = []
    try:
        metadata, body = load_front_matter(path)
    except Exception as exc:
        return [f"{path}: {exc}"], None

    missing = REQUIRED_TOP_LEVEL - set(metadata)
    if missing:
        errors.append(f"{path}: champs manquants: {', '.join(sorted(missing))}")

    signal_id = metadata.get("id", "")
    if not re.fullmatch(r"SIG-[A-Z0-9]+-\d{4}-\d{4}", signal_id):
        errors.append(f"{path}: id invalide '{signal_id}'")

    classification = metadata.get("classification", {})
    if classification.get("domaine_principal") not in taxonomy.get("themes", []):
        errors.append(f"{path}: domaine_principal absent de la taxonomie")
    if classification.get("type_signal") not in taxonomy.get("types_signal", []):
        errors.append(f"{path}: type_signal absent de la taxonomie")
    if classification.get("statut_signal") not in taxonomy.get("statuts_signal", []):
        errors.append(f"{path}: statut_signal absent de la taxonomie")
    if classification.get("statut_epistemique") not in taxonomy.get("statuts_epistemiques", []):
        errors.append(f"{path}: statut_epistemique absent de la taxonomie")
    if classification.get("horizon_principal") not in taxonomy.get("horizons", []):
        errors.append(f"{path}: horizon_principal absent de la taxonomie")

    strength = metadata.get("signal", {}).get("force_signal")
    uncertainty = metadata.get("signal", {}).get("incertitude")
    if strength not in taxonomy.get("echelles", {}).get("force_signal", {}):
        errors.append(f"{path}: force_signal doit être comprise entre 1 et 5")
    if uncertainty not in taxonomy.get("echelles", {}).get("incertitude", {}):
        errors.append(f"{path}: incertitude doit être comprise entre 1 et 4")

    for scenario in metadata.get("scenarios_affectes", []):
        if scenario.get("effet") not in taxonomy.get("effets_scenario", []):
            errors.append(f"{path}: effet de scénario absent de la taxonomie")

    relations = metadata.get("relations", {})
    for relation_type, prefix in [("donnees", "DATA-"), ("operateurs", "OP-"), ("solutions", "SOL-")]:
        entries = relations.get(relation_type, [])
        if not isinstance(entries, list):
            errors.append(f"{path}: relations.{relation_type} doit être une liste")
            continue
        for entry in entries:
            relation_id = entry.get("id", "") if isinstance(entry, dict) else ""
            if not relation_id.startswith(prefix):
                errors.append(f"{path}: identifiant {relation_type} invalide '{relation_id}'")
            elif relation_id not in reference_ids[relation_type]:
                errors.append(f"{path}: identifiant référentiel introuvable '{relation_id}'")

    sources = re.findall(r"https?://[^)\s]+", body)
    if not sources:
        errors.append(f"{path}: au moins une URL de source est requise")

    for section in REQUIRED_SECTIONS:
        if section not in body:
            errors.append(f"{path}: section manquante '{section}'")

    return errors, {"id": signal_id, "path": path.relative_to(VEILLE).as_posix()}


def main():
    if not TAXONOMY.exists() or not CATALOGUE.exists() or not FICHES.exists():
        print("Structure veille-strategique incomplète")
        return 1

    try:
        reference_ids = load_reference_ids()
    except Exception as exc:
        print(f"Validation échouée : {exc}")
        return 1

    taxonomy = yaml.safe_load(TAXONOMY.read_text(encoding="utf-8"))
    errors = []
    records = []

    for path in sorted(FICHES.rglob("*.md")):
        fiche_errors, record = validate_fiche(path, taxonomy, reference_ids)
        errors.extend(fiche_errors)
        if record:
            records.append(record)

    ids = [record["id"] for record in records]
    duplicates = sorted({item for item in ids if ids.count(item) > 1})
    if duplicates:
        errors.append(f"Identifiants SIG dupliqués: {', '.join(duplicates)}")

    with CATALOGUE.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    catalogue_ids = [row.get("id", "") for row in rows]
    catalogue_paths = {row.get("fiche", "") for row in rows}

    for record in records:
        if record["id"] not in catalogue_ids:
            errors.append(f"{record['path']}: fiche absente du catalogue_signaux.csv")
        if record["path"] not in catalogue_paths:
            errors.append(f"{record['path']}: chemin absent du catalogue_signaux.csv")

    unknown = sorted(set(catalogue_ids) - set(ids))
    if unknown:
        errors.append(f"Catalogue contient des identifiants sans fiche: {', '.join(unknown)}")

    if errors:
        print("Validation échouée :")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validation réussie : {len(records)} fiche(s), {len(rows)} entrée(s) au catalogue.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
