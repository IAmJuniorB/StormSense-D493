# StormSense Weather Data Analysis

## Table of Contents

- [Overview](#overview)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Testing](#testing)
- [HTML Template](#html-template)
- [Dependencies](#dependencies)
- [Contributors](#contributors)
- [License](#license)

## Overview

Welcome to StormSense Weather Data Analysis project! This project utilizes weather data APIs to gather and analyze weather data for specified coordinates and dates. The analysis includes parameters such as mean temperature, maximum wind speed, and precipitation sum over multiple years.

This project consists of several Python files:

- `main.py`: Contains the main function to gather weather data and perform analysis.
- `weather_class.py`: Defines the `StormSense` class and related functions for weather data analysis.
- `weather_api.py`: Provides functions to interact with weather data APIs.
- `app.py`: Sets up a Flask web application to expose endpoints for retrieving weather data.
- `tests.py`: Includes unit tests for the main function, weather class, and API functions.
- `weather.html`: HTML template for displaying weather data analysis results.

## Usage

To run the project:

1. Install the required dependencies using `pip install -r requirements.txt`.
2. Run the Flask application by executing `python app.py`.
3. Access the endpoints to retrieve weather data analysis results.

## Endpoints

The Flask application exposes the following endpoints:

- `/mean_temp/<string:date>`: Retrieves mean temperature for the last five years for a specific date.
- `/wind_speed/<string:date>`: Retrieves maximum wind speed for the last five years for a specific date.
- `/sum_precip/<string:date>`: Retrieves precipitation sum for the last five years for a specific date.
- `/min_temp/<string:date>`: Retrieves minimum temperature for the last five years for a specific date.
- `/max_temp/<string:date>`: Retrieves maximum temperature for the last five years for a specific date.
- `/min_wind/<string:date>`: Retrieves minimum wind speed for the last five years for a specific date.
- `/avg_wind/<string:date>`: Retrieves average wind speed for the last five years for a specific date.
- `/max_precip/<string:date>`: Retrieves maximum precipitation for the last five years for a specific date.
- `/min_precip/<string:date>`: Retrieves minimum precipitation for the last five years for a specific date.
- `/`: Root endpoint returns the results of the main data analysis.

## Testing

Unit tests are provided in `tests.py` to ensure the correctness of the main function, weather class, and API functions. Run the tests using `python tests.py`.

## HTML Template

The `weather.html` file contains an HTML template for displaying weather data analysis results. It utilizes Bootstrap for styling and dynamically injects data using Flask's template engine.

## Dependencies

- Flask: Web framework for building the API endpoints.
- Requests: HTTP library for making requests to weather data APIs.
- SQLAlchemy: SQL toolkit and Object-Relational Mapping (ORM) library for interacting with the database.

## Contributors

- [Joe Bonfanti](https://github.com/IAmJuniorB) - jbonfan@wgu.edu

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to explore and enhance this project further! If you have any questions or suggestions, please reach out to [Your Email]. Happy coding! 🌦️🌬️🌧️
