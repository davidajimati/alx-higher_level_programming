#!/usr/bin/python3
"""
This module contains the class definition of a
State and an instance Base = declarative_base()
"""

from enum import unique
from sqlalchemy import Column, Integer, CHAR, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base


class State(Base):
    """Class States"""

    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, unique=True,
                primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
