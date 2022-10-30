#!/usr/bin/env python3
"""
A model that implements base model class
"""
import uuid

class BaseModel:
	"""
	A class that deines all common attributes/methods for other classes
	"""
	def __init__(self, id):
		"""
		A fuction that defines the instance attributes
		"""
		self.id = str(uuid.uuid4())
		self.created_at = datetime.now()
		self.updated_at = datetime.now()
	
	
	def __str__(self):
		print(f"[{self.__name__}] ({self.id}) <{self.__dict__}>")
