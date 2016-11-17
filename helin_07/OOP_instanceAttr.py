#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 如果Student类本身需要绑定一个属性呢？可以直接在class中定义属性，这种属性是类属性，归Student类所有
class Student(object):
    name = 'Student'

s = Student()  # 创建实例s
m = Student()
print(m.name)
print(s.name)  # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
print(Student.name)  # 打印类的name属性
print('----------------------------')


s.name = 'Michael'  # 给实例绑定name属性
print(s.name)  # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
print(m.name)
print(Student.name)  # 但是类属性并未消失，用Student.name仍然可以访问
print('----------------------------------')


Student.name = 'helin'
print(s.name)  # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
print(m.name)
print(Student.name)  # 但是类属性并未消失，用Student.name仍然可以访问
print('-------------------------------------')


del s.name  # 如果删除实例的name属性
print(s.name)  # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了


# 从上面的例子可以看出，
# 在编写程序的时候，千万不要把实例属性和类属性使用相同的名字，
# 因为相同名称的实例属性将屏蔽掉类属性，
# 但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。
