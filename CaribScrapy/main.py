from scrapy.crawler import CrawlerProcess
from carib_scrapy.spiders.carib import CaribSpider

def main():
    process = CrawlerProcess()
    process.crawl('carib')
    process.start()
    return
