#-*- encoding:utf-8 -*-
from sqlalchemy import Column,Integer,String
from database import Base
from werkzeug.security import check_password_hash,generate_password_hash

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