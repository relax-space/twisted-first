'''
inlineCallbacks: 就是一直循环的调用生成器的send方法, send的参数:将前一次的返回值当做下一次的输入值
注: 如果为一般数据或者已激活的defer, 则直接返回, 继续往下走, 如果是未激活的defer, 则程序会暂停,defer激活完成后,再继续往下走
'''

from twisted.internet.defer import Deferred, inlineCallbacks


@inlineCallbacks
def f1():
    print(1)
    a = yield 2
    print(a)

    b = yield a
    print(b)

    d = Deferred()
    d.callback(0)
    c = yield d
    print(c)


f1()
'''
输出:
1
2
2
0
'''
