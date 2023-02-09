import joblib
import streamlit as st

loaded_model = joblib.load("HeartSurvivalModel.sav")


st.title("Did they survive? :heart:")
