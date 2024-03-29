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
                elif key == '__class__':
                    continue
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Returns the string representation"""
        for key in self.__dict__.keys():
            if key == '__class__':
                self.__dict__.pop(key)
                break
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
        h = self.__dict__.copy()
        h['__class__'] = type(self).__name__
        for key, value in h.items():
            if key == "created_at" or key == "updated_at":
                h[key] = value.isoformat()
            else:
                h[key] = value
        return h
