# -*- coding: utf-8 -*-
import scrapy


class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['http://www.vmovier.com']
    start_urls = ['http://http://www.vmovier.com/']

    def parse(self, response):
         pass
