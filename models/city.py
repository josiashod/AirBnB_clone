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

    def __init__(self, *args, **kwargs):
        """Initialize the class.

        Parameters:
            args (list): not used.
            kwargs (dict): used to assign attribute to the object
        """

        if kwargs is not None and len(kwargs.keys()) > 0:
            super().__init__(**kwargs)
        else:
            super().__init__()
