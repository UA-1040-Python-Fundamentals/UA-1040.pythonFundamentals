import tkinter as tk
from tkinter import font
from pyowm import OWM

API_KEY = 'ef2206ff5da67de63306d0b143e20872'
owm = OWM(API_KEY)
mgr = owm.weather_manager()

HEIGHT = 350
WIDTH = 450

root = tk.Tk()

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

def get_weather():
    try:
        city_name = entry_field.get()
        observation = mgr.weather_at_place(city_name)
        w = observation.weather

        weather_info = f"Status: {w.detailed_status}\nWind Speed: {w.wind()['speed']} m/s\nHumidity: {w.humidity}%\nTemperature: {w.temperature('celsius')['temp']}°C\nClouds: {w.clouds}%"
        label['text'] = weather_info
    except:
        label.config(text="Error getting weather.")

root.mainloop()