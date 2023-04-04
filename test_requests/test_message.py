import requests
requests.post("http://127.0.0.1:8000/balance/message_data", {"message": "souye", "freq":15, "permanent":False, "scroll":True})