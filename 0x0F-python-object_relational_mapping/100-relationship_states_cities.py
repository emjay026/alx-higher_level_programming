#!/usr/bin/env python3
"""Module that adds State object “Louisiana” to the database
"""

if __name__ == "__main__":
    import sys
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    username = sys.argv[1]
    password = sys.argv[2]
    dn_name = sys.argv[3]
    port = 3306

    # Create a MySQL database engine using command-line arguments
    # for username, password, and database name respectively
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:{}/{}'.
                           format(username, password, port, dn_name),
                           pool_pre_ping=True)
    # Create all tables defined in the Base model in the connected database
    Base.metadata.create_all(engine)
    # Create a sessionmaker to interact with the database
    Session = sessionmaker(bind=engine)
    # Create a new session
    session = Session()

    state = State(name="California")
    city = City(name="San Francisco", state=state)

    session.add(state)

    # states = session.query(State).all()
    # for state in states:
    #     session.delete(state)

    # Commit changes to database
    session.commit()
    # Close the session
    session.close()
