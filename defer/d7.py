'''
defer异步的实现方式: defer里面嵌套另外的defer
'''
from twisted.internet.defer import Deferred


def f1(r):
    print(f'f1 {r}')
    return 1


def f2(r):
    print(f'f2 {r}')
    global d2
    d2 = Deferred()
    return d2


def f3(r):
    print(f'f3 {r}')
    return 3


d2: Deferred = None
d = Deferred()

d.addCallback(f1)
d.addCallback(f2)
# f3是在f2的内部defer触发之后触发的
d.addCallback(f3)

d.callback(0)

print('触发内层的defer')

d2.callback(2)

'''
输出:
f1 0
f2 1
触发内层的defer
f3 2
'''