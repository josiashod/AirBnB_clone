#!/usr/bin/python3
"""City Model module"""

from models import base_model


class City(base_model.BaseModel):
    """This class defines the City structure for the projects
    and inherits from BaseModel.

    Atributes:
        state_id (string): the corresponding state id of the city
        name (string): the name of the city
    """

    name = ""
    state_id = ""
