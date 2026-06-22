import streamlit as st
import requests
from PIL import Image

st.title("🧠 MNIST Digit Classifier")

file = st.file_uploader("Upload Digit Image", type=["png", "jpg", "jpeg"])

if file:
    st.image(file)

    if st.button("Predict"):
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            files={"file": file.getvalue()}
        )

        st.write("Prediction:", response.json()["digit"])