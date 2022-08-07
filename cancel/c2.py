'''
cancel: 如果调用callback, 可能就不会执行cancel了
'''
from twisted.internet.defer import Deferred

def f1(r):
    print(1)
    
def f2(r):
    print(2)
    
d = Deferred()
d.addCallbacks(f1,f2)
d.callback(True)
# 没有调用f2
d.cancel()

'''
输出:
1
'''