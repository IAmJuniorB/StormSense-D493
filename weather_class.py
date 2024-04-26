import sqlite3
from sqlalchemy import create_engine, Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from weather_api import fetch_weather_data

# C4: Create class that creates a table


Base = declarative_base()

class StormSense2(Base):
    """
    StormSense2 class represents a table in the database to store weather data.

    Attributes:
        id (int): The primary key of the table.
        latitude (float): Latitude coordinate of the weather data.
        longitude (float): Longitude coordinate of the weather data.
        month (int): Month of the weather data.
        day (int): Day of the weather data.
        year (int): Year of the weather data.
        avg_temp (float): Average temperature of the weather data.
        min_temp (float): Minimum temperature of the weather data.
        max_temp (float): Maximum temperature of the weather data.
        avg_wind (float): Average wind speed of the weather data.
        min_wind (float): Minimum wind speed of the weather data.
        max_wind (float): Maximum wind speed of the weather data.
        sum_precip (float): Sum of precipitation of the weather data.
        min_precip (float): Minimum precipitation of the weather data.
        max_precip (float): Maximum precipitation of the weather data.
    """
    __tablename__ = "StormSense_Weather2"

    id = Column("ID", Integer, primary_key=True)
    latitude = Column("Latitude", Float)
    longitude = Column("Longitude", Float)
    month = Column("Month", Integer)
    day = Column("Day", Integer)
    year = Column("Year", Integer)
    avg_temp = Column("Average Temperature", Float)
    min_temp = Column("Minimum Temperature", Float)
    max_temp = Column("Maximum Temperature", Float)
    avg_wind = Column("Average Wind Speed", Float)
    min_wind = Column("Minimum Wind Speed", Float)
    max_wind = Column("Maximum Wind Speed", Float)
    sum_precip = Column("Sum Precipitation", Float)
    min_precip = Column("Minimum Precipitation", Float)
    max_precip = Column("Maximum Precipitation", Float)

    def __init__(self, latitude, longitude, month, day, year,
                 avg_temp, min_temp, max_temp, avg_wind, min_wind,
                 max_wind, sum_precip, min_precip, max_precip):
        """
                Initializes a StormSense2 instance with the provided weather data.

                Args:
                    latitude (float): Latitude coordinate.
                    longitude (float): Longitude coordinate.
                    month (int): Month of the weather data.
                    day (int): Day of the weather data.
                    year (int): Year of the weather data.
                    avg_temp (float): Average temperature.
                    min_temp (float): Minimum temperature.
                    max_temp (float): Maximum temperature.
                    avg_wind (float): Average wind speed.
                    min_wind (float): Minimum wind speed.
                    max_wind (float): Maximum wind speed.
                    sum_precip (float): Sum of precipitation.
                    min_precip (float): Minimum precipitation.
                    max_precip (float): Maximum precipitation.
                """
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

engine = create_engine('sqlite:///:memory:', echo=True)


Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

# C5: Populate table created in C4

latitude = 32.0002
longitude = -80.8457
years = [2019, 2020, 2021, 2022, 2023]
date_to_check = "05-07"


def table_populate(session, latitude, longitude, date_to_check):
    """
        Populate the StormSense2 table with weather data for a specific location and date.

        Args:
            session (Session): The SQLAlchemy session object.
            latitude (float): Latitude coordinate of the location.
            longitude (float): Longitude coordinate of the location.
            date_to_check (str): The date to fetch weather data for in 'MM-DD' format.

        Returns:
            None
        """
    for year in years:
        data = fetch_weather_data(year, latitude, longitude, date_to_check)
        if data:
            avg_temp_list = data.get('daily', {}).get('temperature_2m_mean')
            min_temp_list = data.get('daily', {}).get('temperature_2m_min')
            max_temp_list = data.get('daily', {}).get('temperature_2m_max')
            avg_wind_list = data.get('daily', {}).get('wind_speed_10m_mean')
            min_wind_list = data.get('daily', {}).get('wind_speed_10m_min')
            max_wind_list = data.get('daily', {}).get('wind_speed_10m_max')
            sum_precip_list = data.get('daily', {}).get('precipitation_sum')
            min_precip_list = data.get('hourly', {}).get('rain')
            max_precip_list = data.get('hourly', {}).get('rain')

            storm_sense_instance = StormSense2(latitude=latitude, longitude=longitude, month=5, day=7, year=year,
                                                  avg_temp = avg_temp_list[0] if avg_temp_list else 0,
                                                  min_temp = min_temp_list[0] if min_temp_list else 0,
                                                  max_temp = max_temp_list[0] if max_temp_list else 0,
                                                  avg_wind = avg_wind_list[0] if avg_wind_list else 0,
                                                  min_wind = min_wind_list[0] if min_wind_list else 0,
                                                  max_wind = max_wind_list[0] if max_wind_list else 0,
                                                  sum_precip = sum_precip_list[0] if sum_precip_list else 0,
                                                  min_precip = min(min_precip_list) if min_precip_list else 0,
                                                  max_precip = max(max_precip_list) if max_precip_list else 0)

            session.add(storm_sense_instance)
    session.commit()
table_populate(session, latitude, longitude, date_to_check)


# C6: Query the table and retrieve the data stored

results = session.query(StormSense2).all()
for record in results:
    print(record.id, record.latitude, record.longitude, record.month, record.day, record.year,
          record.avg_temp, record. min_temp, record.max_temp,
          record.avg_wind, record.min_wind, record.max_wind,
          record.sum_precip, record.min_precip, record.max_precip)

def print_horizontal_line():
    """
    Prints a horizontal line to separate the output.
    """
    print(
        "+----+------------+--------------+-------+-----+------+-------------------+-------------------+-------------------+--------------------+---------------------+---------------------+-----------------+--------------------+--------------------+")

def print_vertical_keys():
    print(
        "| ID | Latitude   |  Longitude   | Month | Day | Year |  Average Temp (F) |  Minimum Temp (F) |  Maximum Temp (F) | Average Wind (m/s) |  Minimum Wind (m/s) |  Maximum Wind (m/s) | Sum Precip (mm) | Minimum Precip (mm)| Maximum Precip (mm)|")

print_horizontal_line()
print_vertical_keys()
print_horizontal_line()

for record in results:
    print(
        f"| {record.id:<2} | {record.latitude:<10.7f} | {record.longitude:<11.7f} | {record.month:<5} | {record.day:<3} | {record.year:<4} | {record.avg_temp:<17.1f} | {record.min_temp:<17.1f} | {record.max_temp:<17.1f} | {record.avg_wind:<18.1f} | {record.min_wind:<19.1f} | {record.max_wind:<19.1f} | {record.sum_precip:<15.3f} | {record.min_precip:<18.3f} | {record.max_precip:<18.3f} |")

print_horizontal_line()
