# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import SitemapSpider as ParentSitemapSpider

class SitemapSpider(ParentSitemapSpider):
    name = 'sitemap'
    allowed_domains = ['example.com']
    # start_urls = ['http://example.com/']

    sitemap_urls = ['https://wired.jp/sitemap.xml']

    sitemap_rules = [(r'/2018/10/', 'parse')]
    def parse(self, response):
        i = {}
        i['title'] = response.css(
            'article.article-detail > header > h1::text').extract_first()
        return i
    # ref https://imabari.hateblo.jp/entry/2018/12/01/155452
