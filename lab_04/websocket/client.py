import asyncio
import websockets


async def listen():
    uri = "ws://127.0.0.1:8888/ws"
    async with websockets.connect(uri) as websocket:
        print(f"[WS CLIENT] Connected to {uri}")
        while True:
            try:
                message = await websocket.recv()
                print(f"[WS CLIENT] Received: {message}")
            except websockets.exceptions.ConnectionClosed:
                print("[WS CLIENT] Connection closed")
                break


if __name__ == "__main__":
    asyncio.run(listen())
