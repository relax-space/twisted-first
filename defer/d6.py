'''
succeed用法: 返回一个已经激活的defer
'''
from twisted.internet.defer import Deferred, succeed


def f1(r):
    print(r)
    return 1


def f2(r):
    print(r)
    return 2


d = succeed(0)
# f1的参数, 是callback方法传进来的
d.addCallback(f1)
# f2函数的参数, 是f1的返回值
d.addCallback(f2)

print(3)

'''
输出:
0
1
3
'''
