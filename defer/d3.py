'''
addBoth: 类似try catch链里面的finally
'''
from twisted.internet.defer import Deferred


def f1(result):
    print(1)


def f2(r):
    print(2)


def f3(r):
    print(3)


def a1():
    d = Deferred()
    # 增加回调
    d.addCallbacks(f1, f2)
    # 无论走正常 还是 异常回调之后, 最后都会走addBoth的回调
    d.addBoth(f3)
    print(0)
    d.errback(Exception(1))


# def a2():
#     d = Deferred()
#     d.addCallbacks(f1, f2)
#     d.addBoth(f3)
#     print(0)
#     d.callback(True)


print('=====> a1')
a1()

# print('=====> a2')
# a2()

'''
输出:
=====> a1
0
2
3
=====> a2
0
1
3
'''
