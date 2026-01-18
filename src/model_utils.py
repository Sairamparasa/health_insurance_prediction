"""
Model utilities for loading and managing ML models and preprocessors
"""

import joblib
import pandas as pd
import os
from typing import Tuple, Any

class ModelManager:
    """Manages loading and using ML models and preprocessors"""
    
    def __init__(self, models_dir: str = "../models"):
        self.models_dir = models_dir
        self.model = None
        self.scaler = None
        self.encoders = {}
        
    def load_model_components(self) -> None:
        """Load all model components (model, scaler, encoders)"""
        try:
            # Load the trained model
            self.model = joblib.load(os.path.join(self.models_dir, 'best_model.pkl'))
            
            # Load the scaler
            self.scaler = joblib.load(os.path.join(self.models_dir, 'scaler.pkl'))
            
            # Load label encoders
            self.encoders['gender'] = joblib.load(os.path.join(self.models_dir, 'label_encoder_gender.pkl'))
            self.encoders['diabetic'] = joblib.load(os.path.join(self.models_dir, 'label_encoder_diabetic.pkl'))
            self.encoders['smoker'] = joblib.load(os.path.join(self.models_dir, 'label_encoder_smoker.pkl'))
            
            print("✅ All model components loaded successfully!")
            
        except Exception as e:
            print(f"❌ Error loading model components: {str(e)}")
            raise
    
    def get_encoder_classes(self) -> dict:
        """Get available classes for each categorical encoder"""
        if not self.encoders:
            self.load_model_components()
            
        return {
            'gender': self.encoders['gender'].classes_,
            'diabetic': self.encoders['diabetic'].classes_,
            'smoker': self.encoders['smoker'].classes_
        }
    
    def preprocess_input(self, input_data: pd.DataFrame) -> pd.DataFrame:
        """Preprocess input data for prediction"""
        if self.model is None:
            self.load_model_components()
        
        # Create a copy to avoid modifying original data
        processed_data = input_data.copy()
        
        # Encode categorical variables
        processed_data['gender'] = self.encoders['gender'].transform(processed_data['gender'])
        processed_data['diabetic'] = self.encoders['diabetic'].transform(processed_data['diabetic'])
        processed_data['smoker'] = self.encoders['smoker'].transform(processed_data['smoker'])
        
        # Scale numerical features
        num_cols = ['age', 'bmi', 'bloodpressure', 'children']
        processed_data[num_cols] = self.scaler.transform(processed_data[num_cols])
        
        return processed_data
    
    def predict(self, input_data: pd.DataFrame) -> float:
        """Make prediction on preprocessed data"""
        if self.model is None:
            self.load_model_components()
        
        processed_data = self.preprocess_input(input_data)
        prediction = self.model.predict(processed_data)[0]
        
        return prediction