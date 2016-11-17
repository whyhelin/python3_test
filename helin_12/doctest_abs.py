#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def abs(n):
    '''
    >>> abs(1)
    1
    >>> abs(-1)
    1
    >>> abs(0)
    0
    '''
    return n if n >= 0 else (-n)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
