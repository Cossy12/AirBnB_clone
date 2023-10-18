#!/usr/bin/env python3
"""  user """

from models.base_model import BaseModel


class User(BaseModel):
    """  attributes of the user """
    email = ''
    password = ''
    first_name = ''
    last_name = ''

