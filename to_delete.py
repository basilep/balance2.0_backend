import requests
data = {"message": "souye", "freq": 5, "permanent": False}
requests.post("http://127.0.0.1:8000/balance/message_data", data)
