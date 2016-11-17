#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

from helin_01.functions_list import my_abs, my_abs2, move, power, enroll, add_end, add_end2, calc, person, info, info2, \
    info3, f1, f2

print(my_abs(-9))
# print(my_abs('a'))
print(my_abs2(-9))
# print(my_abs2('a'))

# 空函数
# 如果想定义一个什么事也不做的空函数，可以用pass语句：


def nop():
    pass

nop()


# 原来返回值是一个tuple！
# 但是，在语法上，返回一个tuple可以省略括号，
# 而多个变量可以同时接收一个tuple，按位置赋给对应的值，
# 所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。

x, y = move(100, 100, 60, math.pi/6)
print(x, y)

r = move(100, 100, 60, math.pi/6)
print(r)

print(power(5))
print(power(5))
print(power(5, 3))
print(power(5, 4))

enroll('Adam', 'M', city='Tianjin')

# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，
# 因为默认参数L也是一个变量，它指向对象[]，
# 每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
# 所以，定义默认参数要牢记一点：默认参数必须指向不变对象！
print(add_end([1, 2]))
print(add_end(['a', 'b']))
print(add_end())
print(add_end())
print(add_end2())
print(add_end2())
print(add_end2(None))

# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。
# 在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变
# 所以Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple
print(calc(1, 2))
print(calc(*[1, 2]))

person('Adam', 45)
person('Adam', 45, gender='M', job='Engineer')

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])
person('Jack', 24, **extra)

info('Jack', 24, city='Beijing', job='Engineer')
# info('Jack', 24, 'Beijing', 'Engineer')

info2('Jack', 24, city='Beijing', job='Engineer')
# info2('Jack', 24, 'Beijing', 'Engineer')
info2('Jack', 24, 'Beijing', 'Engineer', city='Beijing', job='Engineer')

info3('Jack', 24, job='Engineer')


f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)


