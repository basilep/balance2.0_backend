
import requests
data = {"beer_name":"sodzadazdazuye", "weight_empty":18, "rho":1, "quantity":2}
requests.post("http://127.0.0.1:8000/balance/beers", data)
