#!/usr/bin/python3
"""Module that lists all State objects, and
corresponding City objects, contained in the
database hbtn_0e_101_usa.
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

    states = session.query(State).order_by(State.id).all()

    if not states:
        print("No states found.")
    else:
        for state in states:
            print(f"{state.id}: {state.name}")
            for city in state.cities:
                print(f"\t{city.id}: {city.name}")

    # Close the session
    session.close()
