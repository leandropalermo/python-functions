import datetime as dt
import os

import requests

# api_key = os.environ.get("API_KEY_FROM_ENV")
api_key ='209a67a956f8f3327e6785db2e880931'
api_url_five_days_forecast = 'https://api.openweathermap.org/data/2.5/forecast'

PG_LAT = -23.998890
PG_LNG = -46.413540

five_days_forecast_dict = {
    "lat": PG_LAT,
    "lon": PG_LNG,
    "appid": api_key,
    "cnt": 4
}

schedule_time = [3, 6, 9, 12, 15, 18, 21]


def forecast_five_days():
    response = requests.get(url=api_url_five_days_forecast, params=five_days_forecast_dict)
    response.raise_for_status()

    will_rain = False
    json_response = response.json()
    weather_list_response = json_response['list']
    for weather_list in weather_list_response:
        weather = weather_list['weather'][0]
        condition_code = weather['id']
        if condition_code < 700:
            will_rain = True

    if will_rain:
        print('Bring an umbrella.')


forecast_five_days()

