#!/usr/bin/python3
"""
Module: base_model.py
"""
import uuid
import models
from datetime import datetime


class BaseModel:
    """defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """initializes an object
        """
        form1 = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'created_at':
                    self.created_at = datetime.strptime(value, form1)
                elif key == 'updated_at':
                    self.updated_at = datetime.strptime(value, form1)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Returns the string representation"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute
           updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of
            __dict__ of the instance
        """
        h = {**self.__dict__}
        h['__class__'] = type(self).__name__
        h['created_at'] = h['created_at'].isoformat()
        h['updated_at'] = h['updated_at'].isoformat()
        return h
