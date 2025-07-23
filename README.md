# Data-Driven-Salary-Forecasting

📊 Data-Driven Salary Forecasting

This project uses machine learning to predict employee salaries based on job descriptions and company attributes. It leverages a real-world dataset containing job postings to train a regression model, and is deployed via a simple Streamlit web application.

📁 Dataset
Source: Kaggle

Filename: data job posts.csv

Size: ~95 MB

Description: Contains job titles, employment types, company info, locations, and salary estimates.

🧠 Project Overview

Goal: Predict employee salary based on job and company features.

Model Used: RandomForestRegressor

Libraries: Pandas, Scikit-learn, Joblib, Streamlit

🔧 System Requirements
Python 3.8+

Libraries:

pandas

scikit-learn

joblib

streamlit

Install using:

bash
Copy
Edit
pip install pandas scikit-learn joblib streamlit
⚙️ How It Works

Data Preprocessing: Select important columns, handle missing values, encode categorical data.

Model Training: Random Forest Regressor is trained on the cleaned dataset.

Saving Components: Model, scaler, and input columns saved using joblib.

Streamlit App: Users enter job details; app predicts salary in real time.

🚀 Run Locally
Clone the repo or download the files.

Place salary_model.pkl, scaler.pkl, and columns.pkl in your directory.

Run the app:

bash
Copy
Edit
streamlit run app.py
🖥️ Streamlit UI Features

Dropdowns for job title, location, function, industry, employment type

Instant salary prediction

Clean, simple interface

📌 Files
File	Description
app.py	Main Streamlit app
salary_model.pkl	Trained salary prediction model
scaler.pkl	Feature scaler for preprocessing
columns.pkl	Column names used in model training
data job posts.csv	Dataset used to train the model

📚 Learnings

Practical ML model training and evaluation

Data cleaning and feature engineering

Saving/loading models with joblib

Deploying ML model using Streamlit

✅ To Do

Add model evaluation metrics to the app

Improve input validation

Explore deep learning for better predictions

