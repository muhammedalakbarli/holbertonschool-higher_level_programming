#!/usr/bin/python3
"""
Contains the class definition of a State and an instance
Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create the base class for declarative class definitions
Base = declarative_base()


class State(Base):
    """
    State class inherits from Base and links to the MySQL table 'states'
    """
    __tablename__ = 'states'

    # Column 'id': auto-generated, unique integer, can't be null, primary key
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    # Column 'name': string with max 128 characters, can't be null
    name = Column(String(128), nullable=False)
