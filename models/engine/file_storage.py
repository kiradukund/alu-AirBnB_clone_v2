#!/usr/bin/python3
"""This module defines the FileStorage class for the AirBnB clone project."""
import json


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON to instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Return dictionary of all stored objects, optionally filtered by cls."""
        if cls is None:
            return FileStorage.__objects
        return {k: v for k, v in FileStorage.__objects.items()
                if isinstance(v, cls)}

    def new(self, obj):
        """Set obj in __objects with key <class name>.id."""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        d = {}
        for key, obj in FileStorage.__objects.items():
            d[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(d, f)

    def reload(self):
        """Deserialize the JSON file to __objects if the file exists."""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                d = json.load(f)
            for key, value in d.items():
                cls_name = value.get("__class__")
                if cls_name in classes:
                    FileStorage.__objects[key] = classes[cls_name](**value)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete obj from __objects if it exists."""
        if obj is None:
            return
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects.pop(key, None)

    def close(self):
        """Call reload method for deserializing the JSON file to objects."""
        self.reload()
