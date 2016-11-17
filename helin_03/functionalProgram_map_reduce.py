#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# map()函数接收两个参数，一个是函数，一个是Iterable，
# map将传入的函数依次作用到序列的每个元素，
# 并把结果作为新的Iterator返回。
from functools import reduce


def f(x):
    return x * x

print(list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
# 这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
# 比方说对一个序列求和，就可以用reduce实现：
def add(x, y):
   return x + y

print(reduce(add, [1, 3, 5, 7, 9]))


# 但是如果要把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场：
def fn(x, y):
    return x * 10 + y

print(reduce(fn, [1, 3, 5, 7, 9]))


# 这个例子本身没多大用处，但是，如果考虑到字符串str也是一个序列，
# 对上面的例子稍加改动，配合map()，我们就可以写出把str转换为int的函数：
def str2int(s):
    def fnn(x, y):
        return x * 10 + y

    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fnn, map(char2num, s))

print(str2int('12345'))


# 还可以用lambda函数进一步简化成：
def str2int2(s):
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


print(str2int('12345'))


CHAR_TO_INT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}


def str2int(s):
    ints = map(lambda ch: CHAR_TO_INT[ch], s)
    return reduce(lambda x, y: x * 10 + y, ints)

print(str2int('0'))
print(str2int('12300'))
print(str2int('0012345'))

CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1
}


def str2float(s):
    nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
    point = 0

    def to_float(x1, x2):
        nonlocal point
        if x2 == -1:
            point = 1
            return x1
        if point == 0:
            return x1 * 10 + x2
        else:
            point = point * 10
            return x1 + x2 / point

    return reduce(to_float, nums, 0.0)


def str2float2(s):
    def cal(x, y):
        return x * 10 + y
    m = s.find('.')
    if m != -1:
        return reduce(cal, map(int, s[:m] + s[m + 1:]), 0.0) / pow(10, len(s[m + 1:]))
    else:
        return reduce(cal, map(int, s), 0.0)

print(str2float('0'))
print(str2float2('123.456'))
print(str2float2('123'))
print(str2float('123.45600'))
print(str2float('0.1234'))
print(str2float('.1234'))
print(str2float('120.0034'))