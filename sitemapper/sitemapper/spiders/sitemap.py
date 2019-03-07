# -*- coding: utf-8 -*-
import scrapy


class SitemapSpider(scrapy.Spider):
    name = 'sitemap'
    allowed_domains = ['example.com']
    # start_urls = ['http://example.com/']

    sitemap_urls = ['https://sutaba-mac.site/robots.txt']
    def parse(self, response):
        # URLとタイトルの辞書(dictionary)を返す
        yield {
            'url': response.url,
            'title': response.css('title::text').extract_first(),
        }
