
import requests
beer  = requests.get("http://127.0.0.1:8000/balance/beers_data")
print(beer.text)
requests.post("http://127.0.0.1:8000/balance/beers", beer)
data = {"username":"balance", "password":"cerkInfo1970"}
requests.post("http://127.0.0.1:8000/balance/login", data)
beer  = requests.get("http://127.0.0.1:8000/balance/beers_data")
print(beer.text)
