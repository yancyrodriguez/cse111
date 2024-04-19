import unittest
from unittest.mock import patch, mock_open
import io
import time_zone  

class TestTimeZoneFunction(unittest.TestCase):
    # Test to check if the get_time_zone function can correctly handle valid time zones
    @patch('builtins.open', mock_open(read_data="America/New_York\nEurope/London"))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_time_zone_with_valid_zones(self, mock_stdout):
        
        try:
            time_zone.get_time_zone("fake_time_zone.txt") #call the function get_time_zone with a time zones valid file
            success = True
        except Exception as e:
            success = False
        
        self.assertTrue(success, "The function should complete successfully with valid time zones.")

if __name__ == '__main__':
    unittest.main()