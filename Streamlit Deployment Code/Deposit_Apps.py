import numpy as np
import pandas as pd
import streamlit as st
import pickle
import base64

st.markdown("<h1 style='text-align: center; color: black; font-size: 37px;'>ABANCA Bank Potential Customer Prediction</h1>", unsafe_allow_html=True)
# st.title(':black[Potential Customer Prediction]')

with open(r"term_deposit_prediction.sav", 'rb') as f:
    model_loaded = pickle.load(f)

import base64

def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64(r"5b87da.png")
img2 = get_img_as_base64(r"banco_abanca.jpg")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("data:image/png;base64,{img2}");
background-size: 115%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}

[data-testid="stSidebar"] > div:first-child {{
background-image: url("data:image/png;base64,{img}");
background-size: 125%;
background-position: center; 
background-repeat: no-repeat;
background-attachment: fixed;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

st.sidebar.markdown("<h2 style='text-align: center; color: black; font-size: 20px;'>Please input customer's personal data!</h2>", unsafe_allow_html=True)

Age_Input = st.sidebar.number_input("Please input customer's age", min_value= 17, max_value= 98)
Job_Input = st.sidebar.selectbox("Please input customer's job type", ['Student', 'Unemployed', 'Housemaid', 'Services', 'Admin', 'Blue-collar', 'Technician', 'Management', 'Entrepreneur', 'Self-Employed', 'Retired'])
Marital_Input = st.sidebar.radio("Please input customer's marital status", ['Single', 'Married', 'Divorced'])
Education_Input = st.sidebar.selectbox("Please input customer's education level", ['Basic 4y', 'Basic 6y', 'Basic 9y', 'High School', 'Professional Course', 'University Degree'])
Housing_Input = st.sidebar.radio("Does customer have a housing loan ?", ['Yes', 'No'])
Loan_Input = st.sidebar.radio("Does customer have a personal loan (except housing) ?", ['Yes', 'No'])
Contact_Input = st.sidebar.radio("What would you like to call through to customer ?", ['Telephone', 'Cellular'])
Month_Input = st.sidebar.selectbox("What month would you like to call to customer ?", ['March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
Day_Input = st.sidebar.selectbox("What day would you like to call to customer ?", ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
Campaign_Input = st.sidebar.number_input("Please input the number of times you want to call the customer", min_value= 1, max_value= 12)
Emp_Var_Rate_Input = st.sidebar.number_input("Please input its emp.var.rate value", min_value= -3.0, max_value= 1.4)
Cons_Price_Idx_Input = st.sidebar.number_input("Please input its cons.price.idx value", min_value= 92.201, max_value= 94.767)
Cons_Conf_Idx_Input = st.sidebar.number_input("Please input its cons.conf.idx value", min_value= -50.8, max_value= -26.9)
Euribor3m_Input = st.sidebar.number_input("Please input its euribor3m value", min_value= 0.634, max_value= 5.045)
NR_Employed_Input = st.sidebar.number_input("Please input its nr.employed value", min_value= 4963.6, max_value= 5228.1)

if (Job_Input == 'Student'):
    Job_Input = 'student'
elif (Job_Input == 'Unemployed'):
    Job_Input = 'unemployed'
elif (Job_Input == 'Housemaid'):
    Job_Input = 'housemaid'
elif (Job_Input == 'Services'):
    Job_Input = 'services'
elif (Job_Input == 'Admin'):
    Job_Input = 'admin'
elif (Job_Input == 'Blue-collar'):
    Job_Input = 'blue-collar'
elif (Job_Input == 'Technician'):
    Job_Input = 'technician'
elif (Job_Input == 'Management'):
    Job_Input = 'management'
elif (Job_Input == 'Entrepreneur'):
    Job_Input = 'entrepreneur'
elif (Job_Input == 'Self-Employed'):
    Job_Input = 'self-employed'
else:
    Job_Input = 'retired'

if (Marital_Input == 'Single'):
    Marital_Input = 'single'
elif (Marital_Input == 'Married'):
    Marital_Input = 'married'
else:
    Marital_Input = 'divorced'

if (Education_Input == 'Basic 4y'):
    Education_Input = 'basic.4y'
elif(Education_Input == 'Basic 6y'):
    Education_Input = 'basic.6y'
elif(Education_Input == 'Basic 9y'):
    Education_Input = 'basic.9y'
elif(Education_Input == 'High School'):
    Education_Input = 'high.school'
elif(Education_Input == 'Professional Course'):
    Education_Input = 'professional.course'
else:
    Education_Input = 'university.degree'

if (Housing_Input == 'Yes'):
    Housing_Input = 'yes'
else:
    Housing_Input = 'no'

if (Loan_Input == 'Yes'):
    Loan_Input = 'yes'
else:
    Loan_Input = 'no'

if (Contact_Input == 'Telephone'):
    Contact_Input = 'telephone'
else:
    Contact_Input = 'cellular'

if (Month_Input == 'March'):
    Month_Input = 'mar'
elif (Month_Input == 'April'):
    Month_Input = 'apr'
elif (Month_Input == 'May'):
    Month_Input = 'may'
elif (Month_Input == 'June'):
    Month_Input = 'jun'
elif (Month_Input == 'July'):
    Month_Input = 'jul'
elif (Month_Input == 'August'):
    Month_Input = 'aug'
elif (Month_Input == 'September'):
    Month_Input = 'sep'
elif (Month_Input == 'October'):
    Month_Input = 'oct'
elif (Month_Input == 'November'):
    Month_Input = 'nov'
else:
    Month_Input = 'dec'

if (Day_Input == 'Monday'):
    Day_Input = 'mon'
elif (Day_Input == 'Tuesday'):
    Day_Input = 'tue'
elif (Day_Input == 'Wednesday'):
    Day_Input = 'wed'
elif (Day_Input == 'Thursday'):
    Day_Input = 'thu'
else:
    Day_Input = 'fri'

df = pd.DataFrame()
df['age'] = [Age_Input]
df['job'] = [Job_Input]
df['marital'] = [Marital_Input]
df['education'] = [Education_Input]
df['housing'] = [Housing_Input]
df['loan'] = [Loan_Input]
df['contact'] = [Contact_Input]
df['month'] = [Month_Input]
df['day_of_week'] = [Day_Input]
df['campaign'] = [Campaign_Input]
df['emp.var.rate'] = [Emp_Var_Rate_Input]
df['cons.price.idx'] = [Cons_Price_Idx_Input]
df['cons.conf.idx'] = [Cons_Conf_Idx_Input]
df['euribor3m'] = [Euribor3m_Input]
df['nr.employed'] = [NR_Employed_Input]

df.index = ['Value']

st.dataframe(df.T, width=400)

if st.button('Predict'):
    result = model_loaded.predict(df)
    if result == 1:
        st.write("This model predicts this customer WILL TERM DEPOSIT.")
    elif result == 0:
        st.write("This model predicts this customer WILL NOT TERM DEPOSIT.")
else:
    st.write('Please input the correct data!')