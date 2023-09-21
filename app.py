from tkinter import *
from tkinter import messagebox

import requests

app = Tk()
app.title("Weather App")
app.geometry('700x350')

api_key = 'ebec046ac5af2678e9a9608c6ac05149'
global temp
global weather

user_input = StringVar()
city_entry = Entry(app,textvariable=user_input)
city_entry.pack()

def get_weather(user_input):
    global temp
    global weather
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}"
    )

    if weather_data.json()['cod'] == '404':
        print("No City Found")
    else:
        weather = weather_data.json()['weather'][0]['main']
        temp = round(weather_data.json()['main']['temp'])
        city = weather_data.json()['name']
        country = weather_data.json()['sys']['country']
        final = (city, country, weather, temp)
        return final

def search ():
    user_input = city_entry.get()
    weather = get_weather(user_input)
    if weather:
        location_lbl['text']='{}, {}'.format(weather[0], weather[1])
        temp_lbl['text']= '{}'.format(weather[3])
        weather_lbl['text']= '{}'.format(weather[2])

    else:
        messagebox.showerror("Error", f"Cannot find city {user_input} ")


search_btn = Button(app,text='Search Weather',width=12,command=search)
search_btn.pack()

location_lbl = Label(app,text='Location',font=('bold',20))
location_lbl.pack()

image = Label(app,bitmap='')
image.pack()

temp_lbl = Label(app,text='temp')
temp_lbl.pack()

weather_lbl = Label(app,text='weather')
weather_lbl.pack()



app.mainloop()
