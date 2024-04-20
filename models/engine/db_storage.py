#!/usr/bin/python3
'''
storage engine to store database
'''
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine


class DBStorage():
    '''
    class of the storage in the database
    '''
    __engine = None
    __session = None

    def __init__(self):
        '''
        initiator of the database storage class
        '''
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")
        HBNB_ENV = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, password, host, database), pool_pre_ping=True)
        
        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)
            
    def all(self, cls=None):
        '''
        add the object to the current database session
        '''
        classes = ['State', 'City', 'User', 'Place', 'Review', 'Amenity']
        obj_list = []
        class_dict = {}

        if cls == None:
            for item in classes:
                obj_list.extend(self.__session.query(item))
        else:
            obj_list.extend(self.__session.query(cls))

        for obj in obj_list:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            value = obj
            class_dict[key] = value
        
        return class_dict
    
    def save(self):
        '''
        commit all changes of the current database session
        '''
        self.__session.commit()

    def new(self, obj):
        '''
        add the object to the current database session
        '''
        self.__session.add()

    def delete(self, obj=None):
        '''
        delete from the current database session obj if not None
        '''
        if obj:
            self.__session.delete(obj)

    def reload(self):
        '''
        create all tables in the database (feature of SQLAlchemy)
        '''
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(
            bind=self.__engine, expire_on_commit=False))
        self.__session = Session()

        def close(self):
            self.__session.close()

