#!/usr/bin/python3
"""Module that changes the name of a State object from the database
"""

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    username = sys.argv[1]
    password = sys.argv[2]
    dn_name = sys.argv[3]
    new_name = 'New Mexico'
    state_id = 2

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
    state = session.query(State).filter(State.id == state_id).first()
    # Modify the returned row object
    if state:
        state.name = new_name
        # Commit changes to database
        session.commit()
    # Close the session
    session.close()
