# app.py
import streamlit as st
from detector import run_detection

st.title("Universal Object Detector 🔍")
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    with open("input.jpg", "wb") as f:
        f.write(uploaded_file.read())
    
    st.image("input.jpg", caption="Uploaded Image", use_column_width=True)
    
    output_img = run_detection("input.jpg")
    st.image(output_img, caption="Detected Image", use_column_width=True)
