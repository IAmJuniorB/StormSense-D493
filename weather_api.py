from flask import Flask, jsonify, request
import requests
import io
from main import *

#C1: Create class with instance variables

class StormSense:
    def __init__(self, latitude, longitude, month, day, year,
                 avg_temp, min_temp, max_temp, avg_wind, min_wind,
                 max_wind, sum_precip, min_precip, max_precip):
        self.latitude = latitude
        self.longitude = longitude
        self.month = month
        self.day = day
        self.year = year
        self.avg_temp = avg_temp
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.avg_wind = avg_wind
        self.min_wind = min_wind
        self.max_wind = max_wind
        self.sum_precip = sum_precip
        self.min_precip = min_precip
        self.max_precip = max_precip

#C2: Create a method to pull weather variables

def fetch_weather_data(year, latitude, longitude, start_date):
    """
    Fetch weather data from the API for a specific year and location.

    Args:
        year (int): The year for which weather data is to be fetched.
        latitude (float): Latitude coordinate of the location.
        longitude (float): Longitude coordinate of the location.
        start_date (str): The start date in 'MM-DD' format.

     Returns:
       dict: JSON response containing weather data.

     Raises:
       Exception: If the API request fails.
    """
    url = f"https://archive-api.open-meteo.com/v1/archive"

    month, day = start_date.split('-')
    start_date_format = f"{year}-{month}-{day}"
    end_date_format = f"{year}-{month}-{day}"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": start_date_format,
        "end_date": end_date_format,
        "daily": "temperature_2m_mean,precipitation_sum,wind_speed_10m_max,temperature_2m_min,"
                 "temperature_2m_max,wind_speed_10m_min,wind_speed_10m_mean",
        "hourly": "rain",
        "temperature_unit": "fahrenheit",
        "wind_speed_unit": "mph",
        "precipitation_unit": "inch",
        "timezone": "America/New_York",
    }
    responses = requests.get(url, params=params)

    if responses.status_code == 200:
        return responses.json()
    else:
        error_message = f"Failed to fetch data for {year}. Status code: {responses.status_code}"
        error_message += f"\nResponse Content: {responses.content}"
        raise Exception(error_message)
