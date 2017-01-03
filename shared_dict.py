from multiprocessing import Manager
from time import sleep

from celery import Celery

app = Celery('tasks', broker='amqp://guest@localhost//')

manager = Manager()
lock = manager.Lock()
dictionary = manager.dict()
dictionary['counter'] = 0


def synchronized(lock):
    """
    Decorator for critical section using lock.
    :param lock: threading.Lock
    :return: decorated function
    """

    def wrap(func):
        def new_func(*args, **kw):
            lock.acquire()
            try:
                return func(*args, **kw)
            finally:
                lock.release()

        return new_func

    return wrap


@synchronized(lock)
def set_counter_value(value, expected):
    if dictionary['counter'] == expected:
        dictionary['counter'] = value
        print 'Value changed'
    else:
        print 'Same value'
    print dictionary['counter']


@app.task
def one():
    while True:
        set_counter_value(1, 0)
        sleep(1)


@app.task
def two():
    while True:
        set_counter_value(0, 1)
        sleep(1)

one.apply_async()
two.apply_async()
