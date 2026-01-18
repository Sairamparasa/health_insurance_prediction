"""
Tests for the Streamlit application
"""

import unittest
import sys
import os
import pandas as pd

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from data_preprocessing import DataValidator, DataProcessor

class TestDataValidator(unittest.TestCase):
    """Test cases for DataValidator class"""
    
    def test_validate_age(self):
        """Test age validation"""
        self.assertTrue(DataValidator.validate_age(25))
        self.assertTrue(DataValidator.validate_age(1))
        self.assertTrue(DataValidator.validate_age(100))
        self.assertFalse(DataValidator.validate_age(0))
        self.assertFalse(DataValidator.validate_age(101))
    
    def test_validate_bmi(self):
        """Test BMI validation"""
        self.assertTrue(DataValidator.validate_bmi(25.0))
        self.assertTrue(DataValidator.validate_bmi(10.0))
        self.assertTrue(DataValidator.validate_bmi(60.0))
        self.assertFalse(DataValidator.validate_bmi(9.9))
        self.assertFalse(DataValidator.validate_bmi(60.1))
    
    def test_validate_blood_pressure(self):
        """Test blood pressure validation"""
        self.assertTrue(DataValidator.validate_blood_pressure(120))
        self.assertTrue(DataValidator.validate_blood_pressure(60))
        self.assertTrue(DataValidator.validate_blood_pressure(200))
        self.assertFalse(DataValidator.validate_blood_pressure(59))
        self.assertFalse(DataValidator.validate_blood_pressure(201))
    
    def test_validate_children(self):
        """Test children validation"""
        self.assertTrue(DataValidator.validate_children(0))
        self.assertTrue(DataValidator.validate_children(5))
        self.assertTrue(DataValidator.validate_children(8))
        self.assertFalse(DataValidator.validate_children(-1))
        self.assertFalse(DataValidator.validate_children(9))
    
    def test_validate_categorical(self):
        """Test categorical validation"""
        valid_options = ['Yes', 'No']
        self.assertTrue(DataValidator.validate_categorical('Yes', valid_options))
        self.assertTrue(DataValidator.validate_categorical('No', valid_options))
        self.assertFalse(DataValidator.validate_categorical('Maybe', valid_options))

class TestDataProcessor(unittest.TestCase):
    """Test cases for DataProcessor class"""
    
    def test_create_input_dataframe(self):
        """Test DataFrame creation"""
        df = DataProcessor.create_input_dataframe(
            age=30, gender='male', bmi=25.0, bloodpressure=120,
            diabetic='No', children=2, smoker='No'
        )
        
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), 1)
        self.assertEqual(df.iloc[0]['age'], 30)
        self.assertEqual(df.iloc[0]['gender'], 'male')
    
    def test_format_prediction_output(self):
        """Test prediction formatting"""
        formatted = DataProcessor.format_prediction_output(1234.56)
        self.assertEqual(formatted, "$1,234.56")
        
        formatted = DataProcessor.format_prediction_output(10000.00)
        self.assertEqual(formatted, "$10,000.00")

if __name__ == '__main__':
    unittest.main()