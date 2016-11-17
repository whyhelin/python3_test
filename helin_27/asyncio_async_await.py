#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
import threading

# 为了简化并更好地标识异步IO，从Python 3.5开始引入了新的语法async和await，
# 可以让coroutine的代码更简洁易读。
#
# 请注意，async和await是针对coroutine的新语法，
# 要使用新的语法，只需要做两步简单的替换：
#
# 把@asyncio.coroutine替换为async；
# 把yield from替换为await。


async def hello():
    print('Hello world! (%s)' % threading.currentThread())
    await asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

