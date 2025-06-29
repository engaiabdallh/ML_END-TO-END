import streamlit as st
import pandas as pd
from utils.inference import predict_new 
from utils.config import APP_NAME, VERSION, preprocessor, logistic, forest, xgb
from utils.CostumerData import CostumerData

# Page configuration
st.set_page_config(
    page_title=f"{APP_NAME} v{VERSION}",
    page_icon="🔮",
    layout="wide"
)

# Title and description
st.title(f"🔮 {APP_NAME}")
st.markdown(f"**Version:** {VERSION}")
st.markdown("---")

# Sidebar for model selection
st.sidebar.header("Model Selection")
model_choice = st.sidebar.selectbox(
    "Choose a prediction model:",
    ["Logistic Regression", "Random Forest", "XGBoost"]
)

# Main content area
st.header("Customer Data Input")
st.markdown("Please fill in the customer information below to get a prediction.")

# Create columns for better layout
col1, col2 = st.columns(2)

# You'll need to adjust these fields based on your CostumerData class
# I'm creating a generic form - replace with actual fields from your CostumerData class
with col1:
    st.subheader("Customer Information")
    
    # Example fields - replace with actual fields from CostumerData
    customer_id = st.text_input("Customer ID", help="Enter customer ID")
    age = st.number_input("Age", min_value=18, max_value=100, value=30)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    income = st.number_input("Annual Income", min_value=0, value=50000)
    
with col2:
    st.subheader("Additional Details")
    
    # More example fields - adjust based on your actual data structure
    credit_score = st.number_input("Credit Score", min_value=300, max_value=850, value=650)
    employment_status = st.selectbox("Employment Status", ["Employed", "Unemployed", "Self-employed", "Retired"])
    years_with_company = st.number_input("Years with Company", min_value=0, max_value=50, value=5)
    monthly_charges = st.number_input("Monthly Charges", min_value=0.0, value=100.0)

# Additional fields section
st.subheader("Service Information")
col3, col4 = st.columns(2)

with col3:
    contract_type = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
    payment_method = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer", "Credit card"])

with col4:
    internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    phone_service = st.selectbox("Phone Service", ["Yes", "No"])

# Prediction button
st.markdown("---")
if st.button("🚀 Make Prediction", type="primary"):
    try:
        # Create customer data object
        # You'll need to adjust this based on your actual CostumerData class structure
        customer_data = {
            "customer_id": customer_id,
            "age": age,
            "gender": gender,
            "income": income,
            "credit_score": credit_score,
            "employment_status": employment_status,
            "years_with_company": years_with_company,
            "monthly_charges": monthly_charges,
            "contract_type": contract_type,
            "payment_method": payment_method,
            "internet_service": internet_service,
            "phone_service": phone_service
        }
        
        # Convert to CostumerData object
        data = CostumerData(**customer_data)
        
        # Select model based on user choice
        if model_choice == "Logistic Regression":
            model = logistic
            model_name = "Logistic Regression"
        elif model_choice == "Random Forest":
            model = forest
            model_name = "Random Forest"
        else:
            model = xgb
            model_name = "XGBoost"
        
        # Make prediction
        with st.spinner(f"Making prediction using {model_name}..."):
            result = predict_new(data=data, preprocessor=preprocessor, model=model)
        
        # Display results
        st.success("Prediction completed!")
        
        # Create columns for results display
        result_col1, result_col2 = st.columns(2)
        
        with result_col1:
            st.metric(
                label=f"{model_name} Prediction",
                value=result.get('prediction', 'N/A')
            )
        
        with result_col2:
            if 'probability' in result:
                st.metric(
                    label="Confidence Score",
                    value=f"{result['probability']:.2%}"
                )
        
        # Display full results
        st.subheader("Detailed Results")
        st.json(result)
        
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.info("Please check your input data and try again.")

# Additional information section
st.markdown("---")
with st.expander("ℹ️ About this Application"):
    st.markdown(f"""
    This application uses machine learning models to make predictions based on customer data.
    
    **Available Models:**
    - **Logistic Regression**: A linear model for binary classification
    - **Random Forest**: An ensemble method using multiple decision trees
    - **XGBoost**: A gradient boosting framework
    
    **Version:** {VERSION}
    
    **How to use:**
    1. Fill in the customer information in the form above
    2. Select your preferred prediction model from the sidebar
    3. Click the "Make Prediction" button to get results
    """)

# Footer
st.markdown("---")
st.markdown("*Built with Streamlit* 🎈")