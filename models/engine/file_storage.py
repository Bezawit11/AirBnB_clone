#!/usr/bin/python3
"""   """

from os.path import exists
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place
import json


class FileStorage:
    """  """
    __file_path = "file.json"
    __objects = {}  # dictionary - empty but will store all objects by <class name>.id

    def all(self):
        """  """
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """ """
        out_file = open(self.__file_path, "w")
        d = self.__objects.copy()
        for key, value in d.items():
            d[key] = value.to_dict()
        json.dump(d, out_file, indent=6, default=str)
        out_file.close()

    def reload(self):
        """  """
        try:
            with open(FileStorage.__file_path) as f:
                read = json.load(f)
                for keys, values in read.items():
                    for k, v in values.items():
                        if k == "__class__":
                            values.pop("__class__")
                            break
                        break
                    self.__objects[keys] = BaseModel(**values)
        except (json.decoder.JSONDecodeError, FileNotFoundError):
            return
