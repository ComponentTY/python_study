# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field
import sys
sys.path.append("..")


class TopHundred(Item):
    # 电影天堂top100
    # define the fields for your item here like:
    # name = scrapy.Field()
    urls = Field()
    title = Field()
    time = Field()
    imgUrls = Field()


class Shopping(Item):
    # 华强北商城购物网站
    urls = Field()
    imgUrls = Field()
    title = Field()


class ShoppingData(Item):
    # 毕设数据
    urls: Field()
    imgUrls: Field()
    title: Field()
    shopPrice: Field()
    dealNum: Field()
