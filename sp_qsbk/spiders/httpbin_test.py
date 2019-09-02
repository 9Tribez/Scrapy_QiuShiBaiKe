import scrapy


# 用于测试代理
class HttpbinTestSpider(scrapy.Spider):
    name = "httpbin_test"

    allowed_domains = ["httpbin.org"]

    start_urls = ['http://httpbin.org/get']

    def make_requests_from_url(self, url):
        self.logger.debug('Try first time')

        return scrapy.Request(url=url, meta={'download_timeout': 10}, callback=self.parse, dont_filter=False)

    def parse(self, response):
        print(response.text)