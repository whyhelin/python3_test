#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import MetaData
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker


# 初始化数据连接,create_engine()用来初始化数据库连接
# SQLAlchemy用一个字符串表示连接信息：'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/test_python')

# 创建元数据
metadata = MetaData(engine)

# 创建表
c = Table('classroom', metadata,
      Column('id', String(20), primary_key=True),
      Column('name', String(20)),
      mysql_engine='InnoDB',
      mysql_charset='utf8',
      mysql_key_block_size="1024"
     )
t = Table('teacher', metadata,
      Column('id', String(20), primary_key=True),
      Column('name', String(20)),
      Column('subject', String(20)),
      Column('class_id', String(20)),
      mysql_engine='InnoDB',
      mysql_charset='utf8',
      mysql_key_block_size="1024"
     )
metadata.create_all()

# 创建对象基类
Base = declarative_base()


# 班级
class Classroom(Base):
    __tablename__ = 'classroom'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # 一对多
    teacher = relationship('Teacher')

    def __repr__(self):
        return '<User: (id: %s, name: %s, teacher: %s)>' % (self.id, self.name, self.teacher)


class Teacher(Base):
    __tablename__ = 'teacher'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    subject = Column(String(20))

    # "多"的一方teacher表是通过外键关联到class表
    class_id = Column(String(20), ForeignKey('classroom.id'))

    def __repr__(self):
        return '<Teacher: (id: %s, name: %s, subject: %s, class_id: %s)>' % (self.id, self.name, self.subject, self.class_id)


# 多次插入方式
def insert_multiple():
    new_class = Classroom(id='1', name='三年二班')
    session.add(new_class)
    session.commit()

    math_teacher = Teacher(id='1', name='李志', class_id='1', subject='数学')
    chiese_teacher = Teacher(id='2', name='赵雷', class_id='1', subject='语文')
    session.add_all([math_teacher, chiese_teacher])
    session.commit()


# 一次插入方式
def insert_once():
    math_teacher = Teacher(id='1', name='李志', class_id='1', subject='数学')
    chiese_teacher = Teacher(id='2', name='赵雷', class_id='1', subject='语文')
    new_class = Classroom(id='1', name='三年二班', teacher=[math_teacher, chiese_teacher])
    session.add(new_class)
    session.commit()


DBsession = sessionmaker(bind=engine)
session = DBsession()

insert_once()

result = session.query(Classroom).filter(Classroom.id == '1').all()
print(result)

session.close()

