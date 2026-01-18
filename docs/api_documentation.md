# API Documentation

## Overview

This document provides detailed information about the Health Insurance Prediction project's API and components.

## Project Structure

```
health-insurance-prediction/
├── data/                    # Dataset storage
├── models/                  # Trained models and preprocessors
├── notebooks/              # Jupyter notebooks for analysis
├── src/                    # Source code
├── tests/                  # Unit tests
├── docs/                   # Documentation
└── requirements.txt        # Dependencies
```

## Core Components

### ModelManager Class

Located in `src/model_utils.py`

#### Methods:

- `load_model_components()`: Loads all ML models and preprocessors
- `get_encoder_classes()`: Returns available categorical options
- `preprocess_input(data)`: Preprocesses input data for prediction
- `predict(data)`: Makes predictions on input data

#### Usage:

```python
from src.model_utils import ModelManager

manager = ModelManager()
manager.load_model_components()
prediction = manager.predict(input_data)
```

### DataValidator Class

Located in `src/data_preprocessing.py`

#### Methods:

- `validate_age(age)`: Validates age input (1-100)
- `validate_bmi(bmi)`: Validates BMI input (10.0-60.0)
- `validate_blood_pressure(bp)`: Validates BP input (60-200)
- `validate_children(children)`: Validates children count (0-8)
- `validate_input_data(data)`: Validates all input data

### DataProcessor Class

Located in `src/data_preprocessing.py`

#### Methods:

- `create_input_dataframe()`: Creates pandas DataFrame from inputs
- `format_prediction_output()`: Formats prediction for display
- `get_feature_info()`: Returns feature information for UI

## Model Information

### Features Used:
- **age**: Person's age (18-60 years)
- **gender**: Male/Female
- **bmi**: Body Mass Index (16.0-53.1)
- **bloodpressure**: Systolic BP (80-140 mmHg)
- **diabetic**: Yes/No
- **children**: Number of dependents (0-5)
- **smoker**: Yes/No

### Model Types Evaluated:
1. Linear Regression
2. Polynomial Regression
3. Random Forest Regressor
4. Support Vector Regression
5. XGBoost Regressor

### Performance Metrics:
- R² Score (Coefficient of determination)
- MAE (Mean Absolute Error)
- RMSE (Root Mean Square Error)

## Running the Application

### Local Development:
```bash
streamlit run src/app.py
```

### Docker Deployment:
```bash
docker build -t insurance-prediction .
docker run -p 8501:8501 insurance-prediction
```

### Testing:
```bash
python -m pytest tests/
```

## Input Validation

All inputs are validated before processing:

- **Age**: Must be between 1-100 years
- **BMI**: Must be between 10.0-60.0
- **Blood Pressure**: Must be between 60-200 mmHg
- **Children**: Must be between 0-8
- **Categorical fields**: Must match predefined options

## Error Handling

The application includes comprehensive error handling:

- Model loading errors
- Input validation errors
- Prediction errors
- File not found errors

## Security Considerations

- Input validation prevents injection attacks
- No sensitive data is logged
- Models are loaded securely
- Docker container runs as non-root user

## Performance

- Models are cached using Streamlit's `@st.cache_resource`
- Preprocessing is optimized for single predictions
- Memory usage is minimized

## Future Enhancements

- API endpoint for programmatic access
- Batch prediction capability
- Model retraining pipeline
- Advanced visualization features
- Multi-language support