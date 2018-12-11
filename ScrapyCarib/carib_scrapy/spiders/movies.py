# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from ..items import MovieItem

class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['www.caribbeancom.com']
    start_urls = ['https://www.caribbeancom.com/listpages/all1.htm']


    def parse(self, response):
        le = LinkExtractor(restrict_xpaths='//div[@class="grid-item"]//div[@class="meta-title"]/a[@itemprop="url"]')
        for link in le.extract_links(response):
            yield scrapy.Request(link.url, callback=self.parse_movie)

        le = LinkExtractor(restrict_xpaths='//div[@class="pagination-large"]//a[@rel="next"]')
        links = le.extract_links(response)
        if links:
            next_url = links[0].url
            yield scrapy.Request(next_url, callback=self.parse)
    

    def parse_movie(self, response):
        movie = MovieItem()
        movie_id = response.url.split('/')[-2]
        sel = response.css('div.movie-info')

        movie['site'] = "Carib"
        movie['movie_id'] = movie_id
        movie['name'] = sel.css('div.heading h1::text').extract_first()
        movie['description'] = sel.xpath('//p[@itemprop="description"]/text()').extract_first()
        movie['actor'] = sel.xpath('//ul/li/span/a[@itemprop="actor"]/span/text()').extract()
        movie['upload_date'] = sel.xpath('//ul/li//span[@itemprop="uploadDate"]/text()').re_first(r'\d{4}\/\d{2}\/\d{2}')
        movie['duration'] = sel.xpath('//ul/li//span[@itemprop="duration"]/text()').re_first(r'\d{2}\:\d{2}\:\d{2}')
        movie['series'] = sel.xpath('//ul/li[span[@class="spec-title"]/text()="シリーズ"]/span[@class="spec-content"]/a/text()').extract()
        movie['tag'] = sel.xpath('//ul/li[span[@class="spec-title"]/text()="タグ"]/span[@class="spec-content"]/a/text()').extract()
        movie['movie_tag'] = sel.xpath('//div[@class="movie-tag"]/div/text()').extract()
        movie['rating'] = sel.css('span.rating::text').extract_first()
        movie['image_urls'] = ["http://www.caribbeancom.com/moviepages/" + movie_id + "/images/l_l.jpg",]
        movie['file_urls'] = ["https://smovie.caribbeancom.com/sample/movies/" + movie_id + "/480p.mp4",]

        yield movie