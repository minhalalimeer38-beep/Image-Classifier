import streamlit as st
import requests
from PIL import Image

st.title("🧠 MNIST Digit Classifier")

file = st.file_uploader("Upload Digit Image", type=["png", "jpg", "jpeg"])

if file:
    st.image(file)

    if st.button("Predict"):
        response = requests.post(
            "https://minhalali12-image-classifier.hf.space/docs#/default/predict_predict_post",
            files={"file": file.getvalue()}
        )

        st.write("Prediction:", response.json()["digit"])
