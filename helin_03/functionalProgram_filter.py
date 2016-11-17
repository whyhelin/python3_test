#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filter()也接收一个函数和一个序列。
# 和map()不同的是，
# filter()把传入的函数依次作用于每个元素，
# 然后根据返回值是True还是False决定保留还是丢弃该元素。


# 例如，在一个list中，删掉偶数，只保留奇数，可以这么写：
def is_odd(n):
    return n % 2 == 1

l = list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
print(l)
# 结果: [1, 5, 9, 15]


# 把一个序列中的空字符串删掉，可以这么写：
def not_empty(s):
    return s and s.strip()

l = list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
print(l)
# 结果: ['A', 'B', 'C']


# 注意这是一个生成器，并且是一个无限序列。
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


# 然后定义一个筛选函数：
def _not_divisible(n):
    return lambda x: x % n > 0


# 最后，定义一个生成器，不断返回下一个素数：
def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

# 这个生成器先返回第一个素数2，然后，利用filter()不断产生筛选后的新的序列。
# 由于primes()也是一个无限序列，所以调用时需要设置一个退出循环的条件：

# 打印1000以内的素数:
for n in primes():
    if n < 100:
        print(n)
    else:
        break


# 回文数
def is_palindrome(n):
    return int(str(n)[::-1]) == n

print(is_palindrome(1234321))
print(is_palindrome(123))

output = filter(is_palindrome, range(1, 1000))
print(list(output))

