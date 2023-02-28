
import requests
data = {"beer_name":"sodzadazdazuye"}
requests.post("http://127.0.0.1:8000/balance/beers_remove", data)
