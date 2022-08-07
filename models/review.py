#!/usr/bin/python3
"""Review Model module"""

from models import base_model


class Review(base_model.BaseModel):
    """This class defines the Review structure for the projects
    and inherits from BaseModel.

    Atributes:
        place_id (string): the corresponding place id of the review
        user_id (string): the corresponding user id of the review
        text (string): the text of the review
    """

    place_id = ""
    user_id = ""
    text = ""
