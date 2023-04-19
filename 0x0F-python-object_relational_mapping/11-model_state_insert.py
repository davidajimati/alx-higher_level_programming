#!/usr/bin/python3
"""script that adds the State object “Louisiana” to the
    database hbtn_0e_6_usa
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

    # check if the state already exists
    check = session.query(State).filter_by(name='Louisiana').first()

    if not check:
        new_state = State(name='Louisiana')
        session.add(new_state)
        session.commit()
        print(new_state.id)
