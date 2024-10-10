import streamlit as st
import requests
import ast

# URL FastAPI
API_URL = "http://127.0.0.1:8000/predict/"

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
    # st.write(input_data)
    response = requests.post(API_URL, json=input_data)
    # st.write(response.json())
    prediction = response.json()

    # st.write(f"Film prediction:")
    prediction = prediction[0]
    inicio = prediction.find('(') + 1
    fin = prediction.find(')')
    prediction = prediction[inicio:fin]
    prediction = ast.literal_eval(prediction)
    salidas = []
    for elemento in prediction:

        salidas.append(elemento) 
        
        # st.write(f"{elemento}")


    st.write(f"Film prediction: {" ".join(salidas)}.")

    # st.write(f"Film prediction: {prediction[0]}")
