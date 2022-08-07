#!/usr/bin/python3
"""User Model module"""

from models import base_model


class User(base_model.BaseModel):
    """This class defines the User structure for the projects
    and inherits from BaseModel.

    Atributes:
        email (string): the user email
        password (string): the user password
        first_name (string): the user first_name
        last_name (string): the user last_name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
