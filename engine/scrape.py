from bs4 import BeautifulSoup
from urllib import request
from etc import driver, logger

class Scrape:
    def __init__(self):
        yml_path = './config.yml'
        self.param = driver.read_yaml(yml_path)