import unittest
from pricing_model import calculate_listing_price


class TestPricingModel(unittest.TestCase):
    def test_calculate_listing_price_basic(self):
        property_size = 2000
        location = 'Suburban'
        expected_price = 2000 * 1.2  # Base price * location factor
        result = calculate_listing_price(property_size, location)
        self.assertEqual(result, expected_price, "Listing price calculation failed.")

    def test_calculate_listing_price_urban(self):
        property_size = 1500
        location = 'Urban'
        expected_price = 1500 * 1.5
        result = calculate_listing_price(property_size, location)
        self.assertEqual(result, expected_price, "Listing price calculation failed for Urban location.")

    def test_invalid_location(self):
        property_size = 3000
        location = 'Invalid Location'
        with self.assertRaises(ValueError):
            calculate_listing_price(property_size, location)


if __name__ == '__main__':
    unittest.main()
