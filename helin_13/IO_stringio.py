#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from io import StringIO

# StringIO顾名思义就是在内存中读写str
# write to StringIO:
f = StringIO('aa')
f.write('hello')
f.write(' ')
f.write('world!')
f.write('你好')
print(f.getvalue())

g = StringIO(f.getvalue())
while True:
    s = g.readline()
    if s == '':
        break
    print(s.strip())


# read from StringIO:
f = StringIO('水面细风生，\n菱歌慢慢声。\n客亭临小市，\n灯火夜妆明。')
g = StringIO()
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
    g.write(s)

print(g.getvalue())
