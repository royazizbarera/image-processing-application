import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from src.services import get_rgb_array_from_image_data
from src.views.util_view import display_image


# Function to display RGB array and heatmap
def display_rgb(img, title=""):
    st.subheader(f'RGB Array Display {title}')
    
    try:
        # Display the uploaded image
        display_image(img, caption="Uploaded Image", key="rgb_image", width=200)
        # Get RGB array from the image
        rgb_array = get_rgb_array_from_image_data(img)
        
        # Create tabs for "Select members" and "Compare selected"
        selected_tab = st.radio("Select a tab", ["Select members", "Compare selected"])

        # Display RGB array as a table in "Select members" tab
        if selected_tab == "Select members":
            display_rgb_array(rgb_array)
        
        # Only process the heatmap when the "Compare selected" tab is active
        elif selected_tab == "Compare selected":
            st.write("Processing heatmap...")  # Indicate that processing is happening
            htmap1, htmap2, htmap3 = st.columns(3)
            with htmap1:
                display_rgb_heatmap("Red", rgb_array["R"])
            with htmap2:
                display_rgb_heatmap("Green", rgb_array["G"])
            with htmap3:
                display_rgb_heatmap("Blue", rgb_array["B"])
                

    except Exception as e:
        st.error(f"Error processing the image: {e}")
# Display RGB array as a table


def display_rgb_array(rgb_array):
    n_rows_to_display = min(len(rgb_array["R"]), 10)
    st.write("Displaying the first 10 rows of the RGB array:")

    df = pd.DataFrame({
        "Red": rgb_array["R"][:n_rows_to_display],
        "Green": rgb_array["G"][:n_rows_to_display],
        "Blue": rgb_array["B"][:n_rows_to_display]
    })
    st.dataframe(df)

# Display RGB heatmap


def display_rgb_heatmap(channel_name, channel_data):
    plt.figure(figsize=(8, 6))
    sns.heatmap(channel_data, cmap="coolwarm", cbar=True)
    plt.title(f"Heatmap of {channel_name} Channel")
    st.pyplot(plt)
