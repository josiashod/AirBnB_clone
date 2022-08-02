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

    def __init__(self, *args, **kwargs):
        """Initialize the class.

        Parameters:
            args (list): not used.
            kwargs (dict): used to assign attribute to the object

        Description:
            The init function used the kwargs dictionary to create an instance
            with the given key/value in the dictionary. Otherwise
            we create an instance with id and create_at.
        """

        if kwargs is not None and len(kwargs.keys()) > 0:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == 'created_at' or key == 'updated_at':
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def save(self):
        """Updates the public instance attribute updated_at with
        the current datetime."""

        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values
        of __dict__ of the instance."""

        _d = self.__dict__
        _d['__class__'] = self.__class__.__name__
        _d['created_at'] = _d['created_at'].strftime('%Y-%m-%dT%H:%M:%S.%f')
        _d['updated_at'] = _d['updated_at'].strftime('%Y-%m-%dT%H:%M:%S.%f')

        return (_d)

    def __str__(self):
        """Returns the string representation of the object"""

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
