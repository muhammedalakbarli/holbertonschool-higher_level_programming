#!/usr/bin/python3
"""
Changes the name of a State object where id = 2 to "New Mexico"
in the database hbtn_0e_6_usa.
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

    # 3. Query the specific State object by ID
    state_to_update = session.query(State).filter(State.id == 2).first()

    # 4. If the state exists, update the name and commit
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    # 5. Close session
    session.close()
