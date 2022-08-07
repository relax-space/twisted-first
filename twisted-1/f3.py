'''
并发: 通过DeferredList 和 callLater实现
'''
from datetime import datetime

from twisted.internet.defer import DeferredList, succeed


def f0(i):
    print(f'{datetime.now()}: {i}')


def f1(i):
    from twisted.internet import reactor
    reactor.callLater(1, f0, i)


def f():
    ds = [succeed(i).addCallback(f1) for i in range(3)]
    DeferredList(ds)


d = f()

from twisted.internet import reactor

reactor.run()
