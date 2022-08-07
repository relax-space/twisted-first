'''
cancel: 取消不完全的情况
期望: 想要取消f3的调用
实际: 没有成功, 只是取消了f3里面的callback方法
注: 后面的例子就解决这个问题
'''
from twisted.internet.defer import Deferred


def f1(r):
    print(f'f1 {r}')


def f2(r):
    print(f'f2 {r}')


def f3(r):
    print(f'f3 start...')
    r.callback(100)


d = Deferred()
d.addCallbacks(f1, f2)

from twisted.internet import reactor

reactor.callLater(2, f3, d)

reactor.callLater(1, d.cancel)

reactor.callLater(3, reactor.stop)

reactor.run()

'''
输出:
f2 [Failure instance: Traceback (failure with no frames): <class 'twisted.internet.defer.CancelledError'>: 
]
f3 start...
'''
