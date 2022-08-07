#!/usr/bin/python3
"""State Model module"""

from models import base_model


class State(base_model.BaseModel):
    """This class defines the State structure for the projects
    and inherits from BaseModel.

    Atributes:
        name (string): the state name
    """

    name = ""
