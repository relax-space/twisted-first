'''
defer 立即执行: callback在addcallback的前面
'''
from twisted.internet.defer import Deferred


def f1(r):
    print(r)
    return 1


def f2(r):
    print(r)
    return 2


d = Deferred()
d.callback(0)

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
