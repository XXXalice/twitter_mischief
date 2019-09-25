from engine import scrape, db

scraper = scrape.Scrape()
scraper.crawl(lang='ja', word='失恋', user='inage39')