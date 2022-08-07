'''
cancel: 成功取消指定defer
期望: 想要取消f3的调用
实际: 成功, 所以f3里面的方法都没有执行
'''
from datetime import datetime

from twisted.internet.defer import Deferred


def f1(r):
    print(f'{datetime.now()} f1 {r}')


def f2(r):
    print(f'{datetime.now()} f2 {r}')


def f3(r):
    print(f'{datetime.now()} f3 start...')
    r.callback(100)


def canceller(r):
    print(f'{datetime.now()} canceller starting..')
    r1.cancel()


d = Deferred(canceller)
d.addCallbacks(f1, f2)

from twisted.internet import reactor

r1 = reactor.callLater(2, f3, d)

reactor.callLater(1, d.cancel)

reactor.callLater(3, reactor.stop)

print(f'{datetime.now()} starting..')
reactor.run()
'''
输出:
2022-08-17 06:52:06.251236 starting..
2022-08-17 06:52:07.251879 canceller starting..
2022-08-17 06:52:07.251879 f2 [Failure instance: Traceback (failure with no frames): <class 'twisted.internet.defer.CancelledError'>:
]
'''
