#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime

from PIL import Image

f = open('./test.txt', 'r', encoding='utf-8')
s = f.read()
print(s)
f.close()

# ---------------------------------------------
try:
    f = open('/path/to/file', 'r')
    print(f.read())
except FileNotFoundError as e:
    print(e)
finally:
    if f:
        f.close()

# 这和前面的try ... finally是一样的，
# 但是代码更佳简洁，并且不必调用f.close()方法。
with open('test.txt', 'w', encoding='utf-8') as f:
    f.write('今天是 ')
    f.write(datetime.now().strftime('%Y-%m-%d'))

with open('test.txt', 'r', encoding='utf-8') as f:
    s = f.read()
    print('open for read...')
    print(s)

with open('test.txt', 'r', encoding='utf-8') as f:
    s = f.read()
    print('open as binary for read...')
    print(s)

# 调用read()会一次性读取文件的全部内容，
# 如果文件有10G，内存就爆了，
# 所以，要保险起见，可以反复调用read(size)方法，
# 每次最多读取size个字节的内容。
# 另外，调用readline()可以每次读取一行内容，
# 调用readlines()一次读取所有内容并按行返回list。
# 因此，要根据需要决定怎么调用。


# 传入标识符'w'或者'wb'表示写文本文件或写二进制文件：
with open('test.txt', 'a', encoding='utf-8') as f:
    f.write('\n')
    f.write('hello')
    f.write('\n')
    f.write('world')

with open('test.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        print(line.strip())  # 把末尾的'\n'删掉


print('-----------------------------')
with open('test.txt', 'r', encoding='utf-8') as f:
    while True:
        line = f.readline()
        if line == '':
            break
        print(line.strip())
print('-------------------------------------')

with open('test.txt', 'r', encoding='utf-8', errors='ignore') as f:
    s = f.read()
    print(s)
    print(f.name)


print('---------------------------------------')
with open('cat.jpg', 'rb') as f:
    while True:
        line = f.readline()
        if line == b'':
            break
        print(line.strip())
print('-------------------------------------')


with open('cat.jpg', 'rb') as f:
    s = f.read()
    print(s)
    with open('catcopy.jpg', 'wb') as p:
        p.write(s)
        im = Image.open(p.name)
        print(im.format, im.size, im.mode)
        im.rotate(45).show()
        im.thumbnail((200, 100))
        im.save('thumb.jpg', 'JPEG')

