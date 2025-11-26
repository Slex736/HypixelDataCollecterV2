import requests
import csv
from zoneinfo import ZoneInfo
from datetime import datetime

url = "https://api.hypixel.net/v2/skyblock/bazaar"
response = requests.get(url)
data = response.json()



items = ['SHARD_MEGALITH', 
         'SHARD_TIAMAT', 
         'ROBOTRON_REFLECTOR', 
         'ENCHANTMENT_PESTERMINATOR_1', 
         'SHARD_SHINYFISH', 
         'MOLTEN_POWDER', 'HEMOBOMB', 
         'SHARD_SEA_EMPEROR', 'SEARING_STONE', 
         'SHARD_LIZARD_KING', 'ENCHANTED_SULPHUR_CUBE', 
         'SHARD_HIDEONCAVE', 'ENCHANTED_COOKED_SALMON', 
         'SHARD_POWER_DRAGON', 'SHARD_CUBOA',
         'ENCHANTED_DIAMOND_BLOCK', 
         'SHARD_SALAMANDER', 'ENCHANTMENT_ULTIMATE_WISE_2',
         'JERRY_BOX_PURPLE', 'HORSEMAN_CANDLE', 
         'WHIPPED_MAGMA_CREAM', 'TITANIC_EXP_BOTTLE',
         'DUNGEON_CHEST_KEY']



if data.get("success"):
    products = data["products"]
    
    ProductStats = []

    for product in products.values():
        
        stats = product["quick_status"]
        price = (stats["buyPrice"] + stats["sellPrice"])  / 2 # Makes a rough estimate of one price
        turnover = stats["sellVolume"] + stats["buyVolume"]
        productname = stats["productId"]

        for item in items:
            if item == productname:

                ProductStats.append([price])



    print(ProductStats)
else:
    print("API error:", data)

now = datetime.now(ZoneInfo("Europe/Amsterdam"))
time = now.strftime("%Y-%m-%d %H:%M:%S")

with open("Data.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([time] + ProductStats) 

