#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 通过列表生成式，我们可以直接创建一个列表。
# 但是，受到内存限制，列表容量肯定是有限的。
# 而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，
# 如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。
# 所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
# 这样就不必创建完整的list，从而节省大量的空间。
# 在Python中，这种一边循环一边计算的机制，称为生成器：generator。
# 要创建一个generator，有很多种方法。
# 第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
l = [x * x for x in range(10)]
print(l)


g = (x * x for x in range(10))
print(g)
print(list(g))

g = (x * x for x in range(10))
next(g)
next(g)
next(g)
next(g)
for i in g:
    print(i)


# 这就是定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

fib(6)
print(fib(6))
for n in fib(6):
    print(n)


def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

print(fib2(6))
g = fib2(6)
print(next(g))
print(next(g))
print(next(g))

# 没有返回 return 值
for n in fib2(6):
    print(n)

# 但是用for循环调用generator时，发现拿不到generator的return语句的返回值。
# 如果想要拿到返回值，必须捕获StopIteration错误，
# 返回值包含在StopIteration的value中：
g = fib2(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
       print('Generator return value:', e.value)
       break


# 杨辉三角
def triangles():
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [L[m-1] + L[m] for m in range(len(L))]


def triangles2():
    L = [0, 1, 0]
    while True:
        yield L[1:-1]
        for i in range(len(L) - 1):
            L.append(L.pop(0) + L[0])  # 弹出队首元素并将其与当前队首元素之和加入到队尾
        L.append(0)  # 加个0，帮队列推一下屁股，凑成标准体位。

n = 0
for t in triangles2():
    print(t)
    n = n + 1
    if n == 10:
        break


