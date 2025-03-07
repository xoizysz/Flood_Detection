import rasterio
import numpy as np
import matplotlib.pyplot as plt

# Load the GeoTIFF file
tif_file = "sentinel1_flood_detected.tif"

with rasterio.open(tif_file) as src:
    flood_image = src.read(1)  # Read the first band
    transform = src.transform  # Get geo-coordinates

# Normalize the image for display
flood_image[flood_image == 0] = np.nan  # Hide non-water areas
plt.imshow(flood_image, cmap='Blues')
plt.colorbar(label="Water Intensity")
plt.title("Flood Detected Areas (Sentinel-1 SAR)")
plt.show()