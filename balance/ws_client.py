import asyncio
import websockets

async def main():
    uri = "ws://localhost:5000"
    
    async with websockets.connect(uri) as websocket:
        print("Listen to the server, wait for messages\n")
        while True:
            message = await websocket.recv()
            print(f"Message received: {message}")

if __name__ == "__main__":
    asyncio.run(main())