#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa
using SQLAlchemy.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # 1. Database connection details from arguments
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    # 2. Create the engine
    # Format: mysql+mysqldb://user:password@host:port/database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            user, passwd, db_name), pool_pre_ping=True
    )

    # 3. Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # 4. Create a session instance
    session = Session()

    # 5. Query all State objects, sorted by id
    states = session.query(State).order_by(State.id).all()

    # 6. Display results in the required format <id>: <name>
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # 7. Close the session
    session.close()
