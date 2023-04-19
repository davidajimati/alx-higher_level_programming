#!/usr/bin/python3
"""
 script that lists all State objects, and corresponding
    City objects, contained in the database hbtn_0e_101_usa
"""

if __name__ == "__main__":

    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from relationship_city import City, Base
    from relationship_state import State, Base

    engine = create_engine(
        f"mysql://{argv[1]}:{argv[2]}@localhost/{argv[3]}",
        pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = Session(engine)

    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"\t{city.id}: {city.name}")
