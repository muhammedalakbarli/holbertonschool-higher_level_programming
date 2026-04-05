#!/usr/bin/python3
"""
Adds the State object "Louisiana" to the database hbtn_0e_6_usa.
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

    # 3. Create a new State object
    new_state = State(name="Louisiana")

    # 4. Add to session and commit to the database
    session.add(new_state)
    session.commit()

    # 5. Print the new states.id
    # SQLAlchemy automatically refreshes the object with the new ID from MySQL
    print("{}".format(new_state.id))

    # 6. Close session
    session.close()
