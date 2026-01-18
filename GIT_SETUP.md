# Git Setup Guide

## Quick Setup Commands

### 1. Add all files to staging:
```bash
git add .
```

### 2. Commit your changes:
```bash
git commit -m "Initial commit: Health Insurance Prediction Project

- Added Streamlit web application (app.py)
- Added comprehensive EDA notebook (eda.ipynb)
- Added trained ML models and preprocessors (.pkl files)
- Added insurance dataset (insurance.csv)
- Added detailed README with project documentation
- Added requirements.txt with all dependencies
- Updated .gitignore for Python ML projects"
```

### 3. Push to remote repository:
```bash
git push origin main
```

## Alternative: Step-by-step commit

If you prefer to commit files in logical groups:

### Core application files:
```bash
git add app.py eda.ipynb
git commit -m "Add core application and analysis files"
```

### Documentation and setup:
```bash
git add README.md requirements.txt .gitignore
git commit -m "Add project documentation and setup files"
```

### Data and models:
```bash
git add insurance.csv *.pkl
git commit -m "Add dataset and trained ML models"
```

### Push all commits:
```bash
git push origin main
```

## File Status Summary

✅ **Ready to commit:**
- `README.md` (updated with comprehensive documentation)
- `requirements.txt` (new - all project dependencies)
- `.gitignore` (updated with project-specific exclusions)
- `app.py` (Streamlit web application)
- `eda.ipynb` (data analysis and model training)
- `insurance.csv` (dataset)
- `*.pkl` files (trained models and preprocessors)

## Notes

- All sensitive files are properly ignored
- Models and data files are included (remove from .gitignore if too large)
- Documentation is comprehensive and professional
- Dependencies are clearly specified

## Repository Structure After Push

```
health-insurance-prediction/
├── .gitignore                      # Git ignore rules
├── README.md                       # Project documentation
├── requirements.txt                # Python dependencies
├── app.py                          # Streamlit web app
├── eda.ipynb                       # Data analysis notebook
├── insurance.csv                   # Dataset
├── best_model.pkl                  # Trained ML model
├── scaler.pkl                      # Feature scaler
├── label_encoder_*.pkl             # Categorical encoders
└── GIT_SETUP.md                    # This setup guide
```

Delete this file after setup if desired:
```bash
rm GIT_SETUP.md
```