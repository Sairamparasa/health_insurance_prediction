# Health Insurance Payment Prediction

A machine learning project that predicts health insurance claim amounts based on personal and health characteristics using multiple regression algorithms and a user-friendly Streamlit web interface.

## 🎯 Project Overview

This project analyzes health insurance data to build predictive models that estimate insurance claim amounts. The system uses various personal and health metrics to provide accurate predictions through an interactive web application.

## 📊 Dataset

The project uses an insurance dataset (`insurance.csv`) containing **1,340 records** with the following features:

### Input Features:
- **Age**: Person's age (18-60 years)
- **Gender**: Male/Female
- **BMI**: Body Mass Index (16.0-53.1)
- **Blood Pressure**: Systolic blood pressure (80-140 mmHg)
- **Diabetic**: Yes/No
- **Children**: Number of dependents (0-5)
- **Smoker**: Yes/No
- **Region**: Geographic region (southeast, northwest, southwest, northeast)

### Target Variable:
- **Claim**: Insurance payment amount  ($1,121 - $63,770)

## 🤖 Machine Learning Models

The project implements and compares multiple regression algorithms:

1. **Linear Regression** - Baseline model
2. **Polynomial Regression** - Non-linear relationships (degrees 2-3)
3. **Random Forest Regressor** - Ensemble method with hyperparameter tuning
4. **Support Vector Regression (SVR)** - Kernel-based approach
5. **XGBoost Regressor** - Gradient boosting algorithm

### Model Selection Process:
- **Cross-validation** for robust evaluation
- **GridSearchCV** for hyperparameter optimization
- **Multiple metrics**: R², MAE, RMSE for comprehensive assessment
- **Best model selection** based on performance metrics

## 🚀 Web Application

Interactive Streamlit web app (`app.py`) features:

### User Interface:
- **Clean, intuitive form** with input validation
- **Real-time predictions** with formatted currency output
- **Responsive design** with organized layout
- **Input ranges** to prevent invalid entries

### Input Validation:
- Age: 1-100 years
- BMI: 10.0-60.0
- Blood Pressure: 60-200 mmHg
- Children: 0-8
- Dropdown selections for categorical variables

## 📁 Project Structure

```
health-insurance-prediction/
├── 📁 data/
│   └── insurance.csv                    # Dataset
├── 📁 models/
│   ├── best_model.pkl                   # Trained ML model
│   ├── scaler.pkl                       # Feature scaler
│   ├── label_encoder_diabetic.pkl       # Diabetic status encoder
│   ├── label_encoder_gender.pkl         # Gender encoder
│   └── label_encoder_smoker.pkl         # Smoker status encoder
├── 📁 notebooks/
│   └── eda.ipynb                        # Data analysis & model training
├── 📁 src/
│   └── app.py                           # Streamlit web application
├── 📁 tests/                            # Test files (empty)
├── 📁 docs/                             # Documentation (empty)
├── .gitignore                           # Git ignore rules
├── README.md                            # Project documentation
├── requirements.txt                     # Python dependencies
└── GIT_SETUP.md                         # Git setup guide
```

## 🛠️ Installation & Setup

### Prerequisites:
- Python 3.7+
- pip package manager

### Installation Steps:

1. **Clone the repository:**
```bash
git clone <repository-url>
cd health-insurance-prediction
```

2. **Create virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

### Required Libraries:
- streamlit
- pandas
- numpy
- scikit-learn
- xgboost
- joblib
- matplotlib
- seaborn

## 🏃‍♂️ Usage

### Running the Web Application:
```bash
streamlit run src/app.py
```

The app will open in your browser at `http://localhost:8501`

### Using the Prediction Interface:
1. Enter your personal information (age, gender, children)
2. Input health metrics (BMI, blood pressure, diabetic status, smoker status)
3. Click "Predict Payment" button
4. View your estimated insurance claim amount

### Exploring the Analysis:
Open `eda.ipynb` in Jupyter Notebook to see:
- Data exploration and visualization
- Feature engineering process
- Model training and evaluation
- Performance comparisons

## 📈 Model Performance

The project evaluates models using:
- **R² Score**: Coefficient of determination
- **MAE**: Mean Absolute Error
- **RMSE**: Root Mean Square Error

Best performing model is automatically selected and saved as `best_model.pkl`.

## 🔍 Key Features

### Data Preprocessing:
- **Missing value handling**: Automatic detection and removal
- **Feature scaling**: StandardScaler for numerical features
- **Label encoding**: Categorical variable transformation
- **Data validation**: Input range checking

### Model Training:
- **Automated pipeline**: From raw data to deployed model
- **Hyperparameter tuning**: Grid search optimization
- **Cross-validation**: Robust performance estimation
- **Model persistence**: Pickle serialization for deployment

### Web Interface:
- **User-friendly design**: Intuitive form layout
- **Real-time processing**: Instant predictions
- **Error handling**: Input validation and feedback
- **Professional styling**: Clean, modern interface

## 🎯 Use Cases

- **Insurance Companies**: Risk assessment and premium calculation
- **Healthcare Providers**: Cost estimation for treatments
- **Individual Users**: Personal insurance planning
- **Data Scientists**: ML model development reference

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 📞 Contact

For questions or suggestions, please open an issue in the repository.

---

**Built with ❤️ using Python, Scikit-learn, and Streamlit**
