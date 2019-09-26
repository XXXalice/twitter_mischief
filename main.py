from engine import scrape, db

scraper = scrape.Scrape()
html_body = scraper.crawl(lang='ja', word='手取り15万', user='inage39')