#!/usr/bin/python3
"""script that lists all City objects from the
    database hbtn_0e_101_usa
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

    cities = session.query(City).order_by(City.id.asc()).all()
    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")
