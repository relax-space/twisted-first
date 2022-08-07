'''
只有deferredlist里面的defer全部触发, 才会触发deferredlist的回调
顺序: 以DeferredList参数顺序为主, 而不是调用callback的顺序
'''
from twisted.internet.defer import Deferred, DeferredList


def f1(r):
    print(r)


d1 = Deferred()
d2 = Deferred()
d = DeferredList([d1, d2])

d.addCallback(f1)
print(0)
d2.callback(10)
print(1)
d1.callback(11)
'''
输出:
0
1
[(True, 11), (True, 10)]
'''
