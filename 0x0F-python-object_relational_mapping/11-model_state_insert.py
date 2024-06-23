#!/usr/bin/python3
"""Module that adds State object “Louisiana” to the database
"""

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    username = sys.argv[1]
    password = sys.argv[2]
    dn_name = sys.argv[3]
    state_name = 'Louisiana'

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
    # Add entry to the database
    new_state = State(name=state_name)
    session.add(new_state)
    session.commit()
    # Query the database
    state = session.query(State).filter(State.name == state_name).first()
    print(f'{state.id}')
    # Close the session
    session.close()
