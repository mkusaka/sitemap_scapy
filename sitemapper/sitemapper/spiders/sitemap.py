# -*- coding: utf-8 -*-
import scrapy


class SitemapSpider(scrapy.Spider):
    name = 'sitemap'
    # allowed_domains = ['example.com']
    # start_urls = ['http://example.com/']

    # sitemap_urls = ['https://wired.jp/sitemap.xml']

    # sitemap_follow = ['2018-10']

    # sitemap_rules = [(r'/2018/10/', 'parse')]

    # https://imabari.hateblo.jp/entry/2018/12/01/155452

    def parse(self, response):
        yield {
            'url': response.url,
            'title': response.css('title::text').extract_first(),
        }
