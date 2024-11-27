import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Combine data from multiple files
files = [
    'en_climate_daily_NL_8403505_2020_P1D.csv',
    'en_climate_daily_NL_8403505_2021_P1D.csv',
    'en_climate_daily_NL_8403505_2022_P1D.csv',
    'en_climate_daily_NL_8403505_2023_P1D.csv',
    'en_climate_daily_NL_8403505_2024_P1D.csv'
]

# Load and combine all files
dataframes = [pd.read_csv(file) for file in files]
combined_data = pd.concat(dataframes, ignore_index=True)

# Convert Date/Time column to datetime
combined_data['Date/Time'] = pd.to_datetime(combined_data['Date/Time'])

# Add Year and Month columns
combined_data['Year'] = combined_data['Date/Time'].dt.year
combined_data['Month'] = combined_data['Date/Time'].dt.month

# Filter for required columns
required_data = combined_data[['Year', 'Month', 'Mean Temp (°C)']]

# Group by Year and Month to find mean temperature
monthly_means = required_data.groupby(['Year', 'Month']).agg(
    Monthly_Mean=('Mean Temp (°C)', 'mean')
).reset_index()

# Predict 2025 temperatures by averaging previous years' data
predicted_2025 = monthly_means[monthly_means['Year'] != 2025].groupby('Month').agg(
    Predicted_Mean=('Monthly_Mean', 'mean')
).reset_index()
predicted_2025['Year'] = 2025

# Combine predicted data with historical data
all_data_with_prediction = pd.concat([monthly_means, predicted_2025], ignore_index=True)

# Plotting predicted vs actual data
plt.figure(figsize=(12, 6))

# Separate actual and predicted data
actual_data = monthly_means[monthly_means['Year'] != 2025]
predicted_data = predicted_2025

# Plot actual data
for year in actual_data['Year'].unique():
    year_data = actual_data[actual_data['Year'] == year]
    plt.plot(
        year_data['Month'], 
        year_data['Monthly_Mean'], 
        label=f'Actual {year}', 
        marker='o'
    )

# Plot predicted data for 2025
plt.plot(
    predicted_data['Month'], 
    predicted_data['Predicted_Mean'], 
    label='Predicted 2025', 
    marker='x', 
    color='black', 
    linewidth=2
)

# Add labels, title, and legend
plt.title("Monthly Mean Temperatures (Actual vs Predicted for 2025)", fontsize=16)
plt.xlabel("Month", fontsize=14)
plt.ylabel("Mean Temperature (°C)", fontsize=14)
plt.xticks(ticks=np.arange(1, 13), labels=[
    "Jan", "Feb", "Mar", "Apr", "May", "Jun", 
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
])
plt.legend(fontsize=12)
plt.grid(linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('CMSC_6950(3).jpg', format='jpg')

# Show plot
plt.show()
