#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import struct

# Python提供了一个struct模块来解决bytes和其他二进制数据类型的转换。

# python 采用 unicode 编码
n = 10240099
b1 = (n & 0xff000000) >> 24
b2 = (n & 0xff0000) >> 16
b3 = (n & 0xff00) >> 8
b4 = n & 0xff
bs = bytes([b1, b2, b3, b4])
print(b1, b2, b3, b4)
print(chr(b1), chr(b2), chr(b3), chr(b4))
print(bs)
print('---------------------------------------')


# struct的pack函数把任意数据类型变成bytes：
# pack的第一个参数是处理指令，'>I'的意思是：
# >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
# 根据>IH的说明，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数。

b = struct.pack('>I', 10240099)
print(b)
i = struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')
print(i)

bmp_header = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
print(struct.unpack('<ccIIIIIIHH', bmp_header))
print('-------------------------------------------')


# 请编写一个bmpinfo.py，可以检查任意文件是否是位图文件，如果是，打印出图片大小和颜色数。
def testbmp(filepath):
    with open(filepath, 'rb') as f:
        bmp_header = f.read(30)
    b = struct.unpack('<ccIIIIIIHH', bmp_header)
    if b[:2] == (b'B', b'M') or b[:2] == (b'B', b'A'):
        print(str(b[2]/1024)+' kB'+'---'+str(b[6])+'*'+str(b[7])+'---'+str(b[9]))
    else:
        print('not bmp')


testbmp('cat.jpg')
testbmp('OSK.bmp')

