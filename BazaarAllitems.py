import requests
import csv
from zoneinfo import ZoneInfo
from datetime import datetime

url = "https://api.hypixel.net/v2/skyblock/bazaar"
response = requests.get(url)
data = response.json()



if data.get("success"):
    products = data["products"]
    
    ProductStats = []

    for product in products.values():
        
        stats = product["quick_status"]
        price = (stats["buyPrice"] + stats["sellPrice"])  / 2 # Makes a rough estimate of one price
        turnover = stats["sellVolume"] + stats["buyVolume"]
        productname = stats["productId"]


        ProductStats.append([price])

else:
    print("API error:", data)

now = datetime.now(ZoneInfo("Europe/Amsterdam"))
time = now.strftime("%Y-%m-%d %H:%M:%S")

with open("DataAllitems.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([time] + ProductStats) 