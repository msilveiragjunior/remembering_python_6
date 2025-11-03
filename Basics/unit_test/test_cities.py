import unittest
from city_functions import city_country
# Here we create the class to test the function city functions


class TestCityCountry(unittest.TestCase):
    # Here we will compare the results from city_functions.py
    def test_city_country(self):
        formatted_city_country = city_country('santiago', 'chile')
        self.assertEqual(formatted_city_country, "Santiago, Chile")


unittest.main()
