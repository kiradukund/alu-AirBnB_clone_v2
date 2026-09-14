#!/usr/bin/python3
"""Unittest module for the FileStorage class."""
import unittest
import os
from os import getenv
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


@unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == "db", "not for db storage")
class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def test_all_returns_dict(self):
        """Test that all() returns a dictionary."""
        self.assertIsInstance(storage.all(), dict)

    def test_all_with_cls(self):
        """Test that all(cls) returns filtered dictionary."""
        result = storage.all(BaseModel)
        self.assertIsInstance(result, dict)

    def test_new(self):
        """Test that new() adds an object to __objects."""
        obj = BaseModel()
        storage.new(obj)
        key = "BaseModel.{}".format(obj.id)
        self.assertIn(key, storage.all())

    def test_save_creates_file(self):
        """Test that save() creates the JSON file."""
        storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_delete(self):
        """Test that delete() removes an object from storage."""
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        storage.delete(obj)
        key = "BaseModel.{}".format(obj.id)
        self.assertNotIn(key, storage.all())

    def test_class_doc(self):
        """Test that FileStorage class has a docstring."""
        self.assertIsNotNone(FileStorage.__doc__)


if __name__ == "__main__":
    unittest.main()
