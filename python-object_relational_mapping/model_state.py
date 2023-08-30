#!/usr/bin/python3
""" This file contains the class definition of state"""
import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.decorative import declarative_base
Base = declarative_base()


class State(Base):
    """ This class represents a state in a mysql database.
        Attributes:
            id: An integer that is used as the primary keyfor the table.
            name: A string that represents the name of the state. """

    __tablename__ = 'states'

    id = Column(Integer, primay_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)


engine = sqlalchemy.create_engine('mysql+pymysql://root@localhost:3306/test')
Base.metadata.create_all(engine)
