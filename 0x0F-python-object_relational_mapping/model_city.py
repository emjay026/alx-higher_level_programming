#!/usr/bin/env python3
"""This module implements an ORM mapped class named 'City'.

An ORM mappad class can be seen as an equivalent to a
table inside some database.
"""
import sqlalchemy
from model_state import Base, Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    """This class models City ORM mapped class."""
    __tablename__ = 'cities'

    # primary keys need not have to have nullable explicitly set to False.
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    # create a reference to state objects and
    # form a bidirectional attribute in 'State' that has access to my objects
    state = relationship("State", back_populates="cities")
