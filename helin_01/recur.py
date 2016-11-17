#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 利用递归函数计算阶乘
# N! = 1 * 2 * 3 * ... * N
def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n-1)

print(fac(5))
print(fac(100))


# 尾递归
def fac_item(n, result):
    if n == 1:
        return result
    else:
        return fac_item(n - 1, n * result)


def fac2(n):
    return fac_item(n, 1)

print(fac2(5))
print(fac2(500))


# 利用递归函数移动汉诺塔:
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
        return
    move(n-1, a, c, b)
    print('move', a, '-->', c)
    move(n-1, b, a, c)

move(4, 'A', 'B', 'C')