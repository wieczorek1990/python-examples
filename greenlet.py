from gevent import spawn, sleep, Greenlet
from time import sleep as s


def observe_mailbox(text):
    raise Exception(text)


greenlet = Greenlet(observe_mailbox, 'hello')
greenlet.start()
sleep()

while not greenlet.ready():
    print 'wait'
    s(1)

print greenlet.exception.message
