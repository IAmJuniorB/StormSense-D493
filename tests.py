import unittest
from unittest.mock import patch
from main import main
from weather_class import StormSense2, table_populate, Session
from weather_api import fetch_weather_data

#D: Create a unit test file
class TestMain(unittest.TestCase):
    """
    Test cases for the main function.
    """
    @patch('builtins.print')
    def test_main(self, mock_print):
        """
        Run this to test the main function and ensure it runs without errors.
        """
        main()
        self.assertTrue(mock_print.called)

class TestWeatherClass(unittest.TestCase):
    """
    Test cases for the StormSense2 class and related methods.
    """
    def setUp(self):
        """
        Set up the test environment by creating a session to interact with the database.
        """
        self.session = Session()

    def test_table_populate(self):
        """
        Test the table_populate function to ensure data is added successfully to the database.
        """
        latitude = 32.0002
        longitude = -80.8457
        date_to_check = "05-07"
        table_populate(self.session, latitude, longitude, date_to_check)
        result = self.session.query(StormSense2).filter_by(month=5, day=7).all()
        self.assertGreater(len(result), 0)

    def tearDown(self):
        """
        This will clean up the test environment by rolling back the session changes and then closing.
        """
        self.session.rollback()
        self.session.close()

class TestWeatherAPI(unittest.TestCase):
    """
    Test cases for the fetch_weather_data function.
    """
    def test_fetch_weather_data(self):
        """
        Test the fetch_weather_data function to ensure it retrieves weather data successfully.
        """
        year = 2023
        latitude = 32.0002
        longitude = -80.8457
        start_date = '05-07'
        data = fetch_weather_data(year, latitude, longitude, start_date)
        self.assertIsNotNone(data)
        expected_keys = ['daily', 'hourly']
        for key in expected_keys:
            self.assertIn(key, data)

if __name__ == '__main__':
    unittest.main()
