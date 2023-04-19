#!/usr/bin/python3
"""script that prints the State object with the
    name passed as argument from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import Base, State

    engine = create_engine(
        f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}",
        pool_pre_ping=True)

    target = argv[4]
    Base.metadata.create_all(engine)
    session = Session(engine)

    state = session.query(State).filter_by(State.name.like(target)).all()
    if (state):
        for i in state:
            print(i.id)
    else:
        print("Not found")
