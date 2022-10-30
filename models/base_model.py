# #!/usr/bin/env python3

"""
A model that implements base model class
"""
from datetime import datetime
import imp

import uuid


class BaseModel:
	"""
	A class that deines all common attributes/methods for other classes
	"""
	def __init__(self, *args, **kwargs):
		"""
		A fuction that defines the instance attributes

		"""
		from models import storage
		if not kwargs:
			self.id = str(uuid.uuid4())
			self.created_at = datetime.now()
			self.updated_at = datetime.now()
			storage.new(self)
		else:
			for key, value in kwargs.items():
				if key != '__class__':
					if key in ('created_at', 'updated_at'):
						setattr(self, key, datetime.fromisoformat(value))
					else:
						setattr(self, key, value)
	
	
	def __str__(self):
		"""
        Returns the string representation of BaseModel object.
        [<class name>] (<self.id>) <self.__dict__>
        """
		return "[{}] ({}) <{}>".format(type(self).__name__, self.id, self.__dict__)

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
		for key, value in self.__dict__.items():
			if key in ("created_at", "updated_at"):
				value = self.__dict__[key].isoformat()
				newdict[key] = value
		return newdict
