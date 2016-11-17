#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from mysql import connector

# change root password to yours:
conn = connector.connect(user='root', password='root', database='test_python')

cursor = conn.cursor()

# 创建user表:
cursor.execute('create table if not exists user (id int unsigned primary key auto_increment, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into user (name) values (%s)', ('Michael',))

print('rowcount =', cursor.rowcount)

# 提交事务:
conn.commit()
cursor.close()

# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))

values = cursor.fetchall()
print(values)

# 关闭Cursor和Connection:
cursor.close()
conn.close()

