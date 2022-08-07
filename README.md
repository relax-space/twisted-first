# twisted-first

## 目录

### 延迟执行

``` python
'''
延迟1秒之后执行
'''
from datetime import datetime

from twisted.internet import reactor


def f(s):
    print(f'{datetime.now()} hello {s}')
    reactor.stop()


print(f'{datetime.now()} start...')
reactor.callLater(1, f, 'world')

reactor.run()
```
### 每隔几秒执行一次
``` python
'''
每隔1秒执行一次
'''
import time
from datetime import datetime

from twisted.internet import reactor, task


def f():
    print(datetime.now())


print(f'{datetime.now()} start...')
l = task.LoopingCall(f)
# now参数,第一次执行:是否立即执行, 还是等1秒之后才执行
l.start(1.0, now=False)

reactor.callLater(5, reactor.stop)
reactor.run()


```
