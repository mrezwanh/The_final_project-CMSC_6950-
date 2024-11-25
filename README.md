# The_final_project-CMSC_6950
# Data Analysis of Historical Weather Data
**Project Overview:**

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
- Python 3.8 or later
- Required libraries: `numpy`, `pandas`, `matplotlib`

Install the dependencies:
```bash
pip install -r requirements.txt
