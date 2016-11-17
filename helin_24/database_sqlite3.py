#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sqlite3

# SQLite是一种嵌入式数据库，它的数据库就是一个文件。
# 由于SQLite本身是C写的，而且体积很小，所以，经常被集成到各种应用程序中，甚至在iOS和Android的App中都可以集成。
# Python就内置了SQLite3，所以，在Python中使用SQLite，不需要安装任何东西，直接使用。


# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建:
conn = sqlite3.connect('test.db')

# 创建一个Cursor:
cursor = conn.cursor()

# 执行一条SQL语句，创建user表:
cursor.execute('create table IF NOT EXISTS user (id varchar(20) primary key, name varchar(20))')
# 继续执行一条SQL语句，插入一条记录:
cursor.execute('insert or IGNORE into user (id, name) values (\'1\', \'Michael\')')

# 通过rowcount获得插入的行数:
print('rowcount =', cursor.rowcount)

# 关闭Cursor:
cursor.close()

# 提交事务:
conn.commit()

# 关闭Connection:
conn.close()

# 查询记录：
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# 执行查询语句:
# cursor.execute('select * from user where name=? and pwd=?', ('abc', 'password'))
# cursor.execute('select * from user where id=?', '1')
cursor.execute('select * from user')

# 获得查询结果集:
values = cursor.fetchall()
print(values)

cursor.close()
conn.close()


print('--------------------------------------------')
db_file = os.path.join(os.path.dirname(__file__), 'test1.db')
if os.path.isfile(db_file):
    os.remove(db_file)

# 初始数据:
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table IF NOT EXISTS user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert or IGNORE into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert or IGNORE into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert or IGNORE into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()


def get_score_in(low, high):
    ' 返回指定分数区间的名字，按分数从低到高排序 '
    conn = sqlite3.connect('test1.db')
    cursor = conn.cursor()
    cursor.execute('select * from user where score >=? and score <=? order by score', (low, high))
    values = cursor.fetchall()
    print(values)
    cursor.close()
    conn.close()

    return [x[1] for x in values]

# 测试:
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

print('Pass')


