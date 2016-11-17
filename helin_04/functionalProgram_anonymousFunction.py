#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 关键字lambda表示匿名函数，冒号前面的x表示函数参数。
# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。

a = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(a)


f = lambda x: x * x
print(f(5))


def build(x, y):
    return lambda: x * x + y * y

print(build(1, 2)())

