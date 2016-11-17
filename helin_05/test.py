#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from helin_05 import hello
from helin_05.hello import greeting, test, _private_1, __private_2, Animal

test()
print(greeting('he'))
print(greeting('helin'))
print(_private_1('he'))
print(__private_2('he'))


hello.test()
Animal.show_static()
Animal().show_static()
Animal().show()
