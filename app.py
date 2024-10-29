import streamlit as st
import numpy as np
import pickle
import time

# Load the pre-trained model
with open("ada_boost_model.pkl", "rb") as file:
    model = pickle.load(file)

# Custom CSS for vibrant styling
st.markdown(
    """
    <style>
    body {
        background-color: #f0f2f6;
    }
    .main-title {
        color: #f44336;
        font-size: 40px;
        text-align: center;
        font-weight: bold;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.4);
    }
    .section-title {
        color: #ff5722;
        font-size: 30px;
        font-weight: bold;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
    }
    .predict-button {
        background-color: #ff9800;
        color: white;
        border: none;
        padding: 10px 20px;
        font-size: 20px;
        cursor: pointer;
        text-align: center;
        width: 100%;
        border-radius: 5px;
        box-shadow: 0px 4px 8px rgba(0,0,0,0.2);
    }
    .predict-button:hover {
        background-color: #ffb74d;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App title
st.markdown('<h1 class="main-title">Loan Prediction App 💼💰</h1>', unsafe_allow_html=True)
st.markdown("### Powered by Machine Learning")

# User input for each feature with animations
st.markdown('<h3 class="section-title">Applicant Information</h3>', unsafe_allow_html=True)
applicant_income = st.number_input("Applicant Income", min_value=0, step=100)
coapplicant_income = st.number_input("Coapplicant Income", min_value=0, step=100)
loan_amount = st.number_input("Loan Amount", min_value=0, step=1)
loan_amount_term = st.number_input("Loan Amount Term (in days)", min_value=0, step=1)
credit_history = st.selectbox("Credit History", [1, 0])

# Additional Information
st.markdown('<h3 class="section-title">Additional Information</h3>', unsafe_allow_html=True)
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

# Convert user inputs to the appropriate binary/categorical format
gender_female, gender_male = int(gender == "Female"), int(gender == "Male")
married_no, married_yes = int(married == "No"), int(married == "Yes")
dependents_0 = int(dependents == "0")
dependents_1 = int(dependents == "1")
dependents_2 = int(dependents == "2")
dependents_3_plus = int(dependents == "3+")
education_graduate = int(education == "Graduate")
education_not_graduate = int(education == "Not Graduate")
self_employed_no = int(self_employed == "No")
self_employed_yes = int(self_employed == "Yes")
property_area_rural = int(property_area == "Rural")
property_area_semiurban = int(property_area == "Semiurban")
property_area_urban = int(property_area == "Urban")

# Compile all inputs into a single array for model prediction
features = np.array([[applicant_income, coapplicant_income, loan_amount, loan_amount_term, credit_history,
                      gender_female, gender_male, married_no, married_yes, dependents_0, dependents_1,
                      dependents_2, dependents_3_plus, education_graduate, education_not_graduate,
                      self_employed_no, self_employed_yes, property_area_rural, property_area_semiurban,
                      property_area_urban]])

# Predict with animation
if st.button("Predict Loan Status", key="predict_button"):
    with st.spinner("Processing... 🔄"):
        time.sleep(2)  # Simulate a loading time
        prediction = model.predict(features)
        loan_status = "Approved ✅" if prediction == 1 else "Rejected ❌"
        st.success(f"Loan Status Prediction: **{loan_status}**")
