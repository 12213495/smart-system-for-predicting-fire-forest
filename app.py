import streamlit as st
from model import train_model
from predict import predict_fire

st.title("🌲 Forest Fire Prediction System")

model = train_model()

temperature = st.number_input("Temperature")
humidity = st.number_input("Humidity")
wind = st.number_input("Wind Speed")
rain = st.number_input("Rainfall")

if st.button("Predict"):
    result = predict_fire(model, temperature, humidity, wind, rain)

    if result == 1:
        st.error("🔥 High Risk of Forest Fire")
    else:
        st.success("✅ Low Risk of Forest Fire")
