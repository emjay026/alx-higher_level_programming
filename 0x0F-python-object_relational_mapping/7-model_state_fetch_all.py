#!/usr/bin/env python3
"""Lists all State objects from the database
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

username = sys.argv[1]
password = sys.argv[2]
dn_name = sys.argv[3]
port = 3306

if __name__ == "__main__":
    # Create a MySQL database engine using command-line arguments
    # for username, password, and database name respectively
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:{}/{}'.
                           format(username, password, port, dn_name),
                           pool_pre_ping=True)

    # Create all tables defined in the Base model in the connected database
    Base.metadata.create_all(engine)
    # Create all tables defined in the Base model in the connected database
    Base.metadata.create_all(engine)
    # Create a sessionmaker to interact with the database
    Session = sessionmaker(bind=engine)
    # Create a new session
    session = Session()
    # Query the database
    all_users = session.query(State).order_by(State.id).all()
    for user in all_users:
        print(f'{user.id}: {user.name}')
