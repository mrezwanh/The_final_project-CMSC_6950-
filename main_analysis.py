import glob
import pandas as pd
import matplotlib.pyplot as plt

# Load and combine all CSV files
file_pattern = 'en_climate_daily_NL_8403505_*.csv'
dataframes = [pd.read_csv(filename) for filename in glob.glob(file_pattern)]
combined_data = pd.concat(dataframes, ignore_index=True)

# Convert 'Date/Time' to datetime
combined_data['Date/Time'] = pd.to_datetime(combined_data['Date/Time'])

# Add Year and Month columns for easier filtering
combined_data['Year'] = combined_data['Date/Time'].dt.year
combined_data['Month'] = combined_data['Date/Time'].dt.month

# List of years in the data
years = combined_data['Year'].unique()

# Initialize dictionary to store extremes
extreme_points = {}

# Iterate through each year and generate graphs
for year in years:
    # Filter data for the current year
    year_data = combined_data[combined_data['Year'] == year]
    temperatures = year_data['Mean Temp (°C)']
    days = year_data['Date/Time']
    
    # Find extreme points
    max_temp = temperatures.max()
    min_temp = temperatures.min()
    extreme_points[year] = {'Max Temp': max_temp, 'Min Temp': min_temp}
    
    # Plot Line and Bar Chart for the full year
    fig, ax1 = plt.subplots(figsize=(14, 7))

    ax1.plot(days, temperatures, label='Line (Mean Temp)', color='blue', marker='o', markersize=2, linewidth=1)
    ax1.set_xlabel('Date', fontsize=14)
    ax1.set_ylabel('Temperature (°C)', fontsize=14, color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')
    ax1.set_title(f'Temperature Trends for {year}', fontsize=16)
    ax1.grid(linestyle='--', alpha=0.6)

    ax2 = ax1.twinx()
    ax2.bar(days, temperatures, alpha=0.3, color='blue', label='Bar (Mean Temp)')
    ax2.set_ylabel('Temperature (°C)', fontsize=14, color='blue')
    ax2.tick_params(axis='y', labelcolor='blue')

    # Add legend
    fig.legend(loc='upper left', fontsize=12)
    plt.tight_layout()
    plt.show()

    # Plot Histogram for the full year
    plt.figure(figsize=(12, 6))
    plt.hist(temperatures, bins=20, rwidth=0.8, color='blue', alpha=0.7, label=f'Histogram for {year}')
    plt.title(f'Temperature Distribution for {year}', fontsize=16)
    plt.xlabel('Temperature (°C)', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.legend(fontsize=12)
    plt.tight_layout()
    plt.show()

# Print Extreme Points for All Years
print("\nExtreme Points for Each Year:")
for year, extremes in extreme_points.items():
    print(f"{year}: Max Temp = {extremes['Max Temp']}°C, Min Temp = {extremes['Min Temp']}°C")
