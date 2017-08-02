#-*- encoding:utf-8 -*-
from sqlalchemy import Column,Integer,String,DateTime,TEXT,ForeignKey
from database import Base
from werkzeug.security import check_password_hash,generate_password_hash

#2017-07-27实现用户操作的model
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer,primary_key=True,autoincrement=True,unique=True)
    name = Column(String(20),unique=True,nullable=True)
    password = Column(String(120),nullable=True)
    email = Column(String(120),nullable=True)

    def __init__(self,name,password,email):
        self.name = name
        self.set_password(password)
        self.email = email

    def set_password(self,password):
        self.password = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password,password)

    def __repr__(self):
        return "<User: %r >"%(self.name)


#2017-07-31实现日记记录的model
class Logger(Base):
    __tablename__ = 'logger'

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    title = Column(String(20), unique=False, nullable=True)
    forwho = Column(String(20), nullable=True)
    content = Column(TEXT, nullable=True)
    date = Column(DateTime,nullable=True)
    user = Column(Integer,ForeignKey('user.id'),nullable=False)

    def __init__(self, title, forwho, content,date):
        self.title = title
        self.forwho = forwho
        self.content = content
        self.date = date

    def __repr__(self):
        return "<User: %r >" % (self.title)