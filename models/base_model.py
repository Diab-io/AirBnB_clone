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

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) <{self.__dict__}>"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        newdict = self.__dict__.copy()
        newdict["__class__"] = self.__class__.__name__
        for key, value in newdict.items():
            if key in ("created_at", "updated_at"):
                value = newdict[key].isoformat()
                newdict[key] = value
        return newdict
