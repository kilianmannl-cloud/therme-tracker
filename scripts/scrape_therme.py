import csv
import requests

from datetime import datetime

now = datetime.now()

# Therme Webseite laden
url = "https://www.therme-bad-aibling.de"

response = requests.get(url)

# HTML speichern
with open("data/page.html", "w", encoding="utf-8") as f:
    f.write(response.text)

# Wetterdaten
weather_url = (
    "https://api.open-meteo.com/v1/forecast"
    "?latitude=47.86"
    "&longitude=12.01"
    "&current=temperature_2m,weather_code"
)

weather_data = requests.get(weather_url).json()

temp = weather_data["current"]["temperature_2m"]
weather_code = weather_data["current"]["weather_code"]

# Noch Testwerte
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

print("HTML gespeichert")
print("Daten gespeichert")
