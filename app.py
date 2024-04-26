from main import *
from weather_api import fetch_weather_data
from flask import send_from_directory
import os

app = Flask(__name__)

@app.route('/mean_temp/<string:date>', methods=['GET'])
def get_mean_temp(date):
    """
    Retrieve the mean temperature for the last five years for a specific date.

    Args:
        date (str): The date in 'MM-DD' format.

    Returns:
         dict: Mean temperature data for each year.
    """
    latitude = 32.0002
    longitude = -80.8457
    years = [2019, 2020, 2021, 2022, 2023]

    temp_data = {}
    for year in years:
        data = fetch_weather_data(year, latitude, longitude, date)
        if data:
            temp_data[year] = data.get('daily', {}).get('temperature_2m_mean')

    return jsonify(temp_data)


@app.route('/wind_speed/<string:date>', methods=['GET'])
def get_wind_speed(date):
    """
    Retrieve the maximum wind speed for the last five years for a specific date.

    Args:
        date (str): The date in 'MM-DD' format.

    Returns:
        dict: Maximum wind speed data for each year.
    """
    latitude = 32.0002
    longitude = -80.8457
    years = [2019, 2020, 2021, 2022, 2023]

    wind_speed_data = {}
    for year in years:
        data = fetch_weather_data(year, latitude, longitude, date)
        if data:
            wind_speed_data[year] = data.get('daily', {}).get('wind_speed_10m_max')

    return jsonify(wind_speed_data)


@app.route('/sum_precip/<string:date>', methods=['GET'])
def get_sum_precip(date):
    """
    Retrieve the precipitation sum for the last five years for a specific date.

    Args:
        date (str): The date in 'MM-DD' format.

    Returns:
        dict: Precipitation sum data for each year.
    """
    latitude = 32.0002
    longitude = -80.8457
    years = [2019, 2020, 2021, 2022, 2023]

    sum_precip_data = {}
    for year in years:
        data = fetch_weather_data(year, latitude, longitude, date)
        if data:
            sum_precip_data[year] = data.get('daily', {}).get('precipitation_sum')

    return jsonify(sum_precip_data)


@app.route('/min_temp/<string:date>', methods=['GET'])
def get_min_temp(date):
    """
    Retrieve the minimum temperature for the last five years for a specific date.

    Args:
        date (str): The date in 'MM-DD' format.

    Returns:
        dict: Minimum temperature data for each year.
    """
    latitude = 32.0002
    longitude = -80.8457
    years = [2019, 2020, 2021, 2022, 2023]

    min_temp_data = {}
    for year in years:
        data = fetch_weather_data(year, latitude, longitude, date)
        if data:
            min_temp_data[year] = data.get('daily', {}).get('temperature_2m_min')

    return jsonify(min_temp_data)


@app.route('/max_temp/<string:date>', methods=['GET'])
def get_max_temp(date):
    """
    Retrieve the maximum temperature for the last five years for a specific date.

    Args:
        date (str): The date in 'MM-DD' format.

    Returns:
        dict: Maximum temperature data for each year.
    """
    latitude = 32.0002
    longitude = -80.8457
    years = [2019, 2020, 2021, 2022, 2023]

    max_temp_data = {}
    for year in years:
        data = fetch_weather_data(year, latitude, longitude, date)
        if data:
            max_temp_data[year] = data.get('daily', {}).get('temperature_2m_max')

    return jsonify(max_temp_data)


@app.route('/min_wind/<string:date>', methods=['GET'])
def get_min_wind(date):
    """
    Retrieve the minimum wind speed for the last five years for a specific date.

    Args:
        date (str): The date in 'MM-DD' format.

    Returns:
        dict: Minimum wind speed data for each year.
    """
    latitude = 32.0002
    longitude = -80.8457
    years = [2019, 2020, 2021, 2022, 2023]

    min_wind_data = {}
    for year in years:
        data = fetch_weather_data(year, latitude, longitude, date)
        if data:
            min_wind_list = data.get('daily', {}).get('wind_speed_10m_min')
            min_wind_data[year] = min_wind_list[0] if min_wind_list else None

    return jsonify(min_wind_data)


@app.route('/avg_wind/<string:date>', methods=['GET'])
def get_avg_wind(date):
    """
    Retrieve the average wind speed for the last five years for a specific date.

    Args:
        date (str): The date in 'MM-DD' format.

    Returns:
        dict: Average wind speed data for each year.
    """
    latitude = 32.0002
    longitude = -80.8457
    years = [2019, 2020, 2021, 2022, 2023]

    avg_wind_data = {}
    for year in years:
        data = fetch_weather_data(year, latitude, longitude, date)
        if data:
            avg_wind_list = data.get('daily', {}).get('wind_speed_10m_mean')
            avg_wind_data[year] = avg_wind_list[0] if avg_wind_list else None

    return jsonify(avg_wind_data)


@app.route('/max_precip/<string:date>', methods=['GET'])
def get_max_precip(date):
    """
    Retrieve the maximum precipitation for the last five years for a specific date.

    Args:
        date (str): The date in 'MM-DD' format.

    Returns:
        dict: Maximum precipitation data for each year.
    """
    latitude = 32.0002
    longitude = -80.8457
    years = [2019, 2020, 2021, 2022, 2023]

    max_precip_data = {}
    for year in years:
        data = fetch_weather_data(year, latitude, longitude, date)
        if data and 'hourly' in data:
            max_precip_list = data.get('hourly', {}).get('rain')
            max_precip_data[year] = max(max_precip_list) if max_precip_list else None

    return jsonify(max_precip_data)


@app.route('/min_precip/<string:date>', methods=['GET'])
def get_min_precip(date):
    """
    Retrieve the minimum precipitation for the last five years for a specific date.

    Args:
        date (str): The date in 'MM-DD' format.

    Returns:
        dict: Minimum precipitation data for each year.
    """
    latitude = 32.0002
    longitude = -80.8457
    years = [2019, 2020, 2021, 2022, 2023]

    min_precip_data = {}
    for year in years:
        data = fetch_weather_data(year, latitude, longitude, date)
        if data and 'hourly' in data:
            min_precip_list = data.get('hourly', {}).get('rain')
            min_precip_data[year] = min(min_precip_list) if min_precip_list else None

    return jsonify(min_precip_data)


@app.route('/')
def index():
    """
    Define the index endpoint for the StormSense API.

    Returns:
        str: Results of the main.py script.
    """
    main_output = main()
    return main_output


@app.route('/favicon.ico')
def favicon():
    """
    Define the favicon endpoint for the StormSense API.

    Returns:
        file: Favicon image file.
    """
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == '__main__':
    app.run(debug=True)
    
