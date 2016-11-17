#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import MetaData
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/test_python')

# 创建元数据
metadata = MetaData(engine)

# 创建表
t = Table('user2', metadata,
      Column('id', Integer, primary_key=True, autoincrement=True),
      Column('name', String(20)),
      mysql_engine='InnoDB',
      mysql_charset='utf8',
      mysql_key_block_size="1024"
     )
metadata.create_all()

# 创建对象的基类:
Base = declarative_base()


# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user2'

    # 表的结构:
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建session对象:
session = DBSession()

# 创建新User对象:
new_user = User(name='Bob')

# 添加到session:
session.add(new_user)

# 提交即保存到数据库:
session.commit()

# 关闭session:
session.close()

# 创建Session:
session = DBSession()

# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id == 1).one()

# 打印类型和对象的name属性:
print('type:', type(user))
print('name:', user.name)

# eg2 via sql
sql = text("select * from user2")
res = session.execute(sql).fetchall()

for row in res:
    for col in row:
        print(col)
    print('----')

# 关闭Session:
session.close()

