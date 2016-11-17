#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from types import MethodType


# 正常情况下，当我们定义了一个class，创建了一个class的实例后，
# 我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。
class Student(object):
    pass

s = Student()
s.name = 'Michael'  # 动态给实例绑定一个属性
print(s.name)


# 还可以尝试给实例绑定一个方法：
def set_age(self, age):
    self.age = age

s.set_age = MethodType(set_age, s)  # 给实例绑定一个方法，直接如下赋值不行
# s.set_age = set_age
s.set_age(25)
print(s.age)


# 但是，给一个实例绑定的方法，对另一个实例是不起作用的：
s2 = Student()
# s2.set_age(25)


# 为了给所有实例都绑定方法，可以给class绑定方法：
def set_score(self, score):
    self.score = score

Student.set_score = set_score

s.set_score(100)
print(s.score)

s2.set_score(99)
print(s2.score)
print('-------------------------------')


# Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性
# 由于'score'没有被放到__slots__中，所以不能绑定score属性，
# 试图绑定score将得到AttributeError的错误。

# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，
# 对继承的子类是不起作用的：
class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


class GraduateStudent(Student):
    pass

s = Student()
s.name = 'Michael'
s.age = 25
# s.score = 99

g = GraduateStudent()
g.score = 99
print('g.score =', g.score)
