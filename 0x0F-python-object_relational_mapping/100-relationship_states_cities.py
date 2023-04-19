#!/usr/bin/python3
"""
script that creates the State “California” with the City
    “San Francisco” from the database hbtn_0e_100_usa:
    (100-relationship_states_cities.py)
"""

if __name__ == "__main__":

    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from relationship_city import Base, City
    from relationship_state import Base, State
    from sqlalchemy.schema import Table

    engine = create_engine(
        f"mysql://{argv[1]}:{argv[2]}@localhost/{argv[3]}",
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)

    new_city = City(name='San Francisco')
    new = State(name='California')

    new.cities.append(new_city)
    session.add_all([new, new_city])
    session.commit()
    session.close()
