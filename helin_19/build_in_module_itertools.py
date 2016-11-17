#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools

# itertools模块提供的全部是处理迭代功能的函数，
# 它们的返回值不是list，而是Iterator，只有用for循环迭代的时候才真正计算。


# count()会创建一个无限的迭代器，所以上述代码会打印出自然数序列，根本停不下来，只能按Ctrl+C退出。
natuals = itertools.count(2)
for n in natuals:
    print(n)
    if n >= 10:
        break


# cycle()会把传入的一个序列无限重复下去：
cs = itertools.cycle('ABC')
t = 10
for c in cs:
    print(c)
    t = t - 1
    if t == 0:
        break


# repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数：
re = itertools.repeat('abc', 3)
for c in re:
    print(c)


# 无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列
na = itertools.count(1)
m = itertools.takewhile(lambda x: x < 10, na)
for n in m:
    print(n)


# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
for c in itertools.chain('abc', '123'):
    print(c)


# groupby()把迭代器中相邻的重复元素挑出来放在一起：
for k, v in itertools.groupby('aaAbbBccCa', lambda c: c.upper()):
    print(k, list(v))

