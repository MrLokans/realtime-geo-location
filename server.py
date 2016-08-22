import os
import json
import uuid
import logging
from collections import defaultdict

from tornado import websocket, web, ioloop

logging.basicConfig(level=logging.INFO)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
static_dir = os.path.join(BASE_DIR, "static")

clients = defaultdict(dict)


def format_clients(clients):
    pass


class IndexHandler(web.RequestHandler):
    def get(self):
        self.render("index.html")


class SocketHandler(websocket.WebSocketHandler):
    def open(self):
        logging.info("WebSocket opened: {}".format(self))
        if self not in clients:
            clients[self]["uid"] = str(uuid.uuid4())
        for client in clients:
            client.write_message("Total clients: {}".format(clients))

    def on_message(self, message):
        coordinates_data = json.loads(message)
        clients[self]["longitude"] = coordinates_data["longitude"]
        clients[self]["latitude"] = coordinates_data["latitude"]
        logging.info("Message received: {}".format(coordinates_data))
        for client in clients:
            client.write_message("Some one told me: {}".format(message))

    def on_close(self):
        clients.pop(self)
        logging.info("WebSocket closed")

app = web.Application([
    (r'/', IndexHandler),
    (r'/ws', SocketHandler),
    (r'/static/(.*)', web.StaticFileHandler, {'path': static_dir}),
])


def main():
    app.listen(8888)
    ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
