#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import models

storage_type = getenv("HBNB_TYPE_STORAGE")

class State(BaseModel):
    """ State class """
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete-orphan")
    else:
        name = ""

    @property
    def cities(self):
        """ cities """
        ls = []
        for x in models.storage.all(City).values():
            if x.state_id == self.id:
                ls.append(x)
        return ls
