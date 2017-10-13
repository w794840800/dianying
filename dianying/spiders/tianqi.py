# -*- coding: utf-8 -*-
import scrapy


class TianqiSpider(scrapy.Spider):
    name = 'tianqi'
    allowed_domains = ['tianqi.com']
    start_urls = ['http://hefei.tianqi.com/']

    def parse(self, response):
        #print(response)
        tqshow1 = response.xpath('//div[@class="tqshow1"]')
        #print(len(tqshow1))
        for div in tqshow1:
            data = div.xpath('./p//text()').extract()[0]
            
            print("data",data)