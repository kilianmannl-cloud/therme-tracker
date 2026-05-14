import csv
import requests

from datetime import datetime

now = datetime.now()

# Wetterdaten von Open-Meteo
weather_url = (
    "https://api.open-meteo.com/v1/forecast"
    "?latitude=47.86"
    "&longitude=12.01"
    "&current=temperature_2m,weather_code"
)

weather_data = requests.get(weather_url).json()

temp = weather_data["current"]["temperature_2m"]
weather_code = weather_data["current"]["weather_code"]

# Noch Testwerte für Therme
bad = 80
sauna = 95

holiday = False
bayern_match = False
germany_match = False

row = [
    now.isoformat(),
    bad,
    sauna,
    temp,
    weather_code,
    holiday,
    bayern_match,
    germany_match
]

with open("data/history.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(row)

print("Daten gespeichert")
