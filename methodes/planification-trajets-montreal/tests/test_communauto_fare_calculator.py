import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from communauto_fare_calculator import calculate_best_eligible_rate, calculate_flex, calculate_station, load_rates


class CommunautoFareCalculatorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rates = load_rates(Path(__file__).resolve().parents[1] / "donnees" / "tarifs-communauto.json")

    def test_flex_thirty_minutes(self):
        result = calculate_flex(self.rates, 30, 10)
        self.assertEqual(result["before_taxes"], 12.90)
        self.assertEqual(result["distance_cost"], 0.00)

    def test_flex_daily_cap_and_distance_overage(self):
        result = calculate_flex(self.rates, 240, 80)
        self.assertEqual(result["time_cost"], 50.00)
        self.assertEqual(result["distance_cost"], 1.55)
        self.assertEqual(result["before_taxes"], 51.55)

    def test_station_has_no_four_hour_minimum(self):
        result = calculate_station(self.rates, "economique_extra", 30, 10)
        self.assertEqual(result["time_cost"], 1.50)
        self.assertEqual(result["distance_cost"], 3.30)
        self.assertEqual(result["before_taxes"], 4.80)

    def test_liberte_weekend_surcharge_applies_only_to_station(self):
        result = calculate_station(self.rates, "liberte", 60, 0, weekend=True)
        self.assertEqual(result["time_cost"], 14.60)

    def test_best_rate_uses_four_hour_station_comparison(self):
        result = calculate_best_eligible_rate(self.rates, "economique_extra", 30, 10)
        self.assertEqual(result["mode"], "flex")
        self.assertEqual(result["alternatives"], {"flex": 12.90, "station_comparison": 15.30})

    def test_liberte_has_no_station_comparison(self):
        result = calculate_best_eligible_rate(self.rates, "liberte", 300, 0)
        self.assertEqual(result["selected_by"], "flex_only")
        self.assertEqual(result["before_taxes"], 50.00)


if __name__ == "__main__":
    unittest.main()
