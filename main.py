from weather_api import *
from flask import Flask, render_template
from app import app

# C3: Create main.py file


def main():
    """
    Main function to gather weather data for the specified coordinates and dates.

    This function defines the latitude, longitude, date, and years to check for weather data.
    It then creates an instance of the StormSense class with initial values and loops through
    each year to fetch weather data for the specified date. The data is used to calculate
    aggregate values for average temperature, maximum wind speed, and precipitation sum.

    Returns:
        str: Output of the weather data analysis.
    """
    latitude = 32.0002
    longitude = -80.8457
    date_to_check = '05-07'
    years = [2019, 2020, 2021, 2022, 2023]

    weather_instance = StormSense(latitude=latitude, longitude=longitude,
                                  month=5, day=7, year=2019,
                                  avg_temp=0, min_temp=None, max_temp=None,
                                  avg_wind=None, min_wind=None, max_wind=0,
                                  sum_precip=0, min_precip=None, max_precip=None)

    for year in years:
        data = fetch_weather_data(year, latitude, longitude, date_to_check)
        print(f"Data for {year}: {data}")
        if data:
            avg_temp_list = data.get('daily', {}).get('temperature_2m_mean')
            weather_instance.avg_temp += avg_temp_list[0] if avg_temp_list else 0

            max_wind_agg_list = data.get('daily', {}).get('wind_speed_10m_max')
            weather_instance.max_wind = max(weather_instance.max_wind, max_wind_agg_list[0] if max_wind_agg_list else 0)

            sum_precip_list = data.get('daily', {}).get('precipitation_sum')
            weather_instance.sum_precip += sum_precip_list[0] if sum_precip_list else 0

    weather_instance.avg_temp /= len(years)

    with app.app_context():
        return render_template('weather.html',
                               avg_temp=weather_instance.avg_temp,
                               max_wind=weather_instance.max_wind,
                               sum_precip=weather_instance.sum_precip)


if __name__ == "__main__":
    main()
