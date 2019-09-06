# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re
import json
from sp_qsbk.items import SpQsbkItem


class QsbkSpider(CrawlSpider):
    name = 'qsbk'
    allowed_domains = ['qiushibaike.com']
    start_urls = [
        'https://www.qiushibaike.com/',
        'https://www.qiushibaike.com/hot/',
        'https://www.qiushibaike.com/imgrank/',
        'https://www.qiushibaike.com/text/',
        'https://www.qiushibaike.com/pic/',
        'https://www.qiushibaike.com/textnew/',
    ]

    rules = (
        Rule(LinkExtractor(allow=r'/article/\d+'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'https://www.qiushibaike.com/hot/page/\d+/'), follow=True),
        Rule(LinkExtractor(allow=r'https://www.qiushibaike.com/imgrank/page/\d+/'), follow=True),
        Rule(LinkExtractor(allow=r'https://www.qiushibaike.com/text/page/\d+/'), follow=True),
        Rule(LinkExtractor(allow=r'https://www.qiushibaike.com/pic/page/\d+/'), follow=True),
        Rule(LinkExtractor(allow=r'https://www.qiushibaike.com/textnew/page/\d+/'), follow=True),
    )

    def parse_item(self, response):
        item = {}
        detail_page = response.xpath('//div[@id="content"]/div/div[@class="col1 new-style-col1"]')
        title = detail_page.xpath('./h1/text()').get().strip()
        author = re.search(r'(.*)的糗事.*', title, re.S)[1]
        article_id = detail_page.xpath('.//input[@id="articleCurrentLink"]/@value').get()
        stats_time = detail_page.xpath('./div[@class="stats"]/span[@class="stats-time"]/text()').get().strip()
        stats_vote = detail_page.xpath('./div[@class="stats"]/span[@class="stats-vote"]/i/text()').get()
        content = detail_page.xpath('.//div[@class="content"]/text()').get().strip()
        images_thumb = detail_page.xpath('.//div[@class="thumb"]/img/@src').getall()
        video_tag = detail_page.xpath('.//video[@id="article-video"]/source/@src').get()
        item['images'] = None
        item['video_link'] = None
        if images_thumb:
            images = []
            for image in images_thumb:
                images.append('http:' + image)
            item['images'] = images
        if video_tag:
            item['video_link'] = 'http:' + video_tag
        item['author'] = author
        item['article_id'] = article_id
        item['stats_time'] = stats_time
        item['stats_vote'] = stats_vote
        item['content'] = content
        comment_info = []
        page = 1
        yield scrapy.Request(url='https://www.qiushibaike.com/commentpage/{0}?page=1&count=10'.format(article_id), meta={'item': item, 'comment_info': comment_info, 'page': page}, callback=self.parse_comment)

    def parse_comment(self, response):
        item = response.meta['item']
        article_id = item['article_id']
        comment_info = response.meta['comment_info']
        page = response.meta['page']
        text = str(json.loads(response.text))
        total_pattern = re.compile(r".*?'total': (\d+).*?", re.S)
        total = re.search(total_pattern, text).group(1)
        total_num = int(total) // 10 + 1
        if page == total_num:
            item['comment'] = comment_info
            spqsbk_item = SpQsbkItem(
                author=item['author'],
                article_id=item['article_id'],
                stats_time=item['stats_time'],
                stats_vote=item['stats_vote'],
                content=item['content'],
                images=item['images'],
                video_link=item['video_link'],
                comment=item['comment']
            )
            yield spqsbk_item
        else:
            comment_pattern = re.compile(r".*?'content': '(.*?)'.*?'login': '(.*?)'.*?", re.S)
            comment_list = re.findall(comment_pattern, text)
            for comment in comment_list:
                comment_dict = {
                    'comment_content': comment[0],
                    'comment_author': comment[1]
                }
                comment_info.append(comment_dict)
            page += 1
            yield scrapy.Request(url='https://www.qiushibaike.com/commentpage/{0}?page={1}&count=10'.format(article_id, page), meta={'item': item, 'comment_info': comment_info, 'page': page}, callback=self.parse_comment)
