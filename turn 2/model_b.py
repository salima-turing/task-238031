import unittest
import math


class PricingModel:
    # (Same code as before)
    def __init__(self, price_per_unit_area):
        self.price_per_unit_area = price_per_unit_area

    def calculate_list_price(self, area):
        if not isinstance(area, (int, float)):
            raise ValueError("Area must be a numeric value")
        if area <= 0:
            raise ValueError("Area must be positive")

        return self.price_per_unit_area * area


class TestPricingModel(unittest.TestCase):
    # (Same code as before)
    def setUp(self):
        self.model = PricingModel(price_per_unit_area=100)

    def test_calculate_list_price_valid_input(self):
        test_cases = [
            (100, 10000),
            (200, 20000),
            (0.5, 50),
        ]
        for area, expected_price in test_cases:
            with self.subTest(area=area):
                self.assertEqual(self.model.calculate_list_price(area), expected_price)


def test_calculate_list_price_valid_input_edge_cases(self):
    test_cases = [
        (0, 0),  # Smallest possible area
        (float('inf'), float('inf')),  # Very large area
        (math.nan, math.nan),  # Floating-point NaN
    ]
    for area, expected_price in test_cases:
        with self.subTest(area=area):
            self.assertAlmostEqual(self.model.calculate_list_price(area), expected_price,
                                   places=7)  # Use assertAlmostEqual for floating-point precision


def test_calculate_list_price_very_small_area(self):
    very_small_area = 0.00000000000000001  # A very small area close to zero
    expected_price = very_small_area * self.model.price_per_unit_area
    self.assertAlmostEqual(self.model.calculate_list_price(very_small_area), expected_price, places=7)


def test_calculate_list_price_floating_point_precision(self):
    area_with_floating_point_error = 0.1 + 0.2  # This should sum to 0.3, but due to floating-point precision, it may not
    expected_price = area_with_floating_point_error * self.model.price_per_unit_area
    self.assertAlmostEqual(self.model.calculate_list_price(area_with_floating_point_error), expected_price, places=7)


if __name__ == '__main__':
    unittest.main()
