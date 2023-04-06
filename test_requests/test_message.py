import requests
requests.post("http://127.0.0.1:8000/balance/message_data", {"message": "test_web_hook", "freq":15, "permanent":False, "scroll":True})
#requests.post("https://balance.e-kot.be/balance/message_data", {"message": "souye", "freq":15, "permanent":False, "scroll":True})