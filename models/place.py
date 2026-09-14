#!/usr/bin/python3
"""This module defines the Place class for the AirBnB clone project."""
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship

place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             primary_key=True, nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """Represents a Place for the AirBnB clone project."""

    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        amenities = relationship("Amenity", secondary="place_amenity",
                                 viewonly=False)
        reviews = relationship("Review", backref="place",
                               cascade="all, delete-orphan")
    else:
        @property
        def amenities(self):
            """Return list of Amenity instances linked to this Place."""
            from models import storage
            from models.amenity import Amenity
            return [a for a in storage.all(Amenity).values()
                    if a.id in self.amenity_ids]

        @amenities.setter
        def amenities(self, obj):
            """Append amenity id to amenity_ids list."""
            from models.amenity import Amenity
            if isinstance(obj, Amenity):
                if not hasattr(self, 'amenity_ids'):
                    self.amenity_ids = []
                self.amenity_ids.append(obj.id)

        @property
        def reviews(self):
            """Return list of Review instances with place_id == self.id."""
            from models import storage
            from models.review import Review
            return [r for r in storage.all(Review).values()
                    if r.place_id == self.id]
