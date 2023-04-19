#!/usr/bin/python3
"""
This module contains the class definition of a
State and an instance Base = declarative_base()
"""

from enum import unique
from sys import argv
from sqlalchemy import Column, Integer, CHAR, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base


class State(Base):
    """
    Class States - the class that the objects belong to
    """

    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, unique=True,
                primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)


engine = create_engine(
    'mysql://{}:{}@localhost:3306/{}'.format(argv[1], argv[2], argv[3]))
Base.metadata.create_all(engine)
