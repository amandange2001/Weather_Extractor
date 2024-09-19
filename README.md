# Weather Data Aggregator and Analyzer

This project is a simple weather data aggregator and analyzer, built using Python. It fetches real-time weather data from the WeatherAPI, stores the data in a local SQLite database, and provides a visualization of the weather trends over time using Matplotlib and Pandas.

## Features
- Fetches real-time weather data such as temperature, humidity, and wind speed.
- Stores the weather data in an SQLite database.
- Calculates the average temperature over time.
- Visualizes temperature trends using Matplotlib.

## Prerequisites

Before running this project, make sure you have the following installed:

- Python 3.x
- `requests` library for making API calls.
- `sqlite3` for database handling.
- `matplotlib` for data visualization.
- `pandas` for data manipulation.

You can install the required libraries using the following command:
```bash
pip install requests matplotlib pandas
```


## Setup

1. Clone the repository
git clone https://github.com/amandange2001/Weather_Extractor.git


2. Obtain an API Key
Sign up at  `WeatherAPI` to get your API key.

3. Modify the API Key
Replace the API_KEY variable in weather.py with your actual API key:
```bash
API_KEY = 'your_api_key_here'
```
4. Run the Script
The script will fetch the current weather data for a specified location, store it in the SQLite database, and then display the average temperature along with a graph of the temperature trends.
```bash
python weather.py
```
## Files
- weather.py: Main script to fetch, store, and visualize weather data.
- weather_data.db: SQLite database file that stores the weather data.
- README.md: Documentation for the project.
