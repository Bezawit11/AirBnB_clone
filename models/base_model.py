import uuid
import models
from datetime import datetime


class BaseModel:
        """  """
    def __init__(self, *args, **kwargs):
        """  """
        form1 = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'created_at':
