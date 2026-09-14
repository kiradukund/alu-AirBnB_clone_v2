#!/usr/bin/python3
"""This module defines the State class for the AirBnB clone project."""
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """Represents a State for the AirBnB clone project."""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")
    else:
        @property
        def cities(self):
            """Return list of City instances with state_id == current State.id."""
            from models import storage
            from models.city import City
            return [c for c in storage.all(City).values()
                    if c.state_id == self.id]
