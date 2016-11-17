#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Animal(object):
    def run(self):
        print('Animal is running...')


class Timer(object):
    def run(self):
        print('Start...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


def run_twice(animal):
    animal.run()
    animal.run()

a = Animal()
d = Dog()
c = Cat()

print('a is Animal?', isinstance(a, Animal))
print('a is Dog?', isinstance(a, Dog))
print('a is Cat?', isinstance(a, Cat))

print('d is Animal?', isinstance(d, Animal))
print('d is Dog?', isinstance(d, Dog))
print('d is Cat?', isinstance(d, Cat))


# 对于静态语言（例如Java）来说，
# 如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，
# 否则，将无法调用run()方法。
#
# 对于Python这样的动态语言来说，则不一定需要传入Animal类型。
# 我们只需要保证传入的对象有一个run()方法就可以了：
# 这就是动态语言的“鸭子类型”，
# 它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，
# 那它就可以被看做是鸭子。
# Python的“file-like object“就是一种鸭子类型。
# 对真正的文件对象，它有一个read()方法，返回其内容。
# 但是，许多对象，只要有read()方法，都被视为“file-like object“。
# 许多函数接收的参数就是“file-like object“，
# 你不一定要传入真正的文件对象，完全可以传入任何实现了read()方法的对象。


run_twice(c)
run_twice(Timer())