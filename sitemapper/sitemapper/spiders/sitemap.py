# -*- coding: utf-8 -*-
import scrapy


class SitemapSpider(scrapy.Spider):
    name = 'sitemap'
    allowed_domains = ['www.bbc.co.uk']
    sitemap_urls = [
        # ここにはrobots.txtのURLを指定してもよいが、
        # 無関係なサイトマップが多くあるので、今回はサイトマップのURLを直接指定する。
        'http://www.bbc.co.uk/news/sitemap.xml',
    ]
    sitemap_rules = [
        # 正規表現 '/news/' にマッチするページをparse_newsメソッドでパースする
        (r'/news/', 'parse'),
    ]

    def parse(self, response):
        yield {
            'url': response.url,
            'title': response.css('title::text').extract_first(),
        }
