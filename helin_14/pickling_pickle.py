#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pickle


# 我们把变量从内存中变成可存储或传输的过程称之为序列化，
# 在Python中叫pickling，
# 在其他语言中也被称之为serialization，marshalling，flattening等等，
# 都是一个意思。
# 序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
# 反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。
# Python提供了pickle模块来实现序列化。

d = dict(name='Bob', age=20, score=88)
data = pickle.dumps(d)
print(data)
print(isinstance(data, bytes))

reborn = pickle.loads(data)
print(reborn)
print(isinstance(reborn, dict))
print('--------------------------------')

with open('dump.txt', 'wb') as f:
    pickle.dump(d, f)

with open('dump.txt', 'rb') as f:
    re = pickle.load(f)
    print(re)

