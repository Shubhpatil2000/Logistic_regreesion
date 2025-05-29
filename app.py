import streamlit as st
import pandas as pd
import joblib
from utils import binary_cleanup
# Load trained model
model = joblib.load("attrition_model.joblib")

st.title("Employee Attrition Prediction")

with st.form("attrition_form"):
    # Collect user inputs
    age = st.slider("Age", 18, 60, 30)
    daily_rate = st.number_input("Daily Rate", 100, 1500, 800)
    distance = st.slider("Distance From Home", 1, 30, 5)
    education = st.selectbox("Education Level", [1, 2, 3, 4, 5])
    env_satisfaction = st.selectbox("Environment Satisfaction", [1, 2, 3, 4])
    gender = st.selectbox("Gender", ["Male", "Female"])
    hourly_rate = st.number_input("Hourly Rate", 20, 150, 60)
    job_involvement = st.selectbox("Job Involvement", [1, 2, 3, 4])
    job_level = st.selectbox("Job Level", [1, 2, 3, 4, 5])
    job_satisfaction = st.selectbox("Job Satisfaction", [1, 2, 3, 4])
    monthly_income = st.number_input("Monthly Income", 1000, 20000, 5000)
    monthly_rate = st.number_input("Monthly Rate", 1000, 25000, 15000)
    num_companies_worked = st.number_input("Num Companies Worked", 0, 10, 2)
    overtime = st.selectbox("OverTime", ["Yes", "No"])
    percent_salary_hike = st.slider("Percent Salary Hike", 0, 100, 15)
    performance_rating = st.selectbox("Performance Rating", [1, 2, 3, 4])
    relationship_satisfaction = st.selectbox("Relationship Satisfaction", [1, 2, 3, 4])
    stock_option_level = st.selectbox("Stock Option Level", [0, 1, 2, 3])
    total_working_years = st.number_input("Total Working Years", 0, 40, 8)
    training_times = st.selectbox("Training Times Last Year", list(range(0, 10)))
    work_life_balance = st.selectbox("Work Life Balance", [1, 2, 3, 4])
    years_at_company = st.number_input("Years At Company", 0, 40, 4)
    years_in_role = st.number_input("Years In Current Role", 0, 20, 2)
    years_since_promo = st.number_input("Years Since Last Promotion", 0, 15, 1)
    years_with_manager = st.number_input("Years With Current Manager", 0, 20, 2)
    business_travel = st.selectbox("Business Travel", ["Non-Travel", "Travel_Rarely", "Travel_Frequently"])
    department = st.selectbox("Department", ["Sales", "Research & Development", "Human Resources"])
    education_field = st.selectbox("Education Field", ["Life Sciences", "Medical", "Marketing", "Technical Degree", "Human Resources", "Other"])
    job_role = st.selectbox("Job Role", [
        "Sales Executive", "Research Scientist", "Laboratory Technician", "Manufacturing Director",
        "Healthcare Representative", "Manager", "Sales Representative", "Research Director", "Human Resources"
    ])
    marital_status = st.selectbox("Marital Status", ["Single", "Married", "Divorced"])

    submit = st.form_submit_button("Predict")

if submit:
    # Assemble input into dataframe
    input_data = pd.DataFrame([{
        'Age': age,
        'DailyRate': daily_rate,
        'DistanceFromHome': distance,
        'Education': education,
        'EnvironmentSatisfaction': env_satisfaction,
        'Gender': gender,
        'HourlyRate': hourly_rate,
        'JobInvolvement': job_involvement,
        'JobLevel': job_level,
        'JobSatisfaction': job_satisfaction,
        'MonthlyIncome': monthly_income,
        'MonthlyRate': monthly_rate,
        'NumCompaniesWorked': num_companies_worked,
        'OverTime': overtime,
        'PercentSalaryHike': percent_salary_hike,
        'PerformanceRating': performance_rating,
        'RelationshipSatisfaction': relationship_satisfaction,
        'StockOptionLevel': stock_option_level,
        'TotalWorkingYears': total_working_years,
        'TrainingTimesLastYear': training_times,
        'WorkLifeBalance': work_life_balance,
        'YearsAtCompany': years_at_company,
        'YearsInCurrentRole': years_in_role,
        'YearsSinceLastPromotion': years_since_promo,
        'YearsWithCurrManager': years_with_manager,
        'BusinessTravel': business_travel,
        'Department': department,
        'EducationField': education_field,
        'JobRole': job_role,
        'MaritalStatus': marital_status,
        'EmployeeCount': 1,
        'Over18': 'Y',
        'StandardHours': 80,
        'EmployeeNumber': 9999
    }])

    # Predict
    prediction = model.predict(input_data)[0]
    result = "Yes (Will Leave)" if prediction == 1 else "No (Will Stay)"
    
    st.subheader("Prediction Result:")
    st.success(result)
