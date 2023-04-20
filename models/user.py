#!/usr/bin/python3
"""Class User represents the clients that subscribe to GLS"""


from models.base_model import BaseModel


class User(BaseModel):
    """the User class"""
    full_name = ""
    business_name = ""
    email = ""
    password = ""
    phone_number = ""
    county = ""
    sub_county= ""
    area_and_street = ""
