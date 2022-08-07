'''
maybeDeferred适用场景: 不确定返回值是defer还是一般的值, 但是又期望返回值是defer
注: 如果是Deferred对象原样返回, 如果是一般的值, 则包装成激活的Deferred再返回
'''

from twisted.internet.defer import Deferred, maybeDeferred


def f1(r):
    print(r)


def f2(r):
    if r == 1:
        return 100
    return Deferred()


def f3():
    d2 = maybeDeferred(f2, 1)
    d2.addCallback(f1)


def f4():
    d2 = maybeDeferred(f2, 2)
    d2.addCallback(f1)
    d2.callback(0)


f3()
print('========')
f4()
'''
输出:
100
========
0
'''
