import json
import pprint
import sseclient

def with_urllib3(url, headers):
    """Get a streaming response for the given event feed using urllib3."""
    import urllib3
    http = urllib3.PoolManager()
    return http.request('GET', url, preload_content=False, headers=headers)

def with_requests(url, headers):
    """Get a streaming response for the given event feed using requests."""
    import requests
    return requests.get(url, stream=True, headers=headers)

url = 'http://127.0.0.1:8000/balance/beers_data'
headers = {'Accept': 'text/event-stream'}
response = with_requests(url, headers)  # or with_requests(url, headers)
client = sseclient.SSEClient(response)
print("I'm executed")
print(response.text)
print(client)
for event in client.events():
    print(event)
    pprint.pprint(json.loads(event.data))