#!/usr/bin/python3
"""Link class to table in database
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    # Create a MySQL database engine using command-line arguments
    # for username, password, and database name respectively
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    # Create all tables defined in the Base model in the connected database
    Base.metadata.create_all(engine)
