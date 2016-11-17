#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json


# 由于JSON标准规定JSON编码是UTF-8，所以我们总是能正确地在Python的str与JSON的字符串之间转换。
d = dict(name='Bob', age=20, score=88)
data = json.dumps(d)
print(isinstance(data, str))
print('JSON Data is a str:', data)
reborn = json.loads(data)
print(reborn)
print(isinstance(reborn, dict))

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str))
print('-----------------------------')


class Student(object):

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return 'Student object (%s, %s, %s)' % (self.name, self.age, self.score)

s = Student('Bob', 20, 88)
std_data = json.dumps(s, default=lambda obj: obj.__dict__)
print('Dump Student:', std_data)

rebuild = json.loads(std_data, object_hook=lambda d: Student(d['name'], d['age'], d['score']))
print(rebuild)
print('----------------------------')


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

s = Student('Bob', 20, 88)
std_data = json.dumps(s, default=student2dict)
print('Dump Student:', std_data)
print(isinstance(std_data, str))

rebuild = json.loads(std_data, object_hook=dict2student)
print(rebuild)
print(isinstance(rebuild, Student))


