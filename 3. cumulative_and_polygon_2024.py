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

# List of years in the data
years = combined_data['Year'].unique()

# Iterate through each year and generate graphs
for year in years:
    # Filter data for the current year
    year_data = combined_data[combined_data['Year'] == year]
    temperatures = year_data['Mean Temp (°C)']

    # Calculate histogram data (frequency counts and bin edges)
    counts, bin_edges = np.histogram(temperatures, bins=20)

    # Plot cumulative histogram
    plt.figure(figsize=(14, 7))
    plt.hist(temperatures, bins=20, rwidth=0.8, color='green', alpha=0.7, cumulative=True, label=f'Cumulative Histogram for {year}')
    
    # Calculate the midpoints of the bins for the frequency polygon
    bin_centers = 0.5 * (bin_edges[1:] + bin_edges[:-1])
    
    # Plot frequency polygon
    plt.plot(bin_centers, counts, label=f'Frequency Polygon for {year}', color='blue', marker='o', linestyle='-', linewidth=2)
    
    # Labels and title
    plt.title(f'Cumulative Histogram and Frequency Polygon for {year}', fontsize=16)
    plt.xlabel('Temperature (°C)', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.legend(fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
