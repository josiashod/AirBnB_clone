#!/usr/bin/python3
"""Modue for test BaseModel class"""
import unittest
from models.base_model import BaseModel


class TestBaseModelMethods(unittest.TestCase):
    """ Suite to test BaseModel class """

    def setUp(self):
        """ Method invoked for each test """
        self.base_one = BaseModel()
        self.base_two = BaseModel()

    def test_id(self):
        """Test if each new instance has different id"""

        self.assertNotEqual(self.base_one, self.base_two)

    def test_str(self):
        """Test the str representation of the object"""

        obj_str = f"[{self.base_one.__class__.__name__}] "
        obj_str += f"({self.base_one.id}) {self.base_one.__dict__}"

        self.assertEqual(self.base_one.__str__(), obj_str)

    def test_save(self):
        """Test the method save of base_model"""

        old_date = self.base_one.updated_at
        self.base_one.save()

        self.assertNotEqual(self.base_one.updated_at, old_date)

    def test_to_dict(self):
        """Test the method to_dict of base_model"""

        base_one = self.base_one
        base_one.name = "Josias"
        base_one.age = 30

        expected_dict = {
            'id': base_one.id,
            '__class__': base_one.__class__.__name__,
            'created_at': base_one.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f'),
            'updated_at': base_one.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f'),
            'name': base_one.name,
            'age': base_one.age,
        }

        self.assertEqual(base_one.to_dict(), expected_dict)
