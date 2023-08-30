#!/usr/bin/python3
""" This file contains the class definition of state"""
import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.decorative import declarative_base
Base = declarative_base()


class State(Base):
    """ This state class inherits from the Base class

        Args:
            Base (imported class): [imported class]"""

    __tablename__ = 'states'

    id = Column(Integer, primay_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)


engine = sqlalchemy.create_engine('mysql+pymysql://root@localhost:3306/test')
Base.metadata.create_all(engine)
