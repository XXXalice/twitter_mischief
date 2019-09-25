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
        return b

    def __construct_query(self, attrs):
        base = self.param['server']['api']
        base += '?'
        items_checker = {
            'lang':"lang={}&",
            'user':"(from:{})",
            'word':"{}"
        }
        for k, v in items_checker.items():
            if k in attrs.keys():
                if not k == 'lang' and not 'q=' in base:
                    base += 'q='
                base += v.format(attrs[k])


        return base