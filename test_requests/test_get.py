import requests
data = requests.get("http://127.0.0.1:8000/balance/beers")
#data = requests.get("https://balance.e-kot.be/balance/beers")
print(data.text)