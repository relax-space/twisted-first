'''
cancel: 正常取消
'''
from twisted.internet.defer import Deferred


def f1(r):
    print(1)


def f2(r):
    print(2)


d = Deferred()
d.addCallbacks(f1, f2)
# 抛出cancel异常,调用f2
d.cancel()

'''
输出:
2
'''
