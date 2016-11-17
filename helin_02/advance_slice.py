#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print('L[0:3] =', L[0:3])
print('L[:3] =', L[:3])
print('L[1:3] =', L[1:3])
print('L[-2:] =', L[-2:])

R = list(range(100))
print('R[:10] =', R[:10])
print('R[-10:] =', R[-10:])
print('R[10:20] =', R[10:20])
print('R[:10:2] =', R[:10:2])
print('R[::5] =', R[::5])


# tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
t = (0, 1, 1, 2, 3, 4, 5)[:3]
print(t[:])


# 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：
s = 'ABCDEFG'[:3]
print(s)
s = 'ABCDEFG'[::2]
print(s)

r = range(1, 5)
t = tuple(r)
l = list(s)
t = tuple(l)

print(r)
print(s)
print(l)
print(t)
