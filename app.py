import random
from flask import Flask, render_template
import requests
import os


app = Flask(__name__)
api_key = os.environ.get("API_KEY", "")

@app.route('/')
def hello():
    return 'Hello World'

@app.route('/<string:city>/weather')
def get_weather(city):
    if api_key == "":
        return "No API key"

    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}",
    )
    weather = weather_data.json()
    if weather:
        weather = weather_data.json()['weather'][0]['main']
        temp = round(weather_data.json()['main']['temp'])
        city = weather_data.json()['name']
        country = weather_data.json()['sys']['country']
        return {"city": city, "country": country, "weather": weather, "temp": temp}
    else:
        return "Error", f"Cannot find city {city} "


@app.route('/random/weather')
def search():
    if api_key == "":
        return "No API key"
    cities= ["London", "Lagos", "Tokyo"]
    city = cities[int(random.random() * len(cities))]
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}"
    )
    weather = weather_data.json()
    if weather:
        weather = weather_data.json()['weather'][0]['main']
        temp = round(weather_data.json()['main']['temp'])
        city = weather_data.json()['name']
        country = weather_data.json()['sys']['country']
        return {"city": city, "country": country, "weather": weather, "temp": temp}
    else:
        return "Error", f"Cannot find city {city} "
