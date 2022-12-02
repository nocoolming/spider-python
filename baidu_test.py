import scrapy


class BaiduTestSpider(scrapy.Spider):
    name = 'baidu_test'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        print("Hello")
