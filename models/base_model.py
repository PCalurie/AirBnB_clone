#!/usr/bin/python3
""" Define the BaseModel"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """
    BaseModel class for the AirBnB clone project.

    Attributes:
        id (str): The unique identifier of the instance.
        created_at (datetime): datetime when the instance was last created.
        updated_at (datetime): datetime when the instance was last updated.
    """
    def __init__(self, *args, **kwargs):
        """
    Initializes a new instance of the class.

    Args:
        *args: Variable positional arguments (not used).
        **kwargs: Keyword arguments to initialize instance attributes.
            '__class__' key is ignored. 'created_at' and 'updated_at'
            keys are parsed as datetime objects, other keys are assigned
            their corresponding values.

    Attributes:
        id (str): Unique identifier for the instance.
        created_at (datetime): Timestamp rep the instance's creation time.
        updated_at (datetime): Timestamp rep the instance's update time.
        Other instance attributes set using **kwargs.

    """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                format_string = '%Y-%m-%dT%H:%M:%S.%f'
                if key == 'updated_at' or key == 'created_at':
                    setattr(self, key, datetime.strptime(value, format_string))
                else:
                    setattr(self, key, value)
        else:
            models.storage.new(self)

    def save(self):
        """
        Updates the updated_at attribute with
        the current datetime and saves the instance.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Converts the instance attributes to a dictionary representation.

        Returns:
            dict: A dictionary containing the instance attributes.
        """
        data = self.__dict__.copy()
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        data['__class__'] = self.__class__.__name__
        return data

    def __str__(self):
        """
        Returns a string representation of the instance.

        Returns:
            str: A formatted string representing the instance.
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )
