# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class Demo1Pipeline:
    def process_item(self, item, spider):
        print('====================================:'+spider.name)
        text = "["+str(item['m_index'])+"]《"+item['m_title']+"》 - "+str(item['m_score'])+" - "+item['m_intro']
        print(item['m_url']+"\n")
        print(text)

        return item
