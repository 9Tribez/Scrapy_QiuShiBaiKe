# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpQsbkItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    author = scrapy.Field()  # 作者
    article_id = scrapy.Field()  # 文章的id
    stats_time = scrapy.Field()  # 发布时间
    stats_vote = scrapy.Field()  # 人气
    content = scrapy.Field()  # 文章内容
    images = scrapy.Field()  # 文章中的图片
    video_link = scrapy.Field()  # 文章的视频链接
    comment = scrapy.Field()  # 文章中的评论
