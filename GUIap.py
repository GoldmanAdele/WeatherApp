from tkinter import *
from configparser import ConfigParser
import requests

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&APPID={}'
api_key = 'ebec046ac5af2678e9a9608c6ac05149'

config_file = 'config.ini'
config = ConfigParser()
config.read(config_file)



def get_weather(city):
    result = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city_text}&units=imperial&APPID={api_key}"
    )

    if result:
        json = result.json()
        city = json['name']
        country = json['sys']['country']
        temp_kelvin = json['main']['temp']
        temp_celsius = temp_kelvin - 273.15
        temp_fahrenheit = (temp_kelvin - 273.15)*9/5 + 32
        weather = json['weather'][0]['main']
        final = (city,country,temp_celsius,temp_fahrenheit,weather)
        return final
    else:
        return None


print(get_weather('London'))

app = Tk()
app.title("Weather App")
app.geometry('700x350')

city_text = StringVar()
city_entry = Entry(app,textvariable=city_text)
city_entry.pack()


def search():
    pass


search_btn = Button(app,text='Search Weather',width=12,command=search)
search_btn.pack()

location_lbl = Label(app,text='Location',font=('bold',20))
location_lbl.pack()

image = Label(app,bitmap='')
image.pack()

temp_lbl = Label(app,text='temperature')
temp_lbl.pack()

weather_lbl = Label(app, text='weather')
weather_lbl.pack()


app.mainloop()
