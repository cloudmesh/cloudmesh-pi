import falcon
import motor


class MainHandler(object):
    def on_get(self, req, resp):
        driver = motor.MotorDriver()
        driver.setLeftSpeed(int(req.params["LEFT"]))
        driver.setRightSpeed(int(req.params["RIGHT"]))


def _get_app():
    main = MainHandler()
    app = falcon.API()

    app.add_route('/', main)

    return app


if __name__ == "__main__":
    import sys
    from wsgiref.simple_server import web_server

    app = _get_app()
    interface = sys.argv[1]
    port = 8080
    if len(sys.argv) == 3:
        port = sys.argv[2]
    server = web_server(interface, int(port), app)

    print("Listening on http://{}:{}".format(interface, port))
    server.serve_forever()
else:
    application = _get_app()
