from bs4 import BeautifulSoup
from urllib import request, parse
import unicodedata
from etc import driver, logger

class Scrape:
    def __init__(self):
        yml_path = './config.yml'
        self.param = driver.read_yaml(yml_path)
        self.log = logger.Logger()


    def crawl(self, **attrs):
        uri = self.__construct_query(attrs)
        ua = self.param['server']['ua']
        req = request.Request(url=uri, headers={ 'User-Agent': ua})
        print(uri)
        with request.urlopen(req) as resp:
            b = resp.read().decode('UTF-8')
        return b

    def __construct_query(self, attrs):
        base = self.param['server']['api']
        self.word = attrs['word']
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
                attrs[k] = parse.quote(attrs[k]) if not unicodedata.east_asian_width(attrs[k][0]) == 'Na' else attrs[k]

                base += v.format(attrs[k])
        return base

    def tweet_scrape(self, body, parser='lxml'):
        scrap_contents = ['strong', 'a']
        soup = BeautifulSoup(body, parser)
        tweets = soup.find_all('p', attrs={ 'class': 'TweetTextSize'})
        contents_stacks = []
        self.log.debug(tweets)
        for tweet in tweets:
            for scrap_content in scrap_contents:
                if not None == tweet.find(scrap_content):
                    tweet.find(scrap_content).replace_with(tweet.find(scrap_content).contents[0])
                else:
                    continue
            contents_stacks.append(tweet.contents[0])
        return contents_stacks
