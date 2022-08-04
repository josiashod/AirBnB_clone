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

    def __init__(self, *args, **kwargs):
        """Initialize the class.

        Parameters:
            args (list): not used.
            kwargs (dict): used to assign attribute to the object
        """

        self.place_id = ""
        self.user_id = ""
        self.text = ""

        if kwargs is not None and len(kwargs.keys()) > 0:
            super().__init__(**kwargs)
        else:
            super().__init__()
