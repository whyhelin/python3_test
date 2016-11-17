#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import queue
import random
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

# 在Thread和Process中，应当优选Process，
# 因为Process更稳定，而且，Process可以分布到多台机器上，
# 而Thread最多只能分布到同一台机器的多个CPU上。

# Python的multiprocessing模块不但支持多进程，
# 其中managers子模块还支持把多进程分布到多台机器上。
# 一个服务进程可以作为调度者，将任务分布到其他多个进程中，依靠网络通信。
# 由于managers模块封装很好，不必了解网络通信的细节，就可以很容易地编写分布式多进程程序。


# 发送任务的队列:
task_queue = queue.Queue()
# 接收结果的队列:
result_queue = queue.Queue()


def get_task_queue():
    global task_queue
    return task_queue


def get_result_queue():
    global result_queue
    return result_queue


# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass


# 当我们在一台机器上写多进程程序时，创建的Queue可以直接拿来用，
# 但是，在分布式多进程环境下，添加任务到Queue不可以直接对
# 原始的task_queue进行操作，那样就绕过了QueueManager的封装，
# 必须通过manager.get_task_queue()获得的Queue接口添加。
def start_master():
    # 把两个Queue都注册到网络上, callable参数关联了Queue对象:
    # register内不要使用lambda，否则win7运行出错
    QueueManager.register('get_task_queue', callable=get_task_queue)
    QueueManager.register('get_result_queue', callable=get_result_queue)

    # 绑定端口5000, 设置验证码'abc':
    # win7 需要写ip地址
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')

    # 启动Queue:
    manager.start()

    # 获得通过网络访问的Queue对象:
    task = manager.get_task_queue()
    result = manager.get_result_queue()

    # 放几个任务进去:
    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %d...' % n)
        task.put(n)

    # 从result队列读取结果:
    print('Try get results...')
    for i in range(10):
        try:
            r = result.get(timeout=10)
            print('Result: %s' % r)
        except queue.Empty:
            print('result queue is empty.')

    # 关闭:
    manager.shutdown()
    print('master exit.')

if __name__ == '__main__':
    freeze_support()        # 注释掉也可以正常运行
    start_master()
