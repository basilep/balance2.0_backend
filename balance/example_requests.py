import requests

#req = requests.post("http://127.0.0.1:8000/balance/balance/2", {"activated":True})
#req = requests.get("http://127.0.0.1:8000/balance/alerts", json={"type":4, "data":{"sensor": "balance_1"}})
#req = requests.post("http://127.0.0.1:8000/balance/box_data", {"temperature":10, "humidity":5})
#req = requests.post("http://127.0.0.1:8000/balance/update_beer_data", {"str_beer_1":10, "str_beer_2":13})
#req = requests.get("http://127.0.0.1:8000/balance/balance")
#req = requests.get("http://127.0.0.1:8000/balance/beers_on_balance")
#req = requests.post("http://127.0.0.1:8000/balance/balance/1", {"related_beer_id":7, "remaining_beer":180})
#req = requests.post("http://127.0.0.1:8000/balance/balance/1", {"nomComplet":"Cercle Informatique", "nomSimple":"INFO", "nameBeerOrCollective":True})
req = requests.get("http://127.0.0.1:8000/balance/matrice_led")
print(req.text)