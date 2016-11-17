#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

print('Test: 010-12345')
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.group(1), m.group(2))

t = '19:05:30'
print('Test:', t)
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:'
             r'(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:'
             r'(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m.groups())
print('------------------------------------')


email1 = re.compile(r'^(\w+\.\w+|\w+)(@)(\w+)(\.com)$')
m = email1.match('some_one@gmail.com')
print(m.group())
m = email1.match('bill.gates@microsoft.com')
print(m.group())

email2 = re.compile(r'^(<.*?>)\s+(?:\w|\d)+?@(?:\w|\d)+?\.\w+$')
m = email2.match('<Tom Paris> tom@voyager.org')
print(m.group())
