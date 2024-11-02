import unittest


class PricingModel:
    def __init__(self, price_per_unit_area):
        self.price_per_unit_area = price_per_unit_area

    def calculate_list_price(self, area):
        if not isinstance(area, (int, float)):
            raise ValueError("Area must be a numeric value")
        if area <= 0:
            raise ValueError("Area must be positive")

        return self.price_per_unit_area * area


class TestPricingModel(unittest.TestCase):

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

    def test_calculate_list_price_invalid_area_type(self):
        with self.assertRaises(ValueError):
            self.model.calculate_list_price("Invalid Input")

    def test_calculate_list_price_negative_area(self):
        with self.assertRaises(ValueError):
            self.model.calculate_list_price(-100)

    def test_calculate_list_price_very_large_area(self):
        self.assertEqual(self.model.calculate_list_price(1e300), 1e302)

    def test_calculate_list_price_very_small_area(self):
        self.assertEqual(self.model.calculate_list_price(1e-300), 1e-298)

    def test_calculate_list_price_floating_point_precision(self):
        area = 0.1 + 0.2
        expected_price = self.model.price_per_unit_area * area
        self.assertAlmostEqual(self.model.calculate_list_price(area), expected_price, places=7)


if __name__ == '__main__':
    unittest.main()
