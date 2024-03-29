#!/usr/bin/python3
"""script that deletes all State objects with a name
    containing the letter a from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import Base, State

    engine = create_engine(
        f"mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}",
        pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)

    cont_as = session.query(State).filter(
        State.name.like('%a%')).all()

    if cont_as:
        for item in cont_as:
            session.delete(item)
        session.commit()
        session.close()
