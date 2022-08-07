'''
addcallbacks: 触发异常的时候, 进入第二个参数
errback: 触发异常回调
'''
from twisted.internet.defer import Deferred


def f1(result):
    print(1)
    
def f2(r):
    print(2)


d = Deferred()
# 增加回调
d.addCallbacks(f1,f2)
print(0)
# 触发回调
d.errback(Exception(1))

'''
输出:
0
2
'''
