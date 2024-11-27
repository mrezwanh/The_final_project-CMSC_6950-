import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import glob

# Use glob to find all matching CSV files
file_pattern = 'en_climate_daily_NL_8403505_*.csv'
files = glob.glob(file_pattern)

if not files:
    print("No files matching the pattern found. Please check the file path or pattern.")
else:
    print(f"Files found: {files}")

# Load and combine all files
dataframes = [pd.read_csv(file) for file in files]
combined_data = pd.concat(dataframes, ignore_index=True)

# Convert Date/Time column to datetime
combined_data['Date/Time'] = pd.to_datetime(combined_data['Date/Time'])

# Add Year and Month columns
combined_data['Year'] = combined_data['Date/Time'].dt.year
combined_data['Month'] = combined_data['Date/Time'].dt.month

# Filter for required columns
required_data = combined_data[['Year', 'Month', 'Max Temp (°C)', 'Min Temp (°C)']]

# Group by Year and Month to find extreme temperatures
monthly_extremes = required_data.groupby(['Year', 'Month']).agg(
    Monthly_Max=('Max Temp (°C)', 'max'),
    Monthly_Min=('Min Temp (°C)', 'min')
).reset_index()

# Save extreme temperatures to a CSV file
monthly_extremes.to_csv('extreme_temperatures.csv', index=False)
print("Extreme temperature data has been saved to 'extreme_temperatures.csv'.")

# Predict 2025 temperatures by averaging monthly extremes over 2020-2024
predicted_2025 = monthly_extremes[monthly_extremes['Year'] < 2025].groupby('Month').agg(
    Predicted_Max=('Monthly_Max', 'mean'),
    Predicted_Min=('Monthly_Min', 'mean')
).reset_index()

# Save predicted 2025 temperatures to another CSV file
predicted_2025.to_csv('predicted_2025_temperatures.csv', index=False)
print("Predicted 2025 temperature data has been saved to 'predicted_2025_temperatures.csv'.")

# Add labels for plotting
predicted_2025['Month_Label'] = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun", 
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]

# Determine grid size for subplots
unique_years = monthly_extremes['Year'].unique()
num_years = len(unique_years) + 1  # Include the 2025 prediction plot
grid_rows = (num_years + 1) // 2  # Two plots per row
grid_cols = 2

fig, axs = plt.subplots(grid_rows, grid_cols, figsize=(14, grid_rows * 6))
axs = axs.flatten()

# Plot yearly data
for i, year in enumerate(unique_years):
    yearly_data = monthly_extremes[monthly_extremes['Year'] == year]
    
    x_labels = [f"{int(month)}" for month in yearly_data['Month']]
    x = np.arange(len(x_labels))
    
    axs[i].bar(x - 0.2, yearly_data['Monthly_Max'], width=0.4, label='Max Temp (°C)', color='red')
    axs[i].bar(x + 0.2, yearly_data['Monthly_Min'], width=0.4, label='Min Temp (°C)', color='blue')
    
    axs[i].set_title(f"Extreme Temperatures for {year}", fontsize=14)
    axs[i].set_ylabel("Temperature (°C)", fontsize=12)
    axs[i].set_xticks(ticks=x)
    axs[i].set_xticklabels(x_labels, fontsize=10)
    axs[i].legend(fontsize=10)
    axs[i].grid(axis='y', linestyle='--', alpha=0.7)

# Plot predicted 2025 data with a different color
x = np.arange(len(predicted_2025['Month_Label']))  # Convert range to array
axs[len(unique_years)].bar(x - 0.2, predicted_2025['Predicted_Max'], width=0.4, color='purple', label='Predicted Max Temp (°C)')
axs[len(unique_years)].bar(x + 0.2, predicted_2025['Predicted_Min'], width=0.4, color='orange', label='Predicted Min Temp (°C)')
axs[len(unique_years)].set_title("Predicted Temperatures for 2025", fontsize=14)
axs[len(unique_years)].set_xticks(x)
axs[len(unique_years)].set_xticklabels(predicted_2025['Month_Label'])
axs[len(unique_years)].set_ylabel("Temperature (°C)", fontsize=12)
axs[len(unique_years)].legend(fontsize=10)
axs[len(unique_years)].grid(axis='y', linestyle='--', alpha=0.7)

# Hide any unused subplots
for j in range(len(unique_years) + 1, len(axs)):
    axs[j].axis('off')

plt.tight_layout()
plt.savefig('CMSC_6950(4).jpg', format='jpg')
plt.show()
