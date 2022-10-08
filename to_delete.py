import requests
URL1='http://localhost:8000/admin/'
URL2='http://localhost:8000/admin/login/?next=/admin/'
UN='balance'
PWD='cerkInfo1970'
client = requests.session()

# Retrieve the CSRF token first
client.get(URL1)  # sets the cookie
csrftoken = client.cookies['csrftoken']
print(csrftoken)

login_data = dict(username=UN, password=PWD, csrfmiddlewaretoken=csrftoken)
r1=client.post(URL1,data=login_data)

beer  = client.get("http://127.0.0.1:8000/balance/beers_data")
#print(beer.text)