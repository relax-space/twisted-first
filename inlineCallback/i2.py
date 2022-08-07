'''
inlineCallbacks中的returnValue: 返回一个defer对象
'''

from twisted.internet.defer import inlineCallbacks, returnValue


@inlineCallbacks
def f1():
    print(1)
    a = yield 2
    print(a)

    returnValue(3)


def f2(d):
    print(d)


d = f1()
d.addCallback(f2)

'''
输出:
1
2
3
'''
