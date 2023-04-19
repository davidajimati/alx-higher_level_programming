#!/usr/bin/python3
"""script that prints the first State
    object from the database hbtn_0e_6_usa
"""


if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from model_state import Base, State
    from sqlalchemy.orm import Session

    engine = create_engine(
        f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}",
        pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = Session(engine)

    state = session.query(State).first()
    print("{}: {}".format(state.id, state.name))
    # print(state)
