'''
立即执行: callWhenRunning
延迟执行: callLater
'''

from datetime import datetime


def f1():
    print(f'{datetime.now()} no delay')


def f2():
    print(f'{datetime.now()} delay 1 s')


from twisted.internet import reactor

print(f'{datetime.now()} start ...')

reactor.callLater(1, f2)

# reactor.callWhenRunning(f1)

reactor.run()

'''
输出:
2022-08-17 06:47:43.263909 start ...
2022-08-17 06:47:43.263909 no delay
2022-08-17 06:47:44.267028 delay 1 s
'''
