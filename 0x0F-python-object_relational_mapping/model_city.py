#!/usr/bin/python3
"""python file that contains the class definition of
a city and an instance Base = declarative_base()"""

from enum import unique
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Class city"""

    __tablename__ = 'cities'
    id = Column("id", Integer, autoincrement=True,
                primary_key=True, nullable=False, unique=True)

    name = Column("name", String(128), nullable=False)
    state_id = Column("state_id", Integer, ForeignKey(
        'states.id'), nullable=False)
