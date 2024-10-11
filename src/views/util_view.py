

import numpy as np
import streamlit as st


def display_image(image, caption="Image Uploaded", width=200, fullscreen=False, key=None):
    # create random key if not provided
    if key is None:
        key = np.random.randint(0, 1e6)
    fullscreen_local = st.toggle("Full screen image", fullscreen, key=key)
    if fullscreen_local:
        st.image(image, caption=caption, use_column_width=True)
    else:
        st.image(image, caption=caption, width=width)
