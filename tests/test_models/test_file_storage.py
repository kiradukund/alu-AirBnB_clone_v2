#!/usr/bin/python3
"""Unittest module for the FileStorage class."""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def test_all_returns_dict(self):
        """Test that all() returns a dictionary."""
        self.assertIsInstance(storage.all(), dict)

    def test_new(self):
        """Test that new() adds an object to __objects."""
        obj = BaseModel()
        key = "BaseModel.{}".format(obj.id)
        self.assertIn(key, storage.all())

    def test_save_creates_file(self):
        """Test that save() creates the JSON file."""
        storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        """Test that reload() loads objects from the JSON file."""
        obj = BaseModel()
        obj.save()
        storage.reload()
        key = "BaseModel.{}".format(obj.id)
        self.assertIn(key, storage.all())

    def test_class_doc(self):
        """Test that FileStorage class has a docstring."""
        self.assertIsNotNone(FileStorage.__doc__)


if __name__ == "__main__":
    unittest.main()
