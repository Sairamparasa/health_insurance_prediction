"""
Health Insurance Payment Prediction App
A Streamlit web application for predicting insurance claim amounts
"""

import streamlit as st
import pandas as pd
import numpy as np
import sys
import os

# Add the src directory to the path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from model_utils import ModelManager
from data_preprocessing import DataValidator, DataProcessor

# Initialize the model manager
@st.cache_resource
def load_model_manager():
    """Load and cache the model manager"""
    manager = ModelManager(models_dir="../models")
    manager.load_model_components()
    return manager

def main():
    """Main application function"""
    
    # Page configuration
    st.set_page_config(
        page_title='Insurance Claim Predictor',
        page_icon='🏥',
        layout='centered',
        initial_sidebar_state='collapsed'
    )
    
    # Header
    st.title("🏥 Health Insurance Payment Prediction")
    st.markdown("---")
    st.write("Enter your details below to get an estimated insurance claim amount based on our machine learning model.")
    
    # Load model manager
    try:
        model_manager = load_model_manager()
        encoder_classes = model_manager.get_encoder_classes()
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        st.stop()
    
    # Create input form
    with st.form('prediction_form'):
        st.subheader("📋 Personal & Health Information")
        
        # Create two columns for better layout
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Personal Details**")
            age = st.number_input(
                'Age (years)',
                min_value=1,
                max_value=100,
                value=30,
                help="Your age in years"
            )
            
            gender = st.selectbox(
                "Gender",
                options=encoder_classes['gender'],
                help="Select your gender"
            )
            
            children = st.number_input(
                "Number of Children",
                min_value=0,
                max_value=8,
                value=0,
                help="Number of dependents"
            )
        
        with col2:
            st.markdown("**Health Metrics**")
            bmi = st.number_input(
                'BMI (Body Mass Index)',
                min_value=10.0,
                max_value=60.0,
                value=25.0,
                step=0.1,
                help="Your Body Mass Index"
            )
            
            bloodpressure = st.number_input(
                "Blood Pressure (Systolic)",
                min_value=60,
                max_value=200,
                value=120,
                help="Systolic blood pressure in mmHg"
            )
            
            diabetic = st.selectbox(
                "Diabetic Status",
                options=encoder_classes['diabetic'],
                help="Are you diabetic?"
            )
            
            smoker = st.selectbox(
                "Smoking Status",
                options=encoder_classes['smoker'],
                help="Do you smoke?"
            )
        
        # Submit button
        st.markdown("---")
        submitted = st.form_submit_button(
            ' Predict Insurance Amount',
            use_container_width=True
        )
    
    # Process prediction when form is submitted
    if submitted:
        # Validate input data
        input_dict = {
            'age': age,
            'bmi': bmi,
            'bloodpressure': bloodpressure,
            'children': children
        }
        
        is_valid, errors = DataValidator.validate_input_data(input_dict)
        
        if not is_valid:
            st.error("❌ Input Validation Errors:")
            for error in errors:
                st.error(f"• {error}")
        else:
            try:
                # Create input DataFrame
                input_data = DataProcessor.create_input_dataframe(
                    age=age,
                    gender=gender,
                    bmi=bmi,
                    bloodpressure=bloodpressure,
                    diabetic=diabetic,
                    children=children,
                    smoker=smoker
                )
                
                # Make prediction
                prediction = model_manager.predict(input_data)
                formatted_prediction = DataProcessor.format_prediction_output(prediction)
                
                # Display result
                st.success(f"✅ **Estimated Insurance Claim Amount:** {formatted_prediction}")
                
                # Additional information
                with st.expander("📊 Prediction Details"):
                    st.write("**Input Summary:**")
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.write(f"• Age: {age} years")
                        st.write(f"• Gender: {gender}")
                        st.write(f"• BMI: {bmi}")
                        st.write(f"• Children: {children}")
                    
                    with col2:
                        st.write(f"• Blood Pressure: {bloodpressure} mmHg")
                        st.write(f"• Diabetic: {diabetic}")
                        st.write(f"• Smoker: {smoker}")
                    
                    st.info("💡 This prediction is based on historical data and machine learning algorithms. Actual insurance costs may vary.")
                
            except Exception as e:
                st.error(f"❌ Error making prediction: {str(e)}")
    
    # Footer
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center; color: #666;'>
            <small>Built with ❤️ using Streamlit and Scikit-learn</small>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()