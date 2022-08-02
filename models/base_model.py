#!/usr/bin/python3
"""Base Model module"""
import uuid
from datetime import datetime

class BaseModel:
    """This class will be the "base model" of all other model of the project
    and defines all common attributes/methods for other classes.

    Atributes:
        id (string): the model instance unique id
        created_at (datetime): the date on which the instance was created
        updated_at (datetime): the date on which the instance was updated
    """

    def __init__(self):
        """Initialize the class."""

        now = datetime.now()
        self.id = str(uuid.uuid4())
        self.created_at = now
        self.updated_at = now
    
    def save(self):
        """Updates the public instance attribute updated_at with the current datetime"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the instance"""

        _dict = self.__dict__
        _dict['__class__'] = self.__class__.__name__
        _dict['created_at'] = _dict['created_at'].strftime('%Y-%m-%dT%H:%M:%S.%f')
        _dict['updated_at'] = _dict['updated_at'].strftime('%Y-%m-%dT%H:%M:%S.%f')

        return (_dict)
    
    def __str__(self):
        """Returns the string representation of the object"""

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
