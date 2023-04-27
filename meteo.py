# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 10:51:50 2023

@author: kevin
"""

import requests
import os

def get_weather():
    api_key = os.environ['API_KEY']
    lat = os.environ['LATITUDE']
    lon = os.environ['LONGITUDE']

    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code != 200:
        return response.status_code

    weather = response.json()

    return weather