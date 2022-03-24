import os
import requests

url = "http://159.196.152.115:1338/message"
token = os.getenv('SteamMarketPriceWatcherToken')

# Publish a simple message to the specified SNS topic
def sendNotif(prices):
    composeMessage = ""
    for item in prices:
        for name, price in item.items():
            stringBuffer = "{} is:          RM{} (median price)\n".format(name, price)
            composeMessage += stringBuffer
    r = requests.post(
        url=url,
        data={
            "message": composeMessage,
            "priority": 1
        },
        params={
            "token": token
        }
    ) 
    print(r)


