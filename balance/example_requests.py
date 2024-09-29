import requests

#req = requests.post("http://127.0.0.1:8000/balance/balance/1", {"activated":False})
#req = requests.post("http://127.0.0.1:8000/balance/alerts", {"alarme_data" : 133})
#req = requests.post("http://127.0.0.1:8000/balance/box_data", {"temperature":10, "humidity":5})
#req = requests.post("http://127.0.0.1:8000/balance/update_beer_data", {"str_beer_1":10, "str_beer_2":13})
#req = requests.get("http://127.0.0.1:8000/balance/balance")
#req = requests.get("http://127.0.0.1:8000/balance/beers_on_balance")
req = requests.post("http://127.0.0.1:8000/balance/balance/2", {"related_beer_id":10, "remaining_beer":180})
#req = requests.post("http://127.0.0.1:8000/balance/balance/1", {"nomComplet":"Cercle Informatique", "nomSimple":"INFO", "nameBeerOrCollective":True})
#req = requests.get("http://127.0.0.1:8000/balance/matrice_led")

#req = requests.post("https://balance.e-kot.be/balance/beers", {"beer_name":"Estaminet","weight_empty":6000,"rho":1013.0,"quantity":250})
#req = requests.post("http://127.0.0.1:8000/balance/balance/1", {"activated":True, "related_beer_id":29, "remaining_beer":180})
#req = requests.post("http://127.0.0.1:8000/balance/send_message", {"message" : "souloulouye"})
#req = requests.post("http://127.0.0.1:8000/balance/data_to_script", json={"message":{"message": "SOUYE", "freq":15, "permanent":True, "scroll":False}})


print(req.text)