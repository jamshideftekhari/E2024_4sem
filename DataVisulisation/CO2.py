import pandas as pd
import matplotlib.pyplot as plt

# Define the path to the CSV file
file_path = "S11GBGE236.csv"

# Read the CSV file with the appropriate delimiter and parse dates
data = pd.read_csv(file_path, delimiter=";", header=0)

# Set column names and clean the data
data.columns = [
    "Sensor", "Name", "Date", "Latitude", "Longitude", "Temperature_C", 
    "Humidity_RH", "CO2_ppm", "VOC_ppb", "Sound_dB", "Min", "Max", 
    "Light_Lux", "Light_Color_K", "Occupied", "Battery_mV", "Coverage_dB"
]

# Convert 'Date' column to datetime format and 'CO2_ppm' to numeric
data["Date"] = pd.to_datetime(data["Date"], errors='coerce')
data["CO2_ppm"] = pd.to_numeric(data["CO2_ppm"], errors='coerce')

# Plotting CO2 concentration over time
plt.figure(figsize=(12, 6))
plt.plot(data['Date'], data['CO2_ppm'], color='green', linestyle='-', linewidth=1)

# Adding labels and title
plt.title('CO₂ Concentration Over Time')
plt.xlabel('Date')
plt.ylabel('CO₂ Concentration (ppm)')
plt.grid(True)
plt.tight_layout()

# Display the plot
plt.show()
