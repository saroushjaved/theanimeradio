import requests
import random

number = random.randint(10000, 11200)
URL = "https://anime-chan.herokuapp.com/api/quotes/random"
req = requests.get(url = URL)
data = req.json()
quote = data[0]['quote']
character= character[0]['character']