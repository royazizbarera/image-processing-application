



import streamlit as st

from src.services import convert_to_gray_scale, histogram_gray_scale
from src.views.util_view import display_image



def display_grayscale_image(image):
    image = convert_to_gray_scale(image)
    st.subheader("Grayscale Image")
    display_image(image, caption="Grayscale Image", key="grayscale_image")