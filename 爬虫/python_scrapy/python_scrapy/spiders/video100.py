from scrapy.spiders import Spider
from scrapy.selector import Selector

from python_scrapy.items import PythonScrapyItem


class DomSpider (Spider):
    name = 'top'
    allowed_domains = ['dy2018']
    start_urls = [
        'https://www.dy2018.com/'
    ]

    def parse(self, response):
        res = response.css('div.co_content222>ul>li')
        for item in res:
            torrent = PythonScrapyItem()
            torrent['urls']= item.css('a::attr(href)').extract_first().strip()
            torrent['title'] = item.css('a::text').extract_first().strip()
            torrent['time'] = item.css('span::text()').extract_first().strip()