#!/usr/bin/python3
"""module for db engine"""
import os

from sqlalchemy import create_engine

from models.base_model import BaseModel
from models.city import City
from models.state import State


class DBStorage:
    """class for database storage"""

    __engine = None
    __session = None

    def __init__(self):
        user = os.getenv("HBNB_MYSQL_USER")
        pwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")
        db_url = "mysql+mysqldb://{}:{}@{}/{}"\
        .format(user, pwd, host, db)
        self.__engine = create_engine(db_url, pool_pre_ping=True)

        Base.metadata.create_all(self.__engine)
