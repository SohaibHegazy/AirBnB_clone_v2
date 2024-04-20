#!/usr/bin/python3
""" State Module for HBNB project """
import models
from os import getenv
from models.base_model import BaseModel
from models.city import City, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,  Integer, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship('City', backref='state', cascade="all, delete")
    else:
        name = ""
        @property
        def cities(self):
            list_of_cities = []
            dict_cities = models.storage.all(City)
            for city in dict_cities.values():
                if city.state_id == self.id:
                    list_of_cities.append(city)
            return list_of_cities

