'''
addcallback: 增加回调函数
callback: 触发回调函数
'''
from twisted.internet.defer import Deferred


def f1(result):
    print(1)


d = Deferred()
# 增加回调
d.addCallback(f1)
print(0)
# 触发回调
d.callback(True)

'''
输出:
0
1
'''
