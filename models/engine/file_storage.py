#!/usr/bin/python3
""" FileStorage module
    This module defines the FileStorage class that serializes instances to JSON
    and deserializes JSON files to instances.
"""

import json
import os

from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """ This class serializes instances to a JSON file and deserializes
    JSON file to instances

    Attributes:
        __file_path (str): the path to the JSON file (ex: file.json).
        __objects (dict): store all objects by <class name>.id
            (ex: to store a BaseModel object with id=12121212,
            the key will be BaseModel.12121212)
    """

    __file_path = "storage.json"
    __objects = {}

    def __init__(self) -> None:
        pass

    def all(self):
        """Return the dictionary __objects"""

        return (self.__objects)

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id

            Parameters:
                obj (obj): the object to set in objects
        """

        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """ Serializes __objects to the JSON file (path: __file_path)"""

        __objects = FileStorage.__objects
        objects_dict = {
            key: __objects[key].to_dict() for key in __objects.keys()
        }
        with open(FileStorage.__file_path, "w") as f:
            f.write(json.dumps(objects_dict))

    def reload(self):
        """  Deserializes the JSON file to __objects if file exist;
        otherwise do nothing"""

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path) as f:
                for obj in json.loads(f.read()).values():
                    self.new(eval(obj['__class__'])(**obj))
