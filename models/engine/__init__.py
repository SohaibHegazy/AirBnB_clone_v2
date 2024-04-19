#!/usr/bin/python3
"""create a unique FileStorage instance for your application"""
from os import getenv


typeStorage = getenv("HBNB_TYPE_STORAGE")

# to MySQL
if typeStorage != 'db':
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
else:  # to JSON File
    from models.engine.db_storage import DBStorage
    storage = DBStorage()

storage.reload()
