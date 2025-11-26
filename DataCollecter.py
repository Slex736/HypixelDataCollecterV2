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
        
        if turnover > 100000 and price < 500000 and price > 200000:

            ProductStats.append([productname, price])
            products_name.append(productname)


else:
    print("API error:", data)

print(products_name)
headers = ["time"] + products_name



with open("Data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(headers) 

