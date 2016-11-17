#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base64

# Base64是一种任意二进制到文本字符串的编码方法，
# 常用于在URL、Cookie、网页中传输少量二进制数据。
# 参数类型为bytes

s = base64.b64encode(b'binary\x00string')
print(s)
d = base64.b64decode(b'YmluYXJ5AHN0cmluZw==')
print(d)

s = base64.b64encode('在Python中使用BASE 64编码'.encode('utf-8'))
print(s)
d = base64.b64decode(s).decode('utf-8')
print(d)

s = base64.urlsafe_b64encode('在Python中使用BASE 64编码'.encode('utf-8'))
print(s)
d = base64.urlsafe_b64decode(s).decode('utf-8')
print(d)
print('---------------------------------------------')


def safe_base64_decode(s):
    s = s.encode('utf-8') if not isinstance(s, bytes) else s
    print(s)
    while len(s) % 4 != 0:
        s = s + b'='
    print(s)
    return base64.b64decode(s)

assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('Pass')

