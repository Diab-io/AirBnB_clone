#!/usr/bin/env python3
"""
A module that implements the base model class
"""
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """
    A class that defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the BaseModel class
        """
        from models import storage
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ("created_at", "updated_at"):
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Returns the string representation of BaseModel object.
        [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[{self.__class__.__name__}] ({self.id}) <{self.__dict__}>"

    def save(self):
        """
        Updates 'self.updated_at' with the current datetime
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__
        of the instance:
        - only instance attributes set will be returned
        - a key __class__ is added with the class name of the object
        - created_at and updated_at must be converted to string object in ISO
        object
        """
        newdict = self.__dict__.copy()
        newdict["__class__"] = self.__class__.__name__
        for key, value in newdict.items():
            if key in ("created_at", "updated_at"):
                value = newdict[key].isoformat()
                newdict[key] = value
        return newdict
