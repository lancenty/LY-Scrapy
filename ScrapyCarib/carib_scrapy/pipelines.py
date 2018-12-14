# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.pipelines.files import FilesPipeline

class RatingPipeline(object):
    rating_map = {
        '★':     1,
        '★★':    2,
        '★★★':   3,
        '★★★★':  4,
        '★★★★★': 5,
    }

    def process_item(self, item, spider):
        rating = item.get('rating')
        if rating:
            item['rating'] = self.rating_map[rating]
        return item


class JsonWithEncodingPipeline(object):

    def __init__(self):
        self.file = codecs.open('scraped_data_utf8.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()


class MyFilesPipeline(FilesPipeline):
    

    def get_media_requests(self, item, info):
        file_url = item['file_urls']
        actor = ' '.join(item['actor'])
        meta = {
                  'filename': '-'.join([item['site'], item['movie_id'], item['name'], actor,]),
                }
        yield scrapy.Request(url=file_url, meta=meta)
        #i = 1
        #for image_url in item['image_urls']:
        #    filename = '{}_{}.jpg'.format(item['name_image'], i)
        #    yield scrapy.Request(image_url, meta={'filename': filename})
        #    i += 1
        #return


    def file_path(self, request, response=None, info=None):
        return request.meta['filename'] 


class MyImagesPipeline(ImagesPipeline):


    def get_media_requests(self, item, info):
        image_url = item['image_urls']
        actor = ' '.join(item['actor'])
        meta = {
                  'filename': '-'.join([item['site'], item['movie_id'], item['name'], actor,]),
                }
        yield scrapy.Request(url=image_url, meta=meta)

    
    def image_path(self, request, response=None, info=None):
        return request.meta['filename'] 