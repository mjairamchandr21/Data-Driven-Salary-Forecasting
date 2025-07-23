import streamlit as st
import pandas as pd
import joblib

# Load the model and other components
model = joblib.load("salary_model.pkl")
scaler = joblib.load("scaler.pkl")
columns = joblib.load("columns.pkl")

st.title("💼 Data-Driven Salary Forecasting App")

st.subheader("Enter Job Details")

# Input from user
title = st.selectbox("Job Title", ['Software Engineer', 'Data Scientist', 'Web Developer'])
location = st.selectbox("Location", ['New York', 'San Francisco', 'Remote'])
function = st.selectbox("Function", ['Engineering', 'Data', 'AI'])
industry = st.selectbox("Industry", ['Tech', 'Finance', 'Healthcare'])
emp_type = st.selectbox("Employment Type", ['Full-time', 'Contract'])

# Build DataFrame
input_df = pd.DataFrame([[title, location, function, industry, emp_type]],
                        columns=['Title', 'Location', 'Function', 'Industry', 'Employment.Type'])

# One-hot encode
input_encoded = pd.get_dummies(input_df)

# Match with training columns
for col in columns:
    if col not in input_encoded:
        input_encoded[col] = 0

input_encoded = input_encoded[columns]

# Scale
input_scaled = scaler.transform(input_encoded)

# Predict
if st.button("Predict Salary"):
    prediction = model.predict(input_scaled)[0]
    st.success(f"💰 Estimated Salary: ${int(prediction):,}")

