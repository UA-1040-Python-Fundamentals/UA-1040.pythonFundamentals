from pyowm import OWM

API_KEY = 'ef2206ff5da67de63306d0b143e20872'
# ---------- FREE API KEY examples ---------------------
def get_weather(city):
    try:
        owm = OWM(API_KEY)
        mgr = owm.weather_manager()

        observation = mgr.weather_at_place(city)
        w = observation.weather

        responce = f'City: {city}\nConditions: {w.detailed_status }\n'
        responce += f'''Temperature is {round(w.temperature('celsius')['temp'], 2)} C\n'''
        responce += f'''Wind speed is {w.wind()['speed']} km/hours\n'''
        responce += f'Humidity of the air is {w.humidity}%'
        return  responce

    except:
        return 'Oops! There was a problem\nretrieving that information.'




