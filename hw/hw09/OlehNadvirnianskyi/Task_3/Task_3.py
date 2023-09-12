import tkinter as tk
from tkinter import font
import requests
import OWM

HEIGHT = 350
WIDTH = 450

root = tk.Tk()
def get_weather():
    city = entry_field.get()
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': OWM.API_KEY, 'q': city, 'units': 'metric'}
    result = requests.get(url, params=params)
    weather = result.json()
    humidity = weather["main"]["humidity"]
    wind_speed = weather["wind"]["speed"]
    pressure = weather["main"]["pressure"]
    label['text'] = f'{str(weather["name"])}: \n {weather["main"]["temp"]}°C temperature, \n{humidity}% humidity, \n{wind_speed} m/s wind speed, \n{pressure} hPa pressure'


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame,
                   text="Get Weather",
                   bg="gray", fg="white",
                   font=('Courier', 8),
                   command=lambda: get_weather())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()
