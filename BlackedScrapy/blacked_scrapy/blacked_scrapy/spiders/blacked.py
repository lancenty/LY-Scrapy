# -*- coding: utf-8 -*-
import scrapy


class BlackedSpider(scrapy.Spider):
    name = 'blacked'
    allowed_domains = ['https://www.blacked.com/videos']
    start_urls = ['http://https://www.blacked.com/videos/']

    def parse(self, response):
        pass
