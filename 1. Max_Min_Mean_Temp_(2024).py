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

# Create a grid layout for the plots
fig, axs = plt.subplots(2, 2, figsize=(18, 12))

# Plot Maximum Temperature
axs[0, 0].bar(data_2024['Date/Time'], data_2024['Max Temp (°C)'], color='red', alpha=0.6, label='Max Temp (°C)')
axs[0, 0].plot(data_2024['Date/Time'], data_2024['Max Temp (°C)'], color='red', marker='o', linestyle='-', linewidth=2)
axs[0, 0].set_title('Maximum Temperature (2024)', fontsize=14)
axs[0, 0].set_xlabel('Date', fontsize=12)
axs[0, 0].set_ylabel('Temperature (°C)', fontsize=12)
axs[0, 0].grid(True)
axs[0, 0].tick_params(axis='x', rotation=45)

# Plot Minimum Temperature
axs[0, 1].bar(data_2024['Date/Time'], data_2024['Min Temp (°C)'], color='blue', alpha=0.6, label='Min Temp (°C)')
axs[0, 1].plot(data_2024['Date/Time'], data_2024['Min Temp (°C)'], color='blue', marker='x', linestyle='-', linewidth=2)
axs[0, 1].set_title('Minimum Temperature (2024)', fontsize=14)
axs[0, 1].set_xlabel('Date', fontsize=12)
axs[0, 1].set_ylabel('Temperature (°C)', fontsize=12)
axs[0, 1].grid(True)
axs[0, 1].tick_params(axis='x', rotation=45)

# Plot Mean Temperature
axs[1, 0].bar(data_2024['Date/Time'], data_2024['Mean Temp (°C)'], color='green', alpha=0.6, label='Mean Temp (°C)')
axs[1, 0].plot(data_2024['Date/Time'], data_2024['Mean Temp (°C)'], color='green', marker='s', linestyle='-', linewidth=2)
axs[1, 0].set_title('Mean Temperature (2024)', fontsize=14)
axs[1, 0].set_xlabel('Date', fontsize=12)
axs[1, 0].set_ylabel('Temperature (°C)', fontsize=12)
axs[1, 0].grid(True)
axs[1, 0].tick_params(axis='x', rotation=45)

# Plot Combined Results
axs[1, 1].bar(data_2024['Date/Time'] - pd.Timedelta(days=0.2), data_2024['Max Temp (°C)'], width=0.4, color='red', alpha=0.6, label='Max Temp (°C)')
axs[1, 1].bar(data_2024['Date/Time'], data_2024['Min Temp (°C)'], width=0.4, color='blue', alpha=0.6, label='Min Temp (°C)')
axs[1, 1].bar(data_2024['Date/Time'] + pd.Timedelta(days=0.2), data_2024['Mean Temp (°C)'], width=0.4, color='green', alpha=0.6, label='Mean Temp (°C)')
axs[1, 1].plot(data_2024['Date/Time'], data_2024['Max Temp (°C)'], color='red', marker='o', linestyle='-', linewidth=2, label='Max Temp (°C)')
axs[1, 1].plot(data_2024['Date/Time'], data_2024['Min Temp (°C)'], color='blue', marker='x', linestyle='-', linewidth=2, label='Min Temp (°C)')
axs[1, 1].plot(data_2024['Date/Time'], data_2024['Mean Temp (°C)'], color='green', marker='s', linestyle='-', linewidth=2, label='Mean Temp (°C)')
axs[1, 1].set_title('Combined Temperature Data (2024)', fontsize=14)
axs[1, 1].set_xlabel('Date', fontsize=12)
axs[1, 1].set_ylabel('Temperature (°C)', fontsize=12)
axs[1, 1].grid(True)
axs[1, 1].legend(fontsize=10)
axs[1, 1].tick_params(axis='x', rotation=45)

# Adjust layout
plt.tight_layout()
plt.savefig('CMSC_6950(1).jpg', format='jpg')

# Show the plots
plt.show()
