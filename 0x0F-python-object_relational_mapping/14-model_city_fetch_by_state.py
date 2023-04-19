#!/usr/bin/python3
"""script that prints all City objects from the
    database hbtn_0e_14_usa
"""

if __name__ == "__main__":

    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_city import City, Base
    from model_state import State, Base

    engine = create_engine(
        f"mysql://{argv[1]}:{argv[2]}@localhost/{argv[3]}",
        pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = Session(engine)

    results = session.query(State.name, City.id, City.name).filter(
        State.id == City.state_id).all()

    for state_name, city_id, city_name in results:
        print("{}: ({}) {}".format(state_name, city_id, city_name))
