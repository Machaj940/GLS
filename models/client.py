#!/usr/bin/python3
"""Class Client represents the clients that subscribe to GLS"""


from models.base_model import BaseModel


class Client(BaseModel):
    """the Client class"""
    full_name = ""
    business_name = ""
    email = ""
    password = ""
    phone_number = ""
    county = ""
    sub_county= ""
    area_and_street = ""
