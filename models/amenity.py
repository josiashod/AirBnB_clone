#!/usr/bin/python3
"""Amenity Model module"""

from models import base_model


class Amenity(base_model.BaseModel):
    """This class defines the Amenty structure for the projects
    and inherits from BaseModel.

    Atributes:
        name (string): the name of the amenity
    """

    name = ""
