import unittest
import importlib  
country_codes = importlib.import_module("16_5")

class CountryCodesTestCase(unittest.TestCase):
    """Tests for country_codes.py."""

    def test_get_country_code(self):
        country_code = country_codes.get_country_code('Andorra')
        self.assertEqual(country_code, 'ad')

        country_code = country_codes.get_country_code('United Arab Emirates')
        self.assertEqual(country_code, 'ae')

        country_code = country_codes.get_country_code('Afghanistan')
        self.assertEqual(country_code, 'af')

        country_code = country_codes.get_country_code('Hong Kong SAR, China')
        self.assertEqual(country_code, 'hk')

unittest.main()