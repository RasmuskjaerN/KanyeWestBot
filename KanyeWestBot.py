#KanyeWestBot
import requests
from requests import api
import json


Greeting = "Yo im Yeezy!"

print(Greeting)

API = "https://api.kanye.rest/"

test_api = requests.get("https://api.kanye.rest/")
kanye_quote = test_api.json()
print(kanye_quote['quote'])

quotes = []

for i in range(10):
    test_api = requests.get("https://api.kanye.rest/")
    kanye_quote = test_api.json()
    quotes.append(kanye_quote['quote'])

print(quotes)

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)