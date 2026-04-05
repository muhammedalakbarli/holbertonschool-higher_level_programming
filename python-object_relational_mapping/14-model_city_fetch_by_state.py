#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_14_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


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

    # 3. Query both State and City using a join
    # We sort by City.id as requested
    results = session.query(State, City)\
                     .filter(State.id == City.state_id)\
                     .order_by(City.id)\
                     .all()

    # 4. Print results: <state name>: (<city id>) <city name>
    for state, city in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # 5. Close session
    session.close()
