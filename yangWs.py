
import tornado.ioloop
import tornado.web
from suds.client import Client


def ws(request):
    url = 'http://61.184.78.105:4588/skpayservice/skpayws.asmx?WSDL'
    client = Client(url)
    services = client.service
    result = services.rews(request)
    # print(result)
    return result


class mainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

    def post(self):
        print(ws(str(self.request.body, 'utf-8')))
        self.write("ok")


def make_app():
    return tornado.web.Application([
        (r"/test", mainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8088)
    print('Server started at http://127.0.0.1:8088...')
    tornado.ioloop.IOLoop.current().start()
