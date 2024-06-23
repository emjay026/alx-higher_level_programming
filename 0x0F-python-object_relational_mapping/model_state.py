#!/usr/bin/python3
"""This module implements an ORM mapped class named 'State'.

An ORM mappad class can be seen as an equivalent to a
table inside some database.
"""
import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """This class models State ORM mapped class."""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    # create a reference to city objects and
    # form a bidirectional attribute in 'City' that has access to my objects
    cities = relationship("City", back_populates="state")
