import streamlit as st
import requests
import pandas as pd

# URL FastAPI
# API_URL = "http://Fastapi:8000/predict"
API_URL = "http://127.0.0.1:8000/predict"

# Title
st.title("Film prediction")

summary = st.text_area("Please enter your text here:")

# Botón
if st.button("Predict"):
    # dictionary to send predict api
    input_data = {
        "summary": summary,
    } 

    # testeo
    st.write(input_data)
    response = requests.post('http://127.0.0.1:8000/predict/', json=input_data)
    st.write(response.json())
    prediction = response.json()
    st.write(f"Film prediction: {prediction}")
