"""
Tests for model utilities
"""

import unittest
import sys
import os
import pandas as pd
from unittest.mock import patch, MagicMock

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from model_utils import ModelManager

class TestModelManager(unittest.TestCase):
    """Test cases for ModelManager class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.model_manager = ModelManager()
    
    @patch('joblib.load')
    def test_load_model_components(self, mock_joblib_load):
        """Test loading model components"""
        # Mock the joblib.load function
        mock_model = MagicMock()
        mock_scaler = MagicMock()
        mock_encoder = MagicMock()
        mock_encoder.classes_ = ['male', 'female']
        
        mock_joblib_load.side_effect = [
            mock_model,  # best_model.pkl
            mock_scaler,  # scaler.pkl
            mock_encoder,  # label_encoder_gender.pkl
            mock_encoder,  # label_encoder_diabetic.pkl
            mock_encoder   # label_encoder_smoker.pkl
        ]
        
        # Test loading
        self.model_manager.load_model_components()
        
        # Verify components are loaded
        self.assertIsNotNone(self.model_manager.model)
        self.assertIsNotNone(self.model_manager.scaler)
        self.assertIn('gender', self.model_manager.encoders)
        self.assertIn('diabetic', self.model_manager.encoders)
        self.assertIn('smoker', self.model_manager.encoders)
    
    def test_create_input_dataframe(self):
        """Test creating input DataFrame with sample data"""
        sample_data = pd.DataFrame({
            'age': [30],
            'gender': ['male'],
            'bmi': [25.0],
            'bloodpressure': [120],
            'diabetic': ['No'],
            'children': [2],
            'smoker': ['No']
        })
        
        self.assertIsInstance(sample_data, pd.DataFrame)
        self.assertEqual(len(sample_data), 1)
        self.assertListEqual(
            list(sample_data.columns),
            ['age', 'gender', 'bmi', 'bloodpressure', 'diabetic', 'children', 'smoker']
        )

if __name__ == '__main__':
    unittest.main()