#!/usr/bin/python3
"""Module that lists all State objects that contain the letter a
"""

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    username = sys.argv[1]
    password = sys.argv[2]
    dn_name = sys.argv[3]

    # Create a MySQL database engine using command-line arguments
    # for username, password, and database name respectively
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(username, password, dn_name),
                           pool_pre_ping=True)
    # Create all tables defined in the Base model in the connected database
    Base.metadata.create_all(engine)
    # Create a sessionmaker to interact with the database
    Session = sessionmaker(bind=engine)
    # Create a new session
    session = Session()
    # Query the database
    states = session.query(State).filter(State.name.like('%a%')).\
        order_by(State.id).all()
    for state in states:
        print(f'{state.id}: {state.name}')
    # Close the session
    session.close()
