import cv2
import numpy as np
import streamlit as st

from src.services import arithmetic_operation_on_image, logical_operation_on_image, resize_to_match
from src.views.util_view import display_image

# Display Arithmetic Operation


def display_arithmetic_operation(img):
    try:
        st.subheader("Arithmetic Operation")
        # Select arithmetic operation
        
        operation = st.radio("Select arithmetic operation:", [
            "add",
            "subtract",
            "max",
            "min",
            "inverse"
        ], horizontal=True)

        # Value slider for the operation
        value = st.slider("Value", min_value=0.0,
                          max_value=255.0, value=0.00, step=1.0)
        result_img = arithmetic_operation_on_image(img, value, operation)

        # Display the resulting image
        display_image(result_img, width=200, caption="Result Image", key="arithmetic_result")
        return result_img
    
    except Exception as e:
        st.error(f"Error processing the image: {e}")

# Display logical operation


def display_logical_operation(image1=None, image2=None):
    try:
        st.subheader("Logical Operation")
        # Select logical operation
        logic_operations = st.radio(
            "Select logical operation:", ["and", "xor", "not"], horizontal=True)

        result_img = None
        if logic_operations == "not":
            result_img = logical_operation_on_image(image1, operation="not")
        else:
            # Ensure both images are the same size
            if image1.shape != image2.shape:
                image2 = resize_to_match(image1, image2)

            # Perform the logical operation
            result_img = logical_operation_on_image(
                image1, image2, logic_operations)

        # Display the resulting image
        if result_img is not None:
            display_image(result_img, width=200, caption="Result Image", key="logical_result")

    except Exception as e:
        st.error(f"Error processing the image: {e}")
