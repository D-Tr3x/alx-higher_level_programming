#!/usr/bin/python3
""" Module prints all `City` objects from the database `hbtn_0e_14_usa`
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, database), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    all_cities = (
        session.query(City, State)
        .join(State, City.state_id == State.id)
        .order_by(City.id)
        .all()
    )
    for city, state in all_cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
