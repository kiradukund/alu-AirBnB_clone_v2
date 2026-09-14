#!/usr/bin/python3
"""Unittest module for the User class."""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    def test_instance(self):
        """Test that User is an instance of BaseModel."""
        u = User()
        self.assertIsInstance(u, BaseModel)

    def test_class_doc(self):
        """Test that User class has a docstring."""
        self.assertIsNotNone(User.__doc__)

    def test_tablename(self):
        """Test that User has correct table name."""
        self.assertEqual(User.__tablename__, "users")


if __name__ == "__main__":
    unittest.main()
