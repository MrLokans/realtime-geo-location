import os
from tornado import websocket, web, ioloop

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
static_dir = os.path.join(BASE_DIR, "static")

clients = []


class IndexHandler(web.RequestHandler):
    def get(self):
        self.render("index.html")


class SocketHandler(websocket.WebSocketHandler):
    def open(self):
        if self not in clients:
            clients.append(self)
        for client in clients:
            client.write_message("Total clients: {}".format(clients))
        print("WebSocket opened")

    def on_message(self, message):
        for client in clients:
            client.write_message("Some one told me: {}".format(message))

    def on_close(self):
        print("WebSocket closed")

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
