# -*- coding: utf-8 -*-

# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    # define the fields for your item here like:
    site = scrapy.Field()
    movie_id = scrapy.Field()
    name = scrapy.Field()
    description = scrapy.Field()
    actor = scrapy.Field()
    upload_date = scrapy.Field()
    duration = scrapy.Field()
    series = scrapy.Field()
    tag = scrapy.Field()
    movie_tag = scrapy.Field()
    rating = scrapy.Field()
    images = scrapy.Field()
    image_urls = scrapy.Field()
    files = scrapy.Field()
    file_urls = scrapy.Field()