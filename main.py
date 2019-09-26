from engine import scrape, db

scraper = scrape.Scrape()
html_body = scraper.crawl(lang='ja', word='裏切られ', user='inage39')