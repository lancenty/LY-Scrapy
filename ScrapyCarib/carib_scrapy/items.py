# -*- coding: utf-8 -*-

# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    # define the fields for your item here like:
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
    image_urls = scrapy.Field()
    file_urls = scrapy.Field()