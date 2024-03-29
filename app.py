import requests
import json
from sendNotif import sendNotif

f = open("/home/pi/SteamMarketPriceWatcher/watchlist.json", "r");
items = f.read();
jsonList = json.loads(items);
currentPrices = []
for item in jsonList:
    r = requests.get(url = item["url"])
    dataInJson = r.json()
    medianPrice = dataInJson["median_price"][2:]
    currentPrices.append({item["name"]:medianPrice})
sendNotif(currentPrices)
