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

    def test_email(self):
        """Test that email is an empty string by default."""
        u = User()
        self.assertEqual(u.email, "")

    def test_password(self):
        """Test that password is an empty string by default."""
        u = User()
        self.assertEqual(u.password, "")

    def test_first_name(self):
        """Test that first_name is an empty string by default."""
        u = User()
        self.assertEqual(u.first_name, "")

    def test_last_name(self):
        """Test that last_name is an empty string by default."""
        u = User()
        self.assertEqual(u.last_name, "")

    def test_class_doc(self):
        """Test that User class has a docstring."""
        self.assertIsNotNone(User.__doc__)


if __name__ == "__main__":
    unittest.main()
