#!/usr/bin/python3
"""This module defines the BaseModel class for the AirBnB clone project."""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

time_fmt = "%Y-%m-%dT%H:%M:%S.%f"
Base = declarative_base()


class BaseModel:
    """Defines all common attributes and methods for other classes."""

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance."""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ("created_at", "updated_at"):
                    value = datetime.strptime(value, time_fmt)
                setattr(self, key, value)
        if "id" not in self.__dict__:
            self.id = str(uuid.uuid4())
        if "created_at" not in self.__dict__:
            self.created_at = datetime.utcnow()
        if "updated_at" not in self.__dict__:
            self.updated_at = datetime.utcnow()

    def __str__(self):
        """Return string representation of the BaseModel instance."""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Update updated_at with current datetime and save to storage."""
        from models import storage
        self.updated_at = datetime.utcnow()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Return a dictionary representation of the instance."""
        d = self.__dict__.copy()
        d["__class__"] = type(self).__name__
        if isinstance(d.get("created_at"), datetime):
            d["created_at"] = d["created_at"].isoformat()
        if isinstance(d.get("updated_at"), datetime):
            d["updated_at"] = d["updated_at"].isoformat()
        d.pop("_sa_instance_state", None)
        return d

    def delete(self):
        """Delete current instance from storage."""
        from models import storage
        storage.delete(self)
