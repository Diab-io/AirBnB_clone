#!/usr/bin/env python3
""" contains the review model """
from models.base_model import BaseModel


class Review(BaseModel):
    """
    implements the review model
    """
    place_id = ""
    user_id = ""
    text = ""
