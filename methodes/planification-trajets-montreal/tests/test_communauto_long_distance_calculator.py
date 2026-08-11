import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from communauto_long_distance_calculator import calculate_long_distance, load_long_distance_rates


class LongDistanceCalculatorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rates = load_long_distance_rates(Path(__file__).resolve().parents[1] / "donnees" / "tarifs-communauto-longue-distance.json")

    def test_low_season_first_day(self):
        result = calculate_long_distance(self.rates, "economique", "2026-02-01T09:00", "2026-02-02T09:00", 100)
        self.assertEqual(result["before_taxes"], 73.00)

    def test_high_season_first_day(self):
        result = calculate_long_distance(self.rates, "economique_extra", "2026-07-01T09:00", "2026-07-02T09:00", 100)
        self.assertEqual(result["before_taxes"], 83.00)

    def test_additional_hours_are_capped_at_day_rate(self):
        result = calculate_long_distance(self.rates, "economique", "2026-02-01T09:00", "2026-02-02T12:00", 0)
        self.assertEqual(result["time_cost"], 80.00)

    def test_weekly_cap(self):
        result = calculate_long_distance(self.rates, "economique", "2026-02-01T09:00", "2026-02-08T09:00", 0)
        self.assertEqual(result["time_cost"], 210.00)

    def test_distance_threshold(self):
        result = calculate_long_distance(self.rates, "economique", "2026-02-01T09:00", "2026-02-02T09:00", 350)
        self.assertEqual(result["distance_cost"], 98.50)

    def test_ineligible_plan(self):
        with self.assertRaises(ValueError):
            calculate_long_distance(self.rates, "liberte", "2026-02-01T09:00", "2026-02-02T09:00", 100)


if __name__ == "__main__":
    unittest.main()
