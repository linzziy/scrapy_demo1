# -*- coding: utf-8 -*-
import scrapy
from demo1.items import DoubanMovieItem

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']
    # allowed_domains = ['cip.cc']
    # start_urls = ['https://www.cip.cc/']

    def parse(self, response):
        movie_list = response.xpath("//div[@id='content']//ol/li")

        # 提取当前数据
        for m in movie_list:
            item = DoubanMovieItem()

            item['m_url']   = response.url
            item['m_index'] = m.xpath(".//div[@class='pic']//em/text()").get(-1)
            item['m_title'] = m.xpath(".//span[@class='title']/text()").extract_first("")
            item['m_score'] = m.xpath(".//div[@class='star']//span[@class='rating_num']/text()").get("")
            item['m_intro'] = m.xpath(".//span[@class='inq']/text()").get("")

            yield item

        # 处理下一页数据
        next_link = m.xpath("//span[@class='next']//a/@href").get()
        if next_link:
            yield scrapy.Request(url="https://movie.douban.com/top250"+next_link, callback=self.parse)