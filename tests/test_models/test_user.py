#!/usr/bin/python3
"""Modue for test User class"""
from datetime import datetime
import unittest
from models.user import User


class TestUserMethods(unittest.TestCase):
    """ Suite to test User class """

    def setUp(self):
        """ Method invoked for each test """
        self.user_one = User()
        self.base_two = User()

    def test_id(self):
        """Test if each new instance has different id"""

        self.assertNotEqual(self.user_one.id, self.base_two.id)

    def test_str(self):
        """Test the str representation of the object"""

        obj_str = f"[{self.user_one.__class__.__name__}] "
        obj_str += f"({self.user_one.id}) {self.user_one.__dict__}"

        self.assertEqual(self.user_one.__str__(), obj_str)

    def test_save(self):
        """Test the method save of base_model"""

        old_date = self.user_one.updated_at
        self.user_one.save()

        self.assertNotEqual(self.user_one.updated_at, old_date)

    def test_to_dict(self):
        """Test the method to_dict of base_model"""

        user_one = self.user_one
        user_one.name = "Josias"
        user_one.age = 30

        expected_dict = {
            'id': user_one.id,
            '__class__': user_one.__class__.__name__,
            'created_at': user_one.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f'),
            'updated_at': user_one.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f'),
            'name': user_one.name,
            'age': user_one.age,
        }

        self.assertDictEqual(user_one.to_dict(), expected_dict)

    def test_init_kwargs(self):
        """Test create of base model with dict parameters"""

        user_one = User(**{
            'id': 'test-b6a6e15c',
            '__class__': 'User',
            'name': 'Josias hod',
            'school': 'ALX'
        })

        base_two = User(**{
            'id': 'test-b6a6e189c',
            '__class__': 'User',
            'created_at': '2017-09-28T21:05:54.119572',
            'name': 'ALX'
        })

        base_three = User(**{
            '__class__': 'User',
            'created_at': '2017-09-28T21:05:54.119572',
            'updated_at': '2018-09-28T21:05:54.119572',
        })

        self.assertEqual(user_one.id, 'test-b6a6e15c')
        self.assertEqual(user_one.name, 'Josias hod')
        self.assertEqual(user_one.school, 'ALX')

        self.assertEqual(base_two.id, 'test-b6a6e189c')
        self.assertIsInstance(base_two.created_at, datetime)
        self.assertEqual(base_two.name, 'ALX')

        self.assertIsInstance(base_three.created_at, datetime)
        self.assertIsInstance(base_three.updated_at, datetime)

    def test_init_kwargs_2(self):
        """Test create of base model with dict parameters"""

        base = User(**self.user_one.to_dict())

        self.assertEqual(base.id, self.user_one.id)
        self.assertEqual(base.created_at, self.user_one.created_at)
        self.assertEqual(base.updated_at, self.user_one.updated_at)
        self.assertDictEqual(base.to_dict(), self.user_one.to_dict())
