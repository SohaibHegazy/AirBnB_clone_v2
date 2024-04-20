#!/usr/bin/python3
'''
Determine the env to select the storage method
'''
from os import getenv


typeStorage = getenv("HBNB_TYPE_STORAGE")

if typeStorage != 'db':
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
else:
    from models.engine.db_storage import DBStorage
    storage = DBStorage()

storage.reload()
