# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import SitemapSpider as ParentSitemapSpider

class SitemapSpider(ParentSitemapSpider):
    name = 'sitemap'
    # allowed_domains = ['example.com']
    # start_urls = ['http://example.com/']

    sitemap_urls = [
        'https://wired.jp/sitemap.xml'
    ]

    sitemap_rules = [(r'/2019/04/', 'parse')]

    # def start_requests(self):
    #     requests = list(map(lambda x:x.replace(url=x.url.replace("https://", "http://")) ,list(super(SitemapSpider, self).start_requests())))
    #     for request in requests:
    #         print(request.url)
    #         # request.replace(url="https://www.google.co.jp/")
    #     return requests

    def parse(self, response):
        i = {}
        i['url'] = response.url
        i['status'] = response.status
        meta_tags = response.css('meta')
        for meta in meta_tags:
            i['content'] = meta.css("meta('content')").extract_first()
            i['name'] = meta.css("meta('content')").extarct_first()
            i['property'] = meta.css("meta('property')").extract_first()
            yield i
    # ref https://imabari.hateblo.jp/entry/2018/12/01/155452
