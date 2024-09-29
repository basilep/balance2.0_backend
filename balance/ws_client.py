import asyncio
import websockets

async def listen_to_server():
    uri = "ws://localhost:5000"
    while True:
        try:
            async with websockets.connect(uri) as websocket:
                print("Connected to the server, listening for messages\n")
                while True:
                    message = await websocket.recv()
                    print(f"Message received: {message}")
        except websockets.exceptions.ConnectionClosedError as e:
            print(f"Connection closed, retrying in 5 seconds: {e}")
            await asyncio.sleep(5)  # Retry after 5 seconds
        except Exception as e:
            print(f"An error occurred: {e}")
            await asyncio.sleep(5)  # Retry after 5 seconds

if __name__ == "__main__":
    asyncio.run(listen_to_server())
