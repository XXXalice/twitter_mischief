from engine import scrape, db
import pprint

scraper = scrape.Scrape()
html_body = scraper.crawl(lang='ja', word='裏切られ', user='inage39')
contents = scraper.tweet_scrape(body=html_body)
print(contents)
# db_scheme = db.Database()
# model = db.Tweet()
# model.create(base=db_scheme.Base, engine=db_scheme.ENGINE)