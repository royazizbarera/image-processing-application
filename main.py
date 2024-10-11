# main.py
from src.constants import UPLOAD_FOLDER
from src.services import load_image_to_numpy, save_image
from src.views.rgb_array_view import display_rgb
from src.views.operation_view import display_arithmetic_operation, display_logical_operation
from src.views.grayscale_view import display_grayscale_image
from src.views.histogram_view import display_histogram_equalization, display_histogram_gray_scale, display_histogram_rgb, display_histogram_specification, display_statistics
from src.views.convolution_view import display_apply_convolution, display_apply_salt_and_pepper_noise, display_filter, display_fourier_transform, display_reduce_periodic_noise, display_sharpen_image, display_zero_padding, display_remove_noise

import streamlit as st
import os

from src.views.util_view import display_image

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


st.set_page_config(page_title="Image Processing", layout="wide")


with st.sidebar:
    st.title("Select features to display")

    # TODO (DONE): Show RGB Array , Operations, Grayscale
    show_rgb_array = st.checkbox("Display RGB Array")
    show_arithmetic_operation = st.checkbox("Perform Arithmetic Operation")
    show_logical_operation = st.checkbox("Perform Logical Operation")
    show_grayscale = st.checkbox("Convert to Grayscale")

    # TODO (DONE): Show Statistics and Histogram
    show_statistics = st.checkbox("Display Statistics")
    show_histogram_gray_scale = st.checkbox(
        "Display Histogram Grayscale Image")
    show_histogram_rgb = st.checkbox("Display Histogram RGB Image")
    show_histogram_equalization = st.checkbox(
        "Display Histogram Equalization")
    show_histogram_specification = st.checkbox(
        "Display Histogram Specification")

    # TODO (DONE): Show convolution
    show_convolution = st.checkbox("Perform Convolution")
    show_zero_padding = st.checkbox("Perform Zero Padding")
    show_filter = st.checkbox("Perform Filter")
    show_fourier_transform = st.checkbox("Perform Fourier Transform")
    show_reduce_periodic_noise = st.checkbox("Reduce Periodic Noise")
    show_apply_salt_and_pepper_noise = st.checkbox(
        "Apply Salt and Pepper Noise")
    show_remove_noise = st.checkbox("Remove Noise")
    show_sharpen_image = st.checkbox("Sharpen Image")


test_edit_image_result = None
st.write("Edit mode is off")
# Main function
# File uploader for image upload
st.subheader("Upload an original image")
image_file = st.file_uploader(
    "Upload an image", type=["jpg", "png", "jpeg"])

# If a new image is uploaded, save it and update session state
if image_file is not None:
    # Save the new image
    image_file_path = save_image(image_file, UPLOAD_FOLDER)
    st.success(f"Image successfully saved: {image_file_path}")

    # Load image as NumPy array
    img_file = load_image_to_numpy(image_file)

    # Store the image and path in session state
    st.session_state['uploaded_image'] = img_file
    st.session_state['uploaded_image_path'] = image_file_path
    st.session_state['new_image_uploaded'] = True
else:
    # Check if image already exists in session state
    if 'uploaded_image' in st.session_state:
        img_file = st.session_state['uploaded_image']
        st.session_state['new_image_uploaded'] = False
    else:
        st.warning("Please upload an image first.")

# Display the image only if there is a new upload or existing image
if 'uploaded_image' in st.session_state:
    if st.session_state['new_image_uploaded']:
        # if image with full screen width is full, if not set width to 300

        # column
        display_image(
            st.session_state['uploaded_image'], caption="Uploaded Image", width=300, key=1)

        if test_edit_image_result:
            display_image(
                st.session_state['test_edit_image_result'], caption="test_edit_image_result", width=300, key=1)

    # Display features based on user selections
    if show_rgb_array:
        st.divider()
        display_rgb(img_file)

    if show_arithmetic_operation:
        st.divider()
        test_edit_image_result = display_arithmetic_operation(img_file)
        st.session_state['test_edit_image_result'] = test_edit_image_result

    if show_logical_operation:
        st.divider()
        image_file2 = st.file_uploader(
            "Upload an image 2", type=["jpg", "png", "jpeg"])
        if image_file2 is not None:
            img_file2 = load_image_to_numpy(image_file2)
            if img_file2 is not None:
                display_logical_operation(
                    image1=img_file, image2=img_file2)
        else:
            st.warning("Please upload image 2 for logical operation.")

    if show_grayscale:
        st.divider()
        display_grayscale_image(img_file)

    if show_statistics:
        st.divider()
        display_statistics(img_file)

    if show_histogram_gray_scale:
        st.divider()
        display_histogram_gray_scale(img_file)

    if show_histogram_rgb:
        st.divider()
        display_histogram_rgb(img_file)

    if show_histogram_equalization:
        st.divider()
        display_histogram_equalization(img_file)

    if show_histogram_specification:
        ref_image = st.file_uploader(
            "Upload an image reference", type=["jpg", "png", "jpeg"])
        if ref_image is not None:
            img_file2 = load_image_to_numpy(ref_image)
            if img_file2 is not None:
                st.divider()
                display_histogram_specification(img_file, img_file2)
        else:
            st.warning(
                "Please upload image reference for histogram specification.")

    if show_convolution:
        st.divider()
        display_apply_convolution(img_file)

    if show_zero_padding:
        st.divider()
        display_zero_padding(img_file)

    if show_filter:
        st.divider()
        display_filter(img_file)

    if show_fourier_transform:
        st.divider()
        display_fourier_transform(img_file)

    if show_reduce_periodic_noise:
        st.divider()
        display_reduce_periodic_noise(img_file)

    if show_apply_salt_and_pepper_noise:
        st.divider()
        display_apply_salt_and_pepper_noise(img_file)

    if show_remove_noise:
        st.divider()
        display_remove_noise(img_file)

    if show_sharpen_image:
        st.divider()
        display_sharpen_image(img_file)

# Run Streamlit app
if __name__ == "__main__":
    pass
