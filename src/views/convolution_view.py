import streamlit as st

from src.services import apply_convolution, apply_filter, apply_fourier_transform, apply_salt_and_pepper_noise, apply_zero_padding, hex_to_rgb, reduce_periodic_noise, remove_noise, sharpen_image
from src.views.util_view import display_image


def display_apply_convolution(image):
    st.subheader("Apply Convolution")

    # Pilihan kernel
    kernel = st.radio("Select kernel:", [
        "edge_detection",
        "sharpen",
        "average",
    ], horizontal=True)

    # Apply convolution
    result_img = apply_convolution(image, kernel)

    ori, result = st.columns(2)
    with ori:
        display_image(image, caption="Original Image", key="original_image_convolution")
    with result:
        display_image(result_img, caption="Result Image", key="result_image_convolution")


def display_zero_padding(image):
    st.subheader("Zero Padding")

    # set color picker
    color = st.color_picker("Pick a color", "#FFFFFF")
    color = hex_to_rgb(color)
    # Set padding size
    padding_size = st.slider("Padding size", min_value=0,
                             max_value=255, value=1, step=1)
    result_img = apply_zero_padding(image, padding_size, color)
    ori, result = st.columns(2)
    with ori:
        display_image(image, caption="Original Image", key="original_image_zero_padding")

    with result:
        display_image(result_img, caption="Result Image", key="result_image_zero_padding")


# Display Filter
def display_filter(image):
    st.subheader("Filter")

    # Pilihan filter
    filter = st.radio("Select filter:", [
        "low",
        "high",
        "band",
    ], horizontal=True)

    # Apply convolution
    result_img = apply_filter(image, filter)

    ori, result = st.columns(2)
    with ori:
        display_image(image, caption="Original Image", key="original_image_filter")
    with result:
        display_image(result_img, caption="Result Image", key="result_image_filter")


def display_fourier_transform(image):
    st.subheader("Fourier Transform")

    # Apply fourier transform
    result_img = apply_fourier_transform(image)

    ori, result = st.columns(2)
    with ori:
        display_image(image, caption="Original Image", key="original_image_fourier")
    with result:
        display_image(result_img, caption="Result Image", key="result_image_fourier")
        
        
def display_reduce_periodic_noise(image):
    st.subheader("Reduce Periodic Noise")

    # Apply fourier transform
    result_img = reduce_periodic_noise(image)

    ori, result = st.columns(2)
    with ori:
        display_image(image, caption="Original Image", key="original_image_periodic_noise")
    with result:
        display_image(result_img, caption="Result Image", key="result_image_periodic_noise")
        
        
def display_apply_salt_and_pepper_noise(image):
    st.subheader("Add Salt and Pepper Noise")
    
    # Set noise percentage
    noise_percentage = st.slider("Noise percentage", min_value=0.0, max_value=1.0, value=0.0, step=0.01)
    
    # pick color for salt and pepper
    col_salt, col_pepper = st.columns(2)
    
    with col_salt:
        salt_color = st.color_picker("Pick a color for salt", "#FFFFFF")
    
    with col_pepper:
        pepper_color = st.color_picker("Pick a color for pepper", "#000000")
    
    salt_color = hex_to_rgb(salt_color)
    pepper_color = hex_to_rgb(pepper_color)
    
    # Apply salt and pepper noise
    result_img = apply_salt_and_pepper_noise(image, noise_percentage, salt_color, pepper_color)
    
    ori, result = st.columns(2)
    with ori:
        display_image(image, caption="Original Image", key="original_image_salt_pepper")
    with result:
        display_image(result_img, caption="Result Image", key="result_image_salt_pepper")
        
def display_remove_noise(image):
    st.subheader("Remove Noise")
    
    # Apply salt and pepper noise
    result_img = remove_noise(image)
    
    ori, result = st.columns(2)
    with ori:
        display_image(image, caption="Original Image", key="original_image_remove_noise")
    with result:
        display_image(result_img, caption="Result Image", key="result_image_remove_noise")
    
    return result_img
        
def display_sharpen_image(image):
    st.subheader("Sharpen Image")
    
    # Apply sharpen image
    result_img = sharpen_image(image)
    
    ori, result = st.columns(2)
    with ori:
        display_image(image, caption="Original Image", key="original_image_sharpen")
    with result:
        display_image(result_img, caption="Result Image", key="result_image_sharpen")
    
    return result_img
        
        
        
        
        
        
        