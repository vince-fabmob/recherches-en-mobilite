import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from bixi_fare_calculator import calculate_bixi_fare, load_bixi_rates


class BixiFareCalculatorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rates = load_bixi_rates(Path(__file__).resolve().parents[1] / "donnees" / "tarifs-bixi.json")

    def test_member_regular_bike_within_included_period(self):
        result = calculate_bixi_fare(self.rates, "member", "regular_bike", [30])
        self.assertEqual(result["cost_before_taxes"], 0.00)

    def test_member_regular_bike_overage(self):
        result = calculate_bixi_fare(self.rates, "member", "regular_bike", [55])
        self.assertEqual(result["cost_before_taxes"], 1.90)
        self.assertEqual(result["cost_after_taxes"], 2.18)

    def test_member_electric_bike_is_charged_from_first_minute(self):
        result = calculate_bixi_fare(self.rates, "member", "electric_bike", [20])
        self.assertEqual(result["cost_before_taxes"], 3.80)

    def test_member_regular_bike_resets_included_period_per_segment(self):
        result = calculate_bixi_fare(self.rates, "member", "regular_bike", [35, 35])
        self.assertEqual(result["cost_before_taxes"], 0.00)

    def test_one_way_regular_bike(self):
        result = calculate_bixi_fare(self.rates, "one_way", "regular_bike", [18])
        self.assertEqual(result["cost_before_taxes"], 5.38)

    def test_rejects_unknown_bike_type(self):
        with self.assertRaises(ValueError):
            calculate_bixi_fare(self.rates, "member", "cargo_bike", [20])


if __name__ == "__main__":
    unittest.main()
