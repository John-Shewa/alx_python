#!/usr/bin/python3
""" This file contains the class definition of 
"state" and an instance "Base" """
import sqlalchemy
from sqlalchemy.ext.decorative import declarative_base

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'

    id = sqlalchemy.Column(
        sqlalchemy.Integer, primay_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String(128), nullable=False)


engine = sqlalchemy.create_engine('mysql+pymysql://root@localhost:3306/test')
Base.metadata.create_all(engine)
