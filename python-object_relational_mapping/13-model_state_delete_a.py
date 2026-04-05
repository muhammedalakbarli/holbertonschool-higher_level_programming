#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # 1. Setup connection
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )

    # 2. Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # 3. Find and delete the states
    # synchronize_session='fetch' ensures the session is updated after delete
    session.query(State).filter(State.name.contains('a')).delete(
        synchronize_session='fetch'
    )

    # 4. Commit changes
    session.commit()

    # 5. Close session
    session.close()
