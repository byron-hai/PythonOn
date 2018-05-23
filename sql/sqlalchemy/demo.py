#!/usr/bin/env python
#coding:utf-8

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declaration import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
db_str_format = "mysql+mysqldb://{user}:{password}@{host}/{dbname}"
engine = create_engine(db_str_format('byron', '10023405', 'localhost', 'testdb'))

class Blog(Base):
    __tablename__ = 'blog'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), unique=True, nullable=False)
    author = Column(String(50), nullable=True)

Base.metadata.create_all(engine)

if __name__ == '__main__':
    Session = sessionmaker(bind=engine)
    session = SessionCls()

    blog1 = Blog(title='First', author='Gost')
    blog2 = Blog(title='Sleeping worm', author='Gost')
    blog3 = Blog(title='Camel', authoe='Gost')

    session.add_all([blog1, blog2, blog3])
    session.commit()
