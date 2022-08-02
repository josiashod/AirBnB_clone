#!/usr/bin/python3
"""Modue for test BaseModel class"""
from datetime import datetime
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

        self.assertNotEqual(self.base_one.id, self.base_two.id)

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

        self.assertDictEqual(base_one.to_dict(), expected_dict)

    def test_init_kwargs(self):
        """Test create of base model with dict parameters"""

        base_one = BaseModel(**{
            'id': 'test-b6a6e15c',
            '__class__': 'BaseModel',
            'name': 'Josias hod',
            'school': 'ALX'
        })

        base_two = BaseModel(**{
            'id': 'test-b6a6e189c',
            '__class__': 'BaseModel',
            'created_at': '2017-09-28T21:05:54.119572',
            'name': 'ALX'
        })

        base_three = BaseModel(**{
            '__class__': 'BaseModel',
            'created_at': '2017-09-28T21:05:54.119572',
            'updated_at': '2018-09-28T21:05:54.119572',
        })

        self.assertEqual(base_one.id, 'test-b6a6e15c')
        self.assertEqual(base_one.name, 'Josias hod')
        self.assertEqual(base_one.school, 'ALX')

        self.assertEqual(base_two.id, 'test-b6a6e189c')
        self.assertIsInstance(base_two.created_at, datetime)
        self.assertEqual(base_two.name, 'ALX')

        self.assertIsInstance(base_three.created_at, datetime)
        self.assertIsInstance(base_three.updated_at, datetime)

    def test_init_kwargs_2(self):
        """Test create of base model with dict parameters"""

        base = BaseModel(**self.base_one.to_dict())

        self.assertEqual(base.id, self.base_one.id)
        self.assertEqual(base.created_at, self.base_one.created_at)
        self.assertEqual(base.updated_at, self.base_one.updated_at)
        self.assertDictEqual(base.to_dict(), self.base_one.to_dict())
