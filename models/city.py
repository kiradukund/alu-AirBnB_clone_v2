#!/usr/bin/python3
"""This module defines the City class for the AirBnB clone project."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """Represents a City for the AirBnB clone project."""

    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    name = Column(String(128), nullable=False)
    places = relationship("Place", backref="cities",
                          cascade="all, delete-orphan")
