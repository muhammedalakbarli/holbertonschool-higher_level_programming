#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa.
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
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            user, passwd, db_name), pool_pre_ping=True
    )

    # 3. Create a configured "Session" class and instance
    Session = sessionmaker(bind=engine)
    session = Session()

    # 4. Query only the first State object, sorted by id
    first_state = session.query(State).order_by(State.id).first()

    # 5. Display results or "Nothing" if empty
    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")

    # 6. Close the session
    session.close()
