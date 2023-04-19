#!/usr/bin/python3
"""script that lists all State objects from
    the database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State, Base

    u_name = argv[1]
    pwd = argv[2]
    db_name = argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{u_name}:{pwd}\
            @localhost:3306/{db_name}", pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id.asc()).all()
    for state in states:
        print(state)
