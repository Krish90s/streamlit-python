import streamlit as st
from PIL import Image  # Image processing


st.title("Image OCR App")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
  try:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

  except Exception as e:
    st.error(f"Error processing image: {e}")