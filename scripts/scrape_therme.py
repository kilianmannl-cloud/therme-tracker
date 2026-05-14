import csv
import re
import requests

from datetime import datetime

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
