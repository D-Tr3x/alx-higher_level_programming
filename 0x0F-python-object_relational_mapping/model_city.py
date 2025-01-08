#!/usr/bin/python3
""" Module defines `City` class and links it to MySQL `cities` table
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State


class City(Base):
    """ Class inherits from `Base` and links to MySQL table `cities`
    """
    __tablename__ = 'cities'

    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
