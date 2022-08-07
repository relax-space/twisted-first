'''
立即触发: 如果deferredList里面是空的
'''
from twisted.internet.defer import Deferred, DeferredList


def f1(r):
    print(2)


d1 = Deferred()
d2 = Deferred()
d = DeferredList([])

d.addCallback(f1)
'''
输出:
2
'''
