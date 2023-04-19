#!/usr/bin/python3

'''
This module implements the solution
importing from the model state
'''
from model_state import State, Base
from sys import argv
from sqlalchemy import create_engine

if __name__ == "__main__":
    '''
    Below: specifies the url and the command to create the engine
    '''
    engine = create_engine(
        'mysql://{}:{}@localhost:3306/{}'.format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
