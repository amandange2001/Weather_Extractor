import requests
from datetime import datetime
import sqlite3
import matplotlib.pyplot as plt
import pandas as pd

# API key and location setup
API_KEY = '9007cf4ca14b408e9b1142448230712'
LOCATION = 'Mumbai'

# Function to fetch weather data from APIg
def fetch_weather_data():
    url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={LOCATION}"
    response = requests.get(url)
    data = response.json()
    weather_data = {
        'temperature': data['current']['temp_c'],  # Corrected key for temperature in Celsius
        'humidity': data['current']['humidity'],   # Corrected key for humidity
        'wind_speed': data['current']['wind_kph'], # Corrected key for wind speed in km/h
        'timestamp': datetime.now().isoformat()    # Store timestamp in ISO format
    }
    return weather_data

# Function to create SQLite database and table
def create_database():
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS weather (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      temperature REAL,
                      humidity REAL,
                      wind_speed REAL,
                      timestamp TEXT)''')
    conn.commit()
    conn.close()

# Function to store weather data into the database
def store_weather_data(data):
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO weather (temperature, humidity, wind_speed, timestamp)
                      VALUES (?, ?, ?, ?)''', 
                      (data['temperature'], data['humidity'], data['wind_speed'], data['timestamp']))
    conn.commit()
    conn.close()

# Function to calculate average temperature from the database
def get_average_temperature():
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT AVG(temperature) FROM weather')
    avg_temp = cursor.fetchone()[0]
    conn.close()
    return avg_temp

# Function to visualize data using Matplotlib
def visualize_data():
    conn = sqlite3.connect('weather_data.db')
    df = pd.read_sql_query('SELECT * FROM weather', conn)
    conn.close()

    # Convert timestamp to datetime for plotting
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Plot temperature trends
    plt.plot(df['timestamp'], df['temperature'], label='Temperature')
    plt.xlabel('Time')
    plt.ylabel('Temperature (°C)')
    plt.title('Temperature Trends Over Time')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

# Example usage:
create_database()
weather_data = fetch_weather_data()
store_weather_data(weather_data)
print(f"Average temperature: {get_average_temperature()} °C")
visualize_data()

