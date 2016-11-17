#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from contextlib import contextmanager, closing
from urllib.request import urlopen

# 并不是只有open()函数返回的fp对象才能使用with语句。
# 实际上，任何对象，只要正确实现了上下文管理，就可以用于with语句。
# 实现上下文管理是通过__enter__和__exit__这两个方法实现的


class Query(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Begin')
        return self

# exc_type,exc_value,traceback 正常情况下都是 None
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s...' % self.name)

with Query('tim') as q:
    q.query()

print('--------------------------------------')


class Query(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)


@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')

with create_query('tim') as q:
    q.query()


# 很多时候，我们希望在某段代码执行前后自动执行特定代码，也可以用@contextmanager实现。
@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

with tag("h1"):
    print("hello")
    print("world")

print('-----------------------------------')

# 如果一个对象没有实现上下文，我们就不能把它用于with语句。这个时候，可以用closing()来把该对象变为上下文对象
with closing(urlopen('https://www.baidu.com')) as page:
    for line in page:
        print(line)
print('---------------------------')

s = urlopen('https://www.baidu.com')
for line in s:
    print(line)
print('----------------------------')

with urlopen('https://www.baidu.com') as f:
    s = f.read().decode('utf-8')
print(s)

