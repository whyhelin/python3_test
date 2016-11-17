#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def now():
    print('2015-3-25')
    return 1

now()
print(now())
print(now.__name__)


def logger(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@logger('DEBUG')
def today():
    print('2015-3-25')

today()
print(today.__name__)
print('--------------')


def testlog(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call begin')
        res = func(*args, **kw)
        print('call end')
        return res
    return wrapper


@testlog
def now():
    print('2015-3-25')
    return 1

now()
print(now())
print('-------------')


def f1(fc):
    def f1s(*args, **kwargs):
        print('Running function:', fc.__name__)
        print('Positional argument:', args)
        print('Keyword argument:', kwargs)
        result = fc(*args, **kwargs)
        print('Result:', result)
        return result
    return f1s


def f2(func):
    def f2s(*args, **kwargs):
        results = func(*args, **kwargs)
        print('Results:', results)
        return results * results
    return f2s


@f2
@f1
def add_ints(a, b):
    return a + b

print(add_ints(3, 5))
print('------------------')


def log(text):
    func = text
    print(dir(func))
    if callable(func):
    # if hasattr(func, '__call__'):
        print(getattr(func, '__call__'))
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print("begin call1")
            f = func(*args, **kw)
            print("end call1")
            return f
        return wrapper
    else:
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print("begin call2 %s" % text)
                f = func(*args, **kw)
                print("end call2 %s" % text)
                return f
            return wrapper
        return decorator


@log
def text():
    print("text")

text()


@log("text")
def text():
    print("text")

text()


