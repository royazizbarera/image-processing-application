import streamlit as st
import numpy as np

from src.services import convert_to_gray_scale, histogram_equalization, histogram_gray_scale, histogram_rgb, histogram_specification
from src.views.util_view import display_image


def display_histogram_gray_scale(img):
    st.subheader("Histogram of Grayscale Image")
    display_image(histogram_gray_scale(
        img), caption="Histogram of Grayscale Image", key="histogram_gray_scale")


def display_histogram_rgb(img):
    st.subheader("Histogram of RGB Image")
    display_image(histogram_rgb(img), caption="Histogram of RGB Image", key="histogram_rgb")


def display_histogram_equalization(img):
    st.subheader("Histogram Equalization")
    display_image(histogram_equalization(img),
                  caption="Histogram Equalization", key="histogram_equalization")


def display_histogram_specification(img, img2):
    st.subheader("Histogram Specification")
    display_image(histogram_specification(img, img2),
                  caption="Histogram Specification", key="histogram_specification")


def display_statistics(img):
    st.subheader("Statistics")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("Mean: ", np.mean(img))
        st.write("Median: ", np.median(img))
        st.write("Standard Deviation: ", np.std(img))

    with col2:
        st.write("Variance: ", np.var(img))
        st.write("Minimum: ", np.min(img))
        st.write("Maximum: ", np.max(img))

    with col3:
        st.write("Range: ", np.ptp(img))
        st.write("Percentile 25: ", np.percentile(img, 25))
        st.write("Percentile 75: ", np.percentile(img, 75))
        st.write("Interquartile Range: ", np.percentile(
            img, 75) - np.percentile(img, 25))
