#-*- encoding:utf-8 -*-
'''
使用flask_sqlalchemy实现一个日记本功能
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql://root:steven@localhost:3306/flasky?charset=utf8mb4',convert_unicode=True)

db_session = scoped_session(sessionmaker(
                            autocommit=False,
                            autoflush=False,
                            bind=engine))

Base = declarative_base()

Base.query = db_session.query_property()

def init_db():
    #这里导入所有的model,以便于生成数据库
    import models
    Base.metadata.create_all(bind=engine)