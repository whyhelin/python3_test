#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools

a = int('12345', base=8)
print(a)


# 简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），
# 返回一个新的函数，调用这个新函数会更简单。

int2 = functools.partial(int, base=2)

print('1000000 =', int2('1000000', base=10))
print('1010101 =', int2('1010101'))

# 最后，创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数
max2 = functools.partial(max, 10)
print(max2(4, 5))  # 10

