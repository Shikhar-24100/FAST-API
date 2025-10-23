import streamlit as st
import requests

FASTAPI_URL = "http://127.0.0.1:8000/predict"  # Must match your running FastAPI app

st.set_page_config(page_title="Iris Flower Predictor 🌸", layout="centered")

st.title("🌸 Iris Flower Variety Predictor")
st.write("Enter the flower’s measurements below to predict its variety using the trained ML model.")

# Input fields
sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0, format="%.2f")
sepal_width = st.number_input("Sepal Width (cm)", min_value=0.0, format="%.2f")
petal_length = st.number_input("Petal Length (cm)", min_value=0.0, format="%.2f")
petal_width = st.number_input("Petal Width (cm)", min_value=0.0, format="%.2f")

if st.button("🔮 Predict"):
    payload = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width
    }

    try:
        response = requests.post(FASTAPI_URL, json=payload)
        if response.status_code == 200:
            result = response.json()
            prediction = result.get("predicted_category")
            st.success(f"🌼 Predicted Iris Variety: **{prediction}**")
        else:
            st.error(f"❌ API Error {response.status_code}: {response.text}")
    except Exception as e:
        st.error(f"🚫 Could not connect to backend: {e}")
