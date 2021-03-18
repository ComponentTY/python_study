import scrapy
import requests
from tutorial.items import GoodsItem
class GoodsSpider(scrapy.Spider):
  name = 'goods'
  allowed_domains = ['m.vip.com']
  start_urls = ['https://m.vip.com/searchlist.html?q=fiveplus%E5%A5%B3%E8%A3%85%E4%B8%8A%E8%A1%A3&channel_id=']
  def parse(self, response):
        res = response.css('dl.u-product')
        for item in res:
          print(item.xpath())
          torrent = GoodsItem()
          pass
          torrent['name']= item.css('img::attr(src)').extract_first().strip()
          # torrent['goodsName'] = item.css('span.vip-price-wrapper::text()').extract_first().strip()
          # torrent['goodsPrice'] = item.css('span::text()').extract_first().strip()