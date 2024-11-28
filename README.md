# The_final_project-CMSC_6950
# Data Analysis of Historical Weather Data
## **Project Overview:**

This project analyzes historical weather data to explore trends, identify extreme values, and generate insights using Python. The dataset includes daily weather records (maximum, minimum, and mean temperatures) from 2020 to 2024.

The analysis includes:
- **Visualizations**: Line graphs, bar charts, histograms, and frequency polygons.
- **Extreme Value Analysis**: Identification of unusual weather events.
- **Trend Analysis**: Insights into long-term patterns.

---

## **Dataset**
### **Source**
The data was obtained from [Environment and Climate Change Canada](https://climate.weather.gc.ca/historical_data/search_historic_data_e.html).

### **Description**
- **Format**: CSV files
- **Columns**:
  - `Date/Time`: Daily timestamps
  - `Max Temp (°C)`: Maximum temperature
  - `Min Temp (°C)`: Minimum temperature
  - `Mean Temp (°C)`: Average daily temperature

### **Files**
The dataset includes:
- `en_climate_daily_NL_8403505_2020_P1D.csv`
- `en_climate_daily_NL_8403505_2021_P1D.csv`
- `en_climate_daily_NL_8403505_2022_P1D.csv`
- `en_climate_daily_NL_8403505_2023_P1D.csv`
- `en_climate_daily_NL_8403505_2024_P1D.csv`

---

## **Project Features**
1. **Data Cleaning**:
   - Combined multiple years of data into a single dataset.
   - Filtered for valid temperature entries.

2. **Visualizations**:
   - **Line Graphs**: Show yearly trends in maximum, minimum, and mean temperatures.
   - **Bar Graphs**: Compare daily averages across years.
   - **Histograms**: Analyze the distribution of temperature data.
   - **Cumulative Histograms & Frequency Polygons**: Display cumulative trends.

3. **Extreme Value Analysis**:
   - Identify extreme events based on statistical thresholds.
   - Compare data points exceeding historical means.

4. **Prediction**:
   - Forecast November 2024 mean temperature using weighted averages of prior years (2020–2023).

---

## **How to Reproduce**
### **Prerequisites**
- Python 3.10 or later
- Required libraries: `numpy`, `pandas`, `matplotlib`, `glob`

- To reproduce the results, follow these steps
### 1. Clone the Repository
### 2. Install Dependencies
Make sure you have Python installed (preferably version 3.8 or higher). Install the required Python packages
*use `pip`
### 3. Prepare the Data
Ensure you have the required climate data files in CSV format.
The dataset includes:
- `en_climate_daily_NL_8403505_2020_P1D.csv`
- `en_climate_daily_NL_8403505_2021_P1D.csv`
- `en_climate_daily_NL_8403505_2022_P1D.csv`
- `en_climate_daily_NL_8403505_2023_P1D.csv`
- `en_climate_daily_NL_8403505_2024_P1D.csv`
### 4. Run the Script
Run the Python script to generate the plots and compute extreme temperature values:

* `0.0 main_analysis.py` for finding Line and Bar Graph of Mean Temperatures and frequency distribution from 2020 to 2024.
* `1. Max_Min_Mean_Temp_(2024).py` for finding Combined Temperature Data (2024).
* `2. Line Graph of Extreme Temperatures_2024.py` fir finding extreme temperature for 2024.
* `3. cumulative_and_polygon_2024.py` for illustrate the cumulative frequency of temperatures and The Frequency Polygon line with markers to represent the frequency distribution of temperatures.
* `4. Extreme Temperatures_and_Predicted Temperatures.py` for finding Monthly Maximum and Minimum Temperatures Across Years (2020–2024) and Predicted Temperatures for 2025 (in `csv and jpg`).
*  `5. Monthly Mean Temperatures (Actual vs Predicted for 2025).py`  shows The line graph of the monthly mean temperatures for several years, including a predicted trend for 2025.
*  `6. Predicted_area_2025` represent Predicted Range (Maximum and Minimum) of Temperatures for 2025.
### 5. View the Outputs
The program generates the following outputs:
 * Represent several types of plot for fonding extreme value and predected temperatures and distributions.
 * A combined CSV file named `combined_data.csv` contain all data, `4.1 extreme_temperatures.csv` contain extreme trmperatures value from 2020 to 2024 and also `4.2 predicted_2025_temperatures.csv` contain predicted data. 


