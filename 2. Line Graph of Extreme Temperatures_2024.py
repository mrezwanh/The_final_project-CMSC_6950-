import pandas as pd
import matplotlib.pyplot as plt

# Load and combine data from multiple CSV files for 2024
files = [
    'en_climate_daily_NL_8403505_2020_P1D.csv',
    'en_climate_daily_NL_8403505_2021_P1D.csv',
    'en_climate_daily_NL_8403505_2022_P1D.csv',
    'en_climate_daily_NL_8403505_2023_P1D.csv',
    'en_climate_daily_NL_8403505_2024_P1D.csv'
]

# Combine data from multiple files
dataframes = [pd.read_csv(file) for file in files]
combined_data = pd.concat(dataframes, ignore_index=True)

# Ensure proper datetime conversion
combined_data['Date/Time'] = pd.to_datetime(combined_data['Date/Time'])

# Filter data for the year 2024
data_2024 = combined_data[combined_data['Year'] == 2024]

# Extract relevant columns for plotting
data_2024 = data_2024[['Date/Time', 'Max Temp (°C)', 'Min Temp (°C)', 'Mean Temp (°C)']]

# Compute the extreme value
data_2024['Extreme Value (°C)'] = data_2024.apply(
    lambda row: row['Max Temp (°C)'] 
    if abs(row['Max Temp (°C)']) > abs(row['Min Temp (°C)']) 
    else row['Min Temp (°C)'], 
    axis=1
)

# Print the extreme values with dates
print("Extreme Values for 2024:")
print(data_2024[['Date/Time', 'Extreme Value (°C)']])

# Plot the extreme values
plt.figure(figsize=(14, 7))
plt.plot(data_2024['Date/Time'], data_2024['Extreme Value (°C)'], label='Extreme Value (°C)', color='purple', marker='o', linestyle='-', linewidth=2)
plt.title('Extreme Temperature Values for 2024', fontsize=16)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Temperature (°C)', fontsize=14)
plt.grid(True)
plt.legend(fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('CMSC_6950(2).jpg', format='jpg')
plt.show()
