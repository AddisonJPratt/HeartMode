import joblib
import streamlit as st
import numpy as np

loaded_model = joblib.load("filename.joblib")


st.title("Did they survive? :heart:")
lst = np.arange(1, 101).tolist()
st.select_slider("Select ejection fraction", lst)
