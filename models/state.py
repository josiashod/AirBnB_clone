#!/usr/bin/python3
"""State Model module"""

from models import base_model


class State(base_model.BaseModel):
    """This class defines the State structure for the projects
    and inherits from BaseModel.

    Atributes:
        name (string): the state name
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
