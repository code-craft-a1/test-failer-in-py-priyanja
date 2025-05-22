import unittest
import os
import sys

# Add the parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import alerter


class TestAlerter(unittest.TestCase):
    
    def setUp(self):
        alerter.alert_failure_count = 0
    
    
    def test_normal_temperature(self):
        # Normal temperature - no alert
        alerter.alert_in_celcius(196)
        self.assertEqual(alerter.alert_failure_count, 0)
    
    def test_just_below_threshold(self):
        # Just below threshold (99.9°C = 211.82°F)
        alerter.alert_in_celcius(211.82)
        self.assertEqual(alerter.alert_failure_count, 0)
    
    def test_at_threshold(self):
        # Exactly at threshold (100°C = 212°F)
        alerter.alert_in_celcius(212)
        self.assertEqual(alerter.alert_failure_count, 0)
    
    def test_just_above_threshold(self):
        # Just above threshold (100.1°C = 212.18°F)
        alerter.alert_in_celcius(212.18)
        self.assertEqual(alerter.alert_failure_count, 1)
    
    def test_high_temperature(self):
        # High temperature
        alerter.alert_in_celcius(400.5)
        self.assertEqual(alerter.alert_failure_count, 1)
    
    def test_another_high_temperature(self):
        # Another high temperature
        alerter.alert_in_celcius(303.6)
        self.assertEqual(alerter.alert_failure_count, 1)
    
    def test_negative_temperature(self):
        # Negative temperature (no alert)
        alerter.alert_in_celcius(-40)
        self.assertEqual(alerter.alert_failure_count, 1)

    def test_zero_temperature(self):
        # Zero temperature (no alert)
        alerter.alert_in_celcius(0)
        self.assertEqual(alerter.alert_failure_count, 1)
    
    def test_invalid_input(self):
        # Invalid string in temperature
        alerter.alert_in_celcius("invalid")
        self.assertEqual(alerter.alert_failure_count, 1)

    def test_low_temperature_Threshold(self):
        alerter.alert_in_celcius(50.00)
        self.assertEqual(alerter.alert_failure_count, 0)

    def test_justbelow_low_temperature_Threshold(self):
        alerter.alert_in_celcius(49.8)
        self.assertEqual(alerter.alert_failure_count, 1)
    
if __name__ == '__main__':
    unittest.main()
