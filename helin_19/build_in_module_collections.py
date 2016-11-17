#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import deque, namedtuple, defaultdict, OrderedDict, Counter

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print('Point:', p.x, p.y)


q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)


dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print('dd[\'key1\'] =', dd['key1'])
print('dd[\'key2\'] =', dd['key2'])


c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)
print(Counter('programming'))


class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)  # 等价于super().__setitem__(self, key, value)

d = LastUpdatedOrderedDict(2)
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
print(d)


d = dict([('b', 1), ('a', 2), ('c', 3)])
print(d)
# 默认删除的是第一个
d.popitem()
print(d)

od = OrderedDict([('b', 1), ('a', 2), ('c', 3)])
print(od)
# last属性表示从哪一头开始删除
od.popitem(last=True)
print(od)
