import csv
import re
import requests

from datetime import datetime
import holidays

now = datetime.now()

# Therme Webseite laden
url = "https://www.therme-bad-aibling.de"

response = requests.get(url)

html = response.text

# HTML speichern
with open("data/page.html", "w", encoding="utf-8") as f:
    f.write(html)

# Prozentwerte finden
matches = re.findall(r'data-occupied=\"([0-9\\.]+)\"', html)

bad = round(float(matches[0]))
sauna = round(float(matches[1]))

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

de_holidays = holidays.DE(prov='BY')

holiday = now.date() in de_holidays
weekend = now.weekday() >= 5
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

print("Bad:", bad)
print("Sauna:", sauna)
print("Temperatur:", temp)
print("Daten gespeichert")
