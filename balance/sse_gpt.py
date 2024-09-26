import requests

def sse_client(url):
    try:
        # Open a streaming connection to the SSE endpoint
        with requests.get(url, stream=True, headers={"Accept": "text/event-stream"}) as response:
            if response.status_code == 200:
                print("Connected to SSE server...")
                # Process the stream line by line
                for line in response.iter_lines(decode_unicode=True):
                    if line:
                        # Print the received message (after the "data: " part)
                        print(line[5:].strip())  # Strip out 'data: ' from the start of each line
            else:
                print(f"Failed to connect, status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    # Use the correct URL path to your Django SSE stream
    server_url = 'http://127.0.0.1:8000/sse-stream/'  # Replace with your correct URL
    print("Connecting to SSE server...")
    sse_client(server_url)
