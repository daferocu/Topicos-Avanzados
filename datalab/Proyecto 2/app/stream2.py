import streamlit as st
import requests

st.title("Clasificador de Sentimiento")

texto_input = st.text_area("Ingrese el texto aquí:")

if st.button("Predecir"):
    url = "http://127.0.0.1:8000/predict/"  # Reemplazar con la URL de tu API
    data = {"texto": texto_input}
    response = requests.post(url, json=data)
    prediccion = response.json()
    st.write("La predicción es:", prediccion)
