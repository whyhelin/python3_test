#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 假定这是你的银行存款:
import multiprocessing
import threading

balance = 0
lock = threading.Lock()


def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(100000):
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)


# 启动与CPU核心数量相同的N个线程，
# 在4核CPU上可以监控到CPU占用率仅有102%，也就是仅使用了一核。
#
# 但是用C、C++或Java来改写相同的死循环，
# 直接可以把全部核心跑满，4核就跑到400%，8核就跑到800%，
# 为什么Python不行呢？
#
# 因为Python的线程虽然是真正的线程，
# 但解释器执行代码时，有一个GIL锁：Global Interpreter Lock，
# 任何Python线程执行前，必须先获得GIL锁，
# 然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。
# 这个GIL全局锁实际上把所有线程的执行代码都给上了锁，
# 所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。
#
# GIL是Python解释器设计的历史遗留问题，
# 通常我们用的解释器是官方实现的CPython，
# 要真正利用多核，除非重写一个不带GIL的解释器。
#
# 所以，在Python中，可以使用多线程，但不要指望能有效利用多核。
# 如果一定要通过多线程利用多核，那只能通过C扩展来实现，不过这样就失去了Python简单易用的特点。
#
# 不过，也不用过于担心，Python虽然不能利用多线程实现多核任务，
# 但可以通过多进程实现多核任务。多个Python进程有各自独立的GIL锁，互不影响。
def loop():
    x = 0
    while True:
        x = x ^ 1
        print(threading.current_thread().name)

# for i in range(multiprocessing.cpu_count()):
#     t = threading.Thread(target=loop)
#     t.start()

print(multiprocessing.cpu_count())
print(multiprocessing.current_process())
