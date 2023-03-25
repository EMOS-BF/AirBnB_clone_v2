#!/usr/bin/python3
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel
from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity

classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class BaseModel:
    engine = None
    session = None
    
    def __init__(self):
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')

        self.engine = create_engine('mysql+pymysql://user:pwd@host/db')
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.engine)

def all(self,cls=None):
        """Returns a dictionary of models currently in storage"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)


def save(self):
    """commit all changes of the current database session"""
    self.__session.commit()


def delete(self, obj=None):
    """delete from the current database session obj if not None"""
    if obj is not None:
        self.__session.delete(obj)

def close(self):
    """call remove() method on the private session attribute"""
    self.__session.remove()

