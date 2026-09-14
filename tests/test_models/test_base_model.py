#!/usr/bin/python3
"""Unittest module for the BaseModel class."""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def test_instance_creation(self):
        """Test that a BaseModel instance is created correctly."""
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)

    def test_id_is_string(self):
        """Test that id is a string."""
        obj = BaseModel()
        self.assertIsInstance(obj.id, str)

    def test_id_unique(self):
        """Test that each instance has a unique id."""
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_created_at_is_datetime(self):
        """Test that created_at is a datetime object."""
        obj = BaseModel()
        self.assertIsInstance(obj.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Test that updated_at is a datetime object."""
        obj = BaseModel()
        self.assertIsInstance(obj.updated_at, datetime)

    def test_str(self):
        """Test the string representation of BaseModel."""
        obj = BaseModel()
        s = str(obj)
        self.assertIn("[BaseModel]", s)
        self.assertIn(obj.id, s)

    def test_to_dict(self):
        """Test that to_dict returns a dictionary with correct keys."""
        obj = BaseModel()
        d = obj.to_dict()
        self.assertIsInstance(d, dict)
        self.assertEqual(d["__class__"], "BaseModel")
        self.assertIsInstance(d["created_at"], str)
        self.assertIsInstance(d["updated_at"], str)
        self.assertNotIn("_sa_instance_state", d)

    def test_kwargs_init(self):
        """Test creating a BaseModel from a dictionary."""
        obj = BaseModel()
        d = obj.to_dict()
        obj2 = BaseModel(**d)
        self.assertEqual(obj.id, obj2.id)
        self.assertIsInstance(obj2.created_at, datetime)
        self.assertFalse(obj is obj2)

    def test_module_doc(self):
        """Test that the module has a docstring."""
        import models.base_model as m
        self.assertIsNotNone(m.__doc__)

    def test_class_doc(self):
        """Test that the class has a docstring."""
        self.assertIsNotNone(BaseModel.__doc__)

    def test_save_doc(self):
        """Test that save has a docstring."""
        self.assertIsNotNone(BaseModel.save.__doc__)

    def test_to_dict_doc(self):
        """Test that to_dict has a docstring."""
        self.assertIsNotNone(BaseModel.to_dict.__doc__)


if __name__ == "__main__":
    unittest.main()
