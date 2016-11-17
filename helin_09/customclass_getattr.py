#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Python还有另一个机制，那就是写一个__getattr__()方法，动态返回一个属性

# 注意，只有在没有找到属性的情况下，才调用__getattr__，
# 已有的属性，比如name，不会在__getattr__中查找。
# 此外，注意到任意调用如s.abc都会返回None，
# 这是因为我们定义的__getattr__默认返回就是None。
class Student(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

s = Student()
print(s.name)
print(s.score)
print(s.age())
# AttributeError: 'Student' object has no attribute 'grade'
print(s.grade)
