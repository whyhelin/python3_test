#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pdb
import logging
logging.basicConfig(level=logging.INFO)


# -----------------断言--------------------------
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n


def main():
    foo('0')

# main()


# -----------------logging--------------------------
s = '0'
n = int(s)
logging.info('n = %d' % n)
# print(10 / n)


# -----------------pdb--------------------------
s = '0'
n = int(s)
pdb.set_trace()  # 运行到这里会自动暂停
print(10 / n)
