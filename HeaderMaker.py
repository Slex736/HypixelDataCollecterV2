import requests
import csv

url = "https://api.hypixel.net/v2/skyblock/bazaar"
response = requests.get(url)
data = response.json()



if data.get("success"):
    products = data["products"]
    
    ProductStats = []
    products_name = []

    for product in products.values():
        
        stats = product["quick_status"]
        price = (stats["buyPrice"] + stats["sellPrice"])  / 2 # Makes a rough estimate of one price
        turnover = stats["sellVolume"] + stats["buyVolume"]
        productname = stats["productId"]

        ProductStats.append([productname, price])
        products_name.append(productname)


else:
    print("API error:", data)


headers = ["time"] + products_name



with open("DataAllitems.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(headers) 