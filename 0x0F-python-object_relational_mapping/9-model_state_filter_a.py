#!/usr/bin/python3
"""script that lists all State objects that contain
    the letter a from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":

    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import Base, State

    engine = create_engine(
        f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}",
        pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)

    cont_as = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id).all()
    if cont_as:
        for item in cont_as:
            print("{}: {}".format(item.id, item.name))
    else:
        print()
