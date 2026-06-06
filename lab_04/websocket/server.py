import asyncio
import tornado.websocket
import tornado.web
import tornado.ioloop


class FruitWebSocket(tornado.websocket.WebSocketHandler):
    clients = set()
    fruits = ["Apple", "Banana", "Cherry", "Dragon Fruit", "Elderberry",
              "Fig", "Grape", "Honeydew", "Jackfruit", "Kiwi"]

    def open(self):
        FruitWebSocket.clients.add(self)
        print(f"[WS SERVER] Client connected. Total: {len(self.clients)}")

    def on_close(self):
        FruitWebSocket.clients.discard(self)
        print(f"[WS SERVER] Client disconnected. Total: {len(self.clients)}")

    @classmethod
    async def broadcast_fruits(cls):
        index = 0
        while True:
            if cls.clients:
                fruit = cls.fruits[index % len(cls.fruits)]
                message = f"Fruit #{index + 1}: {fruit}"
                print(f"[WS SERVER] Broadcasting: {message}")
                for client in cls.clients:
                    try:
                        client.write_message(message)
                    except Exception:
                        pass
                index += 1
            await asyncio.sleep(3)


def make_app():
    return tornado.web.Application([
        (r"/ws", FruitWebSocket),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("[WS SERVER] WebSocket server started at ws://127.0.0.1:8888/ws")

    # Start fruit broadcasting task
    loop = asyncio.get_event_loop()
    loop.create_task(FruitWebSocket.broadcast_fruits())

    tornado.ioloop.IOLoop.current().start()
