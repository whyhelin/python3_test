#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
import os

l = [x * x for x in range(1, 11) if x % 2 == 0]
print(l)

l = [m + n for m in 'ABC' for n in 'XYZ']
print(l)


# os.listdir可以列出文件和目录
l = [d for d in os.listdir('.')]
print(l)

d = {'x': 'A', 'y': 'B', 'z': 'C'}
l = [k + '=' + v for k, v in d.items()]
print(l)

L = ['Hello', 'World', 'IBM', 'Apple']
l = [s.lower() for s in L]
print(l)

L = ['Hello', 'World', 18, 'IBM', 'Apple']
l = [s.lower() if isinstance(s, str) else s for s in L]
print(l)

