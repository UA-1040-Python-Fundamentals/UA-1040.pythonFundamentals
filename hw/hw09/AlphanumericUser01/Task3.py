import tkinter as tk
from pyowm import OWM

API_KEY = '6cffb2408fba391912622087b63dc6cf'


def get_weather():
    user_city = entry_field.get()
    owm = OWM(API_KEY)
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(user_city)
    w = observation.weather

    weather_info = {
        'detailed_status': w.detailed_status,
        'wind': w.wind(),
        'humidity': w.humidity,
        'temperature': w.temperature('celsius')['temp'],
        'rain': w.rain,
        'heat_index': w.heat_index,
        'clouds': w.clouds,
    }

    weather_info_str = ""
    for key, value in weather_info.items():
        weather_info_str += f'{key}: {value}\n'

    label.config(text=weather_info_str)


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
                   command=get_weather)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 14), anchor='nw', justify='left')
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()
