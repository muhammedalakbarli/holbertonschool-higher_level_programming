#!/usr/bin/python3
"""
Lists all State objects that contain the letter 'a'
from the database hbtn_0e_6_usa.
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

    # 3. Create a configured Session class and instance
    Session = sessionmaker(bind=engine)
    session = Session()

    # 4. Query State objects containing the letter 'a'
    # .contains('a') translates to LIKE '%a%' in SQL
    states_with_a = session.query(State).filter(
        State.name.contains('a')
    ).order_by(State.id).all()

    # 5. Display results in the required format <id>: <name>
    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

    # 6. Close the session
    session.close()
