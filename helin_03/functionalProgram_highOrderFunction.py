#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 函数式编程就是一种抽象程度很高的编程范式，
# 纯粹的函数式编程语言编写的函数没有变量，
# 因此，任意一个函数，只要输入是确定的，输出就是确定的，
# 这种纯函数我们称之为没有副作用。
# 而允许使用变量的程序设计语言，由于函数内部的变量状态不确定，
# 同样的输入，可能得到不同的输出，因此，这种函数是有副作用的。

# 函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！
# Python对函数式编程提供部分支持。
# 由于Python允许使用变量，因此，Python不是纯函数式编程语言。

# 把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。
from cmath import sqrt, tan


def add(x, y, f):
    return f(x) + f(y)

print(add(-5, 6, abs))


def same(x, *fs):
    s = [f(x) for f in fs]
    return s

print(same(5, abs, tan, sqrt))


def same2(num, *kw):
    # 参数检查
    if not isinstance(num, (int, float)):
        raise TypeError('bad operand type')
    # 初始化结果字典
    rel = {}
    # 循环计算可变参数
    for func in kw:
        try:
            rel[str(func)[str(func).find('function ') + 9: -1]] = func(num)
        except ValueError:
            rel[str(func)[str(func).find('function ') + 9: -1]] = 'None'
    # 返回结果字典
    return rel

result = same2(-10.5, sqrt, abs, tan)
print(result)

