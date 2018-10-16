# -*- coding: utf-8 -*-
import scrapy
print("banu")
class QSpider(scrapy.Spider):
    name = 'q'
    allowed_domains = ['quotes.toscrape.com/']
    start_urls = ['http://quotes.toscrape.com//']

    def parse(self, response):
        pass