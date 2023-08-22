from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

# ---------- FREE API KEY examples ---------------------

owm = OWM('key')
mgr = owm.weather_manager()


# Search for current weather in London (Great Britain) and get details
observation = mgr.weather_at_place('Lviv,UA')
w = observation.weather

print(f"{w.detailed_status=}")         # 'clouds'
print(f"{w.wind()=}")                  # {'speed': 4.6, 'deg': 330}
print(f"{w.humidity=}")                # 87
print(f"{w.temperature('celsius')=}")  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
print(f"{w.rain=}")                    # {}
print(f"{w.heat_index=}")              # None
print(f"{w.clouds=}")                  # 75
print(w)