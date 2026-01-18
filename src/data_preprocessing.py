"""
Data preprocessing utilities for the insurance prediction project
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Tuple

class DataValidator:
    """Validates input data for the insurance prediction model"""
    
    @staticmethod
    def validate_age(age: float) -> bool:
        """Validate age input"""
        return 1 <= age <= 100
    
    @staticmethod
    def validate_bmi(bmi: float) -> bool:
        """Validate BMI input"""
        return 10.0 <= bmi <= 60.0
    
    @staticmethod
    def validate_blood_pressure(bp: int) -> bool:
        """Validate blood pressure input"""
        return 60 <= bp <= 200
    
    @staticmethod
    def validate_children(children: int) -> bool:
        """Validate number of children"""
        return 0 <= children <= 8
    
    @staticmethod
    def validate_categorical(value: str, valid_options: List[str]) -> bool:
        """Validate categorical input"""
        return value in valid_options
    
    @classmethod
    def validate_input_data(cls, data: Dict) -> Tuple[bool, List[str]]:
        """Validate all input data and return validation status and errors"""
        errors = []
        
        # Validate numerical inputs
        if not cls.validate_age(data.get('age', 0)):
            errors.append("Age must be between 1 and 100")
        
        if not cls.validate_bmi(data.get('bmi', 0)):
            errors.append("BMI must be between 10.0 and 60.0")
        
        if not cls.validate_blood_pressure(data.get('bloodpressure', 0)):
            errors.append("Blood pressure must be between 60 and 200")
        
        if not cls.validate_children(data.get('children', 0)):
            errors.append("Number of children must be between 0 and 8")
        
        return len(errors) == 0, errors

class DataProcessor:
    """Processes and formats data for model input"""
    
    @staticmethod
    def create_input_dataframe(age: float, gender: str, bmi: float, 
                             bloodpressure: int, diabetic: str, 
                             children: int, smoker: str) -> pd.DataFrame:
        """Create a pandas DataFrame from input parameters"""
        
        input_data = pd.DataFrame({
            'age': [age],
            'gender': [gender],
            'bmi': [bmi],
            'bloodpressure': [bloodpressure],
            'diabetic': [diabetic],
            'children': [children],
            'smoker': [smoker]
        })
        
        return input_data
    
    @staticmethod
    def format_prediction_output(prediction: float) -> str:
        """Format prediction output for display"""
        return f"${prediction:,.2f}"
    
    @staticmethod
    def get_feature_info() -> Dict[str, Dict]:
        """Get information about each feature for the UI"""
        return {
            'age': {
                'type': 'numeric',
                'min': 1,
                'max': 100,
                'default': 30,
                'description': 'Age in years'
            },
            'bmi': {
                'type': 'numeric',
                'min': 10.0,
                'max': 60.0,
                'default': 25.0,
                'description': 'Body Mass Index'
            },
            'bloodpressure': {
                'type': 'numeric',
                'min': 60,
                'max': 200,
                'default': 120,
                'description': 'Systolic blood pressure (mmHg)'
            },
            'children': {
                'type': 'numeric',
                'min': 0,
                'max': 8,
                'default': 0,
                'description': 'Number of dependents'
            },
            'gender': {
                'type': 'categorical',
                'options': ['male', 'female'],
                'description': 'Gender'
            },
            'diabetic': {
                'type': 'categorical',
                'options': ['Yes', 'No'],
                'description': 'Diabetic status'
            },
            'smoker': {
                'type': 'categorical',
                'options': ['Yes', 'No'],
                'description': 'Smoking status'
            }
        }