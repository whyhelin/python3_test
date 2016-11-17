#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from io import BytesIO

# StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。
# write to BytesIO:

f = BytesIO()
f.write(b'hello')
f.write(b' ')
f.write(b'world!')
print(f.getvalue())

# read from BytesIO:
data = '人闲桂花落，\n夜静春山空。\n月出惊山鸟，\n时鸣春涧中。'.encode('utf-8')
f = BytesIO(data)
for line in f.readlines():
    print(line)
    print(line.decode('utf-8').strip())

print('--------------------------------')

# read from BytesIO:
data = '人闲桂花落，\n夜静春山空。\n月出惊山鸟，\n时鸣春涧中。'.encode('utf-8')
f = BytesIO(data)
while True:
    s = f.readline()
    if s == b'':
        break
    print(s.decode('utf-8').strip())
print('----------------------------------------')

# read from BytesIO:
data = '人闲桂花落，\n夜静春山空。\n月出惊山鸟，\n时鸣春涧中。'.encode('utf-8')
f = BytesIO(data)
s = f.read()
print(s.decode('utf-8'))


