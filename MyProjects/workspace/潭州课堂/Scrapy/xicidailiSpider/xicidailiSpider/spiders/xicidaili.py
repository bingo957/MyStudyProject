# -*- coding: utf-8 -*-
import scrapy
##from scrapy.spidermiddlewares.httperror import HttpError
# from twisted.internet.error import DNSLookupError
# from twisted.internet.error import TimeoutError

# 创建爬虫类 继承自scrapy.Spider -> 最基础的类 另外几个类都是继承自这个类
class XicidailiSpider(scrapy.Spider):
    name = 'xicidaili' # 爬虫名字，必须唯一
    allowed_domains = ["xicidaili.com"] # 允许采集的网站
    start_urls = ['http://xicidaili.com/nn/1'] # 开始采集的网站
    # start_urls = [f'http://xicidaili.com/nn/{page}' for page in range(1,3741)]  # 开始采集的网站,网页总数不变
    # 解析相应数据，提取数据或网址等 response 就是网页源码
    def parse(self, response):
        # 提取数据

        # 提取IP PORT
        selectors = response.xpath('//tr') # 选择所有tr标签
        # 循环遍历tr标签下的td标签
        for selector in selectors:
            ip = selector.xpath('./td[2].text()').get() # .表示是在当前目录下
            port = selector.xpath('./td[3].text()').get()
            # ip = selector.xpath('./td[2].text()').extract_first()  # 与上边方法等价
            # port = selector.xpath('./td[3].text()').extract_first()
            print(ip, port)
            # items = {
             #   'ip' : ip,
              #  'port' : port
            #}
            # yield items
        # 翻页操作
        next_page = response.xpath('//a[@class = "next_page"]/@href').get()
        if next_page:
            # 拼接网址
            # next_url = 'http://xicidaili.com' + next_page
            next_url = response.urljoin('http://xicidaili.com', next_page)
            # 再次发出请求 callback是回调函数 就是将请求得到的响应交给自己处理
            yield scrapy.Request(next_url, callback=self.parse)
            # yield scrapy.Request(next_url, callback=self.parse, errback=self.errback_xicidaili)

    """def errback_xicidaili(self, failure):
        # log all errback failures,
        # in case you want to do something special for some errors,
        # you may need the failure's type
        self.logger.error(repr(failure))

        if failure.check(HttpError):
            # you can get the response
            response = failure.value.response
            self.logger.error('HttpError on %s', response.url)

        elif failure.check(DNSLookupError):
            # this is the original request
            request = failure.request
            self.logger.error('DNSLookupError on %s', request.url)

        elif failure.check(TimeoutError):
            request = failure.request
            self.logger.error('TimeoutError on %s', request.url)
        """
# 此代码报错twisted.internet.error.DNSLookupError: DNS lookup failed: no results for hostname lookup: xicidaili.com.
# 网上增加errback的方法也不行
