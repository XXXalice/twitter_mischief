from bs4 import BeautifulSoup
from urllib import request
from etc import driver, logger

class Scrape:
    def __init__(self):
        yml_path = './config.yml'
        self.param = driver.read_yaml(yml_path)


    def crawl(self, **attrs):
        uri = self.__construct_query(attrs)
        req = request.Request(url=uri)
        with request.urlopen(req) as resp:
            b = resp.read()

    def __construct_query(self, attrs):
        base = self.param['server']['api']
        base += '?'
        items_checker = {
            'lang':"lang={}",
            'user':"(from:%3A{})",
            'word':"{}"
        }
        for k, v in items_checker.items():
            if k in attrs.keys():
                base += v.format(attrs[k])
            base += '&'

        return base