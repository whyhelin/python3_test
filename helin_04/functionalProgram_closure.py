#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 闭包

# 注意到返回的函数在其定义内部引用了局部变量args，
# 所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用
def lazy_sum(*args):
    def sums():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sums

f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1)
print(f1 == f2)  # False
print(f1())  # 25


# why f1(), f2(), f3() returns 9, 9, 9 rather than 1, 4, 9?
# 全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。
# 等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
# 返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i * i
        fs.append(f)
    return fs

f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())


# fix:
def count():
    fs = []

    def f(n):
        def j():
            return n * n
        return j
    for i in range(1, 4):
        fs.append(f(i))
    return fs

f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())

f = count()
print(f[0]())