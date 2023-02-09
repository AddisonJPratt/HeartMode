import joblib
import streamlit as st
import numpy as np
import pandas as pd

loaded_model = joblib.load("filename.joblib")

columns = [
    "ejection_fraction",
    "high_blood_pressure",
    "serum_creatinine",
    "time",
    "age",
    "diabetes",
]

st.title("Predicting the Survival of Patients with Heart Failure :heart:")
st.subheader(
    "A machine learning classifer to determine if a heart failure patient will survive"
)

ejection_fraction = st.slider("Select ejection fraction", 0, 100, 25)

pressure_input = st.radio("Does the patient have high blood pressure?", ("Yes", "No"))

if pressure_input == "Yes":
    high_blood_pressure = 1
else:
    high_blood_pressure = 0

diabetes_input = st.radio("Does the patient have diabetes?", ("Yes", "No"))

if diabetes_input == "Yes":
    diabetes = 1
else:
    diabetes = 0

serum_creatinine = st.number_input("What are the patient's serum creatinine levels?")

time = st.slider("what was the follow up time in days?", 0, 300, 4)

age = st.slider("What is the age of the patient?", 0, 100, 40)


def predict():
    row = np.array(
        [
            ejection_fraction,
            high_blood_pressure,
            serum_creatinine,
            time,
            age,
            diabetes,
        ]
    )
    X = pd.DataFrame([row], columns=columns)
    prediction = loaded_model.predict(X)[0]

    if prediction == 1:
        st.error("The patient will not survive :disappointed_relieved:")
    else:
        st.success("The patient will survive :thumbsup:")


st.button("Predict", on_click=predict)
