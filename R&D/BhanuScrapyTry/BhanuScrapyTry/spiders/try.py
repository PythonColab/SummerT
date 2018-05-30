# -*- coding: utf-8 -*-
import scrapy


class TrySpider(scrapy.Spider):
    name = 'try'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/']

    def parse(self, response):
        pass
