#!/usr/bin/python3
"""script that lists all State objects from
    the database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.ext.declarative import declarative_base

    from model_state import State, Base
