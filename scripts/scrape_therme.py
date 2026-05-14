import csv
from datetime import datetime

now = datetime.now()

bad = 80
sauna = 95

temp = 12
weather = "rain"

holiday = False
bayern_match = False
germany_match = False

row = [
    now.isoformat(),
    bad,
    sauna,
    temp,
    weather,
    holiday,
    bayern_match,
    germany_match
]

with open("data/history.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(row)

print("Daten gespeichert")
