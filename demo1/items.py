# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanMovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    m_url = scrapy.Field()
    m_index = scrapy.Field()
    m_title = scrapy.Field()
    m_score = scrapy.Field()
    m_intro = scrapy.Field()
