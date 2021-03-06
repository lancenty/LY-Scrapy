# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
from scrapy.linkextractors import LinkExtractor
from ..items import MovieItem

script = """
         function main(splash)
            splash:go(splash.args.url)
            splash:wait(10)
            splash:runjs("document.getElementsByClassName('see-more')[0].click()")
            splash:wait(10)
            return splash:html()
         end
         """

class A1pondoSpider(scrapy.Spider):
    name = '1pondo'
    allowed_domains = ['www.1pondo.tv']
    start_urls = ['http://https://www.1pondo.tv/list/?o=newest/']

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

        movie['site'] = "1pondo"
        movie['movie_id'] = movie_id
        movie['name'] = sel.css('h1.h1--dense::text').extract_first()
        movie['description'] = sel.css('div.movie-detail p::text').extract_first()

        movie['actor'] = sel.xpath('//ul/li/span/a[@itemprop="actor"]/span/text()').extract()
        movie['upload_date'] = sel.xpath('//ul/li//span[@itemprop="uploadDate"]/text()').re_first(r'\d{4}\/\d{2}\/\d{2}')
        movie['duration'] = sel.xpath('//ul/li//span[@itemprop="duration"]/text()').re_first(r'\d{2}\:\d{2}\:\d{2}')
        movie['series'] = sel.xpath('//ul/li[span[@class="spec-title"]/text()="シリーズ"]/span[@class="spec-content"]/a/text()').extract()
        movie['tag'] = sel.xpath('//ul/li[span[@class="spec-title"]/text()="タグ"]/span[@class="spec-content"]/a/text()').extract()
        movie['movie_tag'] = sel.xpath('//div[@class="movie-tag"]/div/text()').extract()
        movie['rating'] = sel.css('span.rating::text').extract_first()
        
        movie['image_urls'] = "https://www.1pondo.tv/assets/sample/" + movie_id + "/str.jpg"

        yield movie
