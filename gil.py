from collections import OrderedDict, namedtuple
from Queue import Queue
from multiprocessing.dummy import Pool
import requests
from threading import Thread
import time

URL = 'https://api.punkapi.com/v2/beers/{}'


def make_pretty_view(response):
    order_response = OrderedDict(sorted(response.items(), key=lambda t: t[0]))

    Beer = namedtuple('Beer', [key.encode('utf-8') for key in order_response])
    p = Beer._make(order_response.values())
    # print p.name, p.tagline


# without threading
t1 = time.time()
for i in range(1, 5):
    response = requests.get(URL.format(i)).json()[0]
    make_pretty_view(response)
t2 = time.time()
print 'Requests without threads took {}'.format(t2 - t1)


# without queue
class MyThread(Thread):
    def __init__(self, name, url):
        Thread.__init__(self)
        self.name = name
        self.url = url

    def run(self):
        response = requests.get(self.url).json()[0]
        make_pretty_view(response)


def create_threads():
    for i in range(1, 5):
        my_thread = MyThread('Thread {}'.format(i), URL.format(i))
        my_thread.start()


t1 = time.time()
create_threads()
t2 = time.time()
print 'Requests with thread without queue took {}'.format(t2 - t1)


# with queue
class MyThreadQ(Thread):
    def __init__(self, name, queue):
        Thread.__init__(self)
        self.name = name
        self.queue = queue

    def run(self):
        while True:
            url = self.queue.get()
            response = requests.get(url).json()[0]
            make_pretty_view(response)
            self.queue.task_done()


def create_threads():
    queue = Queue()

    for i in range(1, 5):
        queue.put(URL.format(i))

    for i in range(1, 5):
        my_thread = MyThreadQ('Thread {}'.format(i), queue)
        my_thread.start()


t1 = time.time()
create_threads()
t2 = time.time()
print 'Requests with thread with queue took {}'.format(t2 - t1)

t1 = time.time()

urls = [URL.format(i) for i in range(1, 5)]
my_pool = Pool(4)
results = my_pool.map(requests.get, urls)
my_pool.close()
# my_pool.join()

for response in results:
    make_pretty_view(response.json()[0])
t2 = time.time()
print 'Requests with multiprocessing took {}'.format(t2 - t1)

#
# """
# Requests without threads took 4.01900005341
# Requests with thread without queue took 0.00499987602234
# Requests with thread with queue took 0.00800013542175
# Requests with multiprocessing took 1.02199983597
# """
