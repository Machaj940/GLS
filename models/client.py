#!/usr/bin/python3
"""Class Client represents the clients that subscribe to GLS"""


from models.base_model import BaseModel


class Client(BaseModel):
    """
        the Client class
        - will add business_name attribute later. the console currently only
          takes one argument for certain functions eg Client.update(
          "<client id>, "business_name" "futurescope Designs") will only
          register the name as futurescope
    """
    first_name = ""
    last_name = ""
    #business_name = ""
    email = ""
    password = ""
    phone_number = ""
    county = ""
    sub_county= ""
    area_and_street = ""
