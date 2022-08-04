#!/usr/bin/python3
"""Amenity Model module"""

from models import base_model


class Amenity(base_model.BaseModel):
    """This class defines the Amenty structure for the projects
    and inherits from BaseModel.

    Atributes:
        name (string): the name of the amenity
    """

    def __init__(self, *args, **kwargs):
        """Initialize the class.

        Parameters:
            args (list): not used.
            kwargs (dict): used to assign attribute to the object
        """

        self.name = ""

        if kwargs is not None and len(kwargs.keys()) > 0:
            super().__init__(**kwargs)
        else:
            super().__init__()
