import streamlit as st
import rasterio
import numpy as np
import matplotlib.pyplot as plt

st.title("🚀 Flood Detection Using Sentinel-1 SAR 🌊")
st.write("Upload a Sentinel-1 SAR GeoTIFF file to detect floods.")

# File uploader
uploaded_file = st.file_uploader("Upload a GeoTIFF file", type=["tif", "tiff"])

if uploaded_file is not None:
    # Read uploaded GeoTIFF file
    with rasterio.open(uploaded_file) as src:
        flood_image = src.read(1)
    
    # Process & display
    flood_image[flood_image == 0] = np.nan
    fig, ax = plt.subplots()
    ax.imshow(flood_image, cmap='Blues')
    ax.set_title("Flooded Areas Detected")
    st.pyplot(fig)

    st.write("Uploaded file processed successfully!")
else:
    st.write("Upload a file to analyze.")

st.markdown("---")
st.markdown("made with ❤️ by Paramita Debbarma")
