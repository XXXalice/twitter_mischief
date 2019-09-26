from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
from etc import driver, logger

class Database:
    def __init__(self):
        yml_path = './config.yml'
        self.param = driver.read_yaml(yml_path)
