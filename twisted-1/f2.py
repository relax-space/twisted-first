'''
LoopingCall: 定时执行
'''
from datetime import datetime


def f1():
    print(f'{datetime.now()} process')


from twisted.internet import reactor, task

l = task.LoopingCall(f1)
# 每隔1秒执行一次. now 默认是true,表示立即执行, 为false表示1秒之后再调用
l.start(1, now=False)
print(f'{datetime.now()} start ...')

reactor.run()

'''
输出:
2022-08-17 06:48:19.045720 process
2022-08-17 06:48:20.055546 process
2022-08-17 06:48:21.050500 process
'''
