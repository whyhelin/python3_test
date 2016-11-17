#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('I\' ok')
print('I\'m learning\nPython.')
print('\\\n\\')

# 如果字符串里面有很多字符都需要转义，就需要加很多\，为了简化，Python还允许用r''表示''内部的字符串默认不转义
print('\\\t\\')
print(r'\\\t\\')

print('''line1
line2
line3''')

print(10/3)
print(10//3)

# n = 123
# f = 456.789
# s1 = 'Hello, world'
# s2 = 'Hello, \'Adam\''
# s3 = r'Hello, "Bart"'
# s4 = r'''Hello,
# Lisa!'''
print("'Hello, world'")
print("'Hello,", r'\'Adam\''"'")
print(r"r'Hello,", "\"Bart\"'")
print("r'''Hello,")
print("Lisa!'''")

# 在最新的Python 3版本中，字符串是以Unicode编码的，也就是说，Python的字符串支持多语言
print('包含中文的str')

# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
print(ord('A'))
print(ord('中'))
print(chr(65))
print(chr(25991))
print('\u4e2d\u6587')

# Python对bytes类型的数据用带b前缀的单引号或双引号表示：
x = b'ABC'
print(x)
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
# print('中文'.encode('ascii'))

# 要把bytes变为str，就需要用decode()方法
print(b'ABC'.decode('ascii'))
print(b'ABC'.decode('ascii'))

print(len('ABC'))
print(len('中文'))
print(len(b'ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8')))

print('Hello, %s' % 'world')
print('Hi, %s, you have $%d.' % ('Michael', 1000000))
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
print('Age: %s. Gender: %s' % (25, True))
print('growth rate: %d %%' % 7)

# 动态数据类型
x = 1
print(x)
x = 'aa'
print(x)

# Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
classmates = ['Michael', 'Bob', 'Tracy']
classmates[0]='aa'
print('classmates =', classmates)
print('len(classmates) =', len(classmates))
print('classmates[0] =', classmates[0])
print('classmates[1] =', classmates[1])
print('classmates[2] =', classmates[2])
print('classmates[-1] =', classmates[-1])
classmates.pop()
print('classmates =', classmates)
classmates.pop(1)
print('classmates =', classmates)
classmates.insert(1,'helin')
print('classmates =', classmates)

s = ['python', 'java', ['asp', 'php'], 'scheme']
print(s)

# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
classmates = ('Michael', 'Bob', 'Tracy')
# classmates[0]='aa'
print(classmates)
# 只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
t = (1)
print(t)
t = (1,)
print(t)


age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')


age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')


# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
x = 0
if x:
    print('True')
else:
    print('False')


s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')


sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

sum = 0
nums = [1, 2, 3, 4, 5]
for x in nums:
    sum = sum + x
print(sum)

sum = 0
for x in range(101):
    sum = sum + x
print(sum)

sum = 0
for x in list(range(101)):
    sum = sum + x
print(sum)

print(range(5))
print(list(range(5)))
print('-----------------------------')

# Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度
d = {
    'Michael': 95,
    'Bob': 75,
    'Tracy': 85
}
print(d)
print('d[\'Michael\'] =', d['Michael'])
print('d[\'Bob\'] =', d['Bob'])
print('d[\'Tracy\'] =', d['Tracy'])
print('d.get(\'Thomas\', -1) =', d.get('Thomas', -1))

d['M'] = 95
d['N'] = 75
d['N'] = 90
print('N' in d)
print('d[\'M\'] =', d['M'])
print('d[\'N\'] =', d['N'])

# 要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key：
# key = [1, 2]
# d[key] = 90
key = (1, 2)
d[key] = 90
print(d)

# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
# 要创建一个set，需要提供一个list作为输入集合：
s = set([1, 1, 2, 3])
print(s)

s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)

key = [1, 2]
s = set(key)
print(s)

key = (1, 2)
s = set(key)
print(1 in s)
print(s)
for n in s:
    print(n)




d = dict({"1": 2})
print(d['1'])


d = {"1": 2}
print(d['1'])


d = {1: 2}
print(d)


c = dict(one=1, two=2, three=3)
print(c['one'])


c = dict(one=1, two=2)
print(c['one'])
c[4] = 5
print(c[4])

# 不能用数字起始的做参数名
# c = dict(one=1, two=2, 4=3)