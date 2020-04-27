import time

from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop
from tornado import gen


@gen.coroutine
def async_sleep(seconds):
    yield gen.Task(IOLoop.instance().add_timeout, time.time() + seconds)


class TestHandler(RequestHandler):
    @gen.coroutine
    def get(self):
        for i in xrange(100):
            print i
            yield async_sleep(1)
            self.write(str(i))
            self.finish()


application = Application([
    (r"/test", TestHandler),
])

application.listen(9999)
IOLoop.instance().start()
