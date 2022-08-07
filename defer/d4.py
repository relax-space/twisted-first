'''
defer 链
'''
from twisted.internet.defer import Deferred


def f1(r):
    print(r)
    return 1


def f2(r):
    print(r)
    return 2


d = Deferred()

# f1的参数, 是callback方法传进来的
d.addCallback(f1)
# f2函数的参数, 是f1的返回值
d.addCallback(f2)

print(3)

d.callback(0)

'''
输出:
3
0
1
'''
