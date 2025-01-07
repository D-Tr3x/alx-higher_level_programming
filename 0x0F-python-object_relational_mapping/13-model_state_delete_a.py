#!/usr/bin/python3
""" Module deletes all `State` objects with a name containing the letter 'a'
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, database), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    clear_states = session.query(State).filter(State.name.like('%a%')).all()

    for state in clear_states:
        session.delete(state)

    session.commit()
    session.close()
