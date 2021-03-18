from scrapy.spiders import Spider
import sys
from scrapy.selector import Selector
from dirotop.items import Shopping, TopHundred, ShoppingData
sys.path.append("..")
# from dirtop.items import TopHundred
# from dirotop.items import { TopHundred, Shopping }


class ShoppingSpider (Spider):
    name = 'shop'
    allowed_domains = ['stopic.okhqb']
    start_urls = [
        'http://stopic.okhqb.com/xinren2016.html?utml=xrcelan#'
    ]

    def parse(self, response):
        res = response.css('div.content-three>ul.guide-title>li')
        i = 1
        items = []
        while i <= 4:
            res1 = response.css('div.content-three>ul.checkList' + str(i) + '>li')
            print('i', i)
            i += 1
            for item in res1:
                torrent = Shopping()
                torrent['urls'] = item.css('p>a::attr(href)').extract_first().strip()
                torrent['imgUrls'] = item.css('a.phone-img>img::attr(data-original)').extract_first().strip()
                torrent['title'] = item.css('a::text').extract_first().strip()
                items.append(torrent)
        return items


class TopVideo (Spider):
    name = 'video'
    allowed_domains = ['dy2018']
    start_urls = [
        'https://www.dy2018.com/'
    ]

    def parse(self, response):
        res = response.css('div.co_content222>ul>li')
        items = []
        for item in res:
            torrent = TopHundred()
            torrent['urls'] = item.css('a::attr(href)').extract_first().strip()
            torrent['title'] = item.css('a::text').extract_first().strip()
            torrent['time'] = item.css('span>font::text').extract_first().strip()
            items.append(torrent)
        return items
    # print('https://www.dy2018.com' + torrent['urls'], '>>>>>', torrent['title'], '>>>>>>>', torrent['time'])


class ShopData (Spider):
    name = 'shopdata'
    allowed_domains = ['d1sc']
    start_urls = [
        'https://www.d1sc.com/store_goods_list_18.html'
    ]

    def parse(self, response):
        res = response.css('div.smallgoods>ul')
        items = []
        for item in res:
            torrent = ShoppingData()
            torrent['imgUrls'] = item.css('li.goodsimg>span>p>a>img::attr(src)').extract_first().strip()
            torrent['title'] = item.css('li.goodsnames>a::text').extract_first().strip()
            torrent['urls'] = item.css('li.goodsnames>a::attr(href)').extract_first().strip()
            torrent['shopPrice'] = item.css('li.goodslook>strong::text').extract_first().strip()
            torrent['shopPrice'] = item.css('li.rencentgoodsok>strong::text').extract_first().strip()
        return items
