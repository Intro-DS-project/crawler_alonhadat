# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from scrapy.exceptions import CloseSpider


class CrawlerAlonhadatSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


from w3lib.http import basic_auth_header
import random


class CrawlerAlonhadatDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        # proxy = random.choice(proxyPools).split(":")
        # httpsProxy = proxy[0]
        # portProxy = proxy[1]
        # usernameProxy = proxy[2]
        # passwordProxy = proxy[3]

        # print("connect to proxy {}".format(proxy))

        # request.meta['proxy'] = "http://" + httpsProxy + ":" + portProxy
        # request.headers['Proxy-Authorization'] = basic_auth_header(usernameProxy, passwordProxy) 
        return None


    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)



# class CheckAuthenticationCloseSpider:
#     def process_response(self, request, response, spider):
#         if "xac-thuc-nguoi-dung.html" in response.url:
#             raise CloseSpider("Authentication required")
#         return response

class RandomUserAgentMiddleware(object):
    def __init__(self, user_agent_list):
        self.user_agent_list = user_agent_list

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            user_agent_list=crawler.settings.get('USER_AGENT_LIST')
        )

    def process_request(self, request, spider):
        request.headers['User-Agent'] = random.choice(self.user_agent_list)

# class ProxyMiddleware(object):
#     def __init__(self, proxy_list, proxy_mode, custom_proxy):
#         self.proxy_list = proxy_list
#         self.proxy_mode = proxy_mode
#         self.custom_proxy = custom_proxy

#     @classmethod
#     def from_crawler(cls, crawler):
#         return cls(
#             proxy_list=crawler.settings.get('PROXY_LIST'),
#             proxy_mode=crawler.settings.get('PROXY_MODE'),
#             custom_proxy=crawler.settings.get('CUSTOM_PROXY')
#         )

#     def process_request(self, request, spider):
#         if self.proxy_mode == 0:
#             proxy = random.choice(self.proxy_list)
#         elif self.proxy_mode == 1:
#             proxy = self.proxy_list[0]
#         elif self.proxy_mode == 2:
#             proxy = self.custom_proxy
#         else:
#             proxy = None

#         if proxy:
#             # Tách các phần của proxy
#             parts = proxy.split(':')
#             if len(parts) == 4:
#                 ip_port = f"{parts[0]}:{parts[1]}"
#                 username_password = f"{parts[2]}:{parts[3]}"
#                 request.meta['proxy'] = f"http://{username_password}@{ip_port}"
#             else:
#                 spider.logger.error(f"Invalid proxy format: {proxy}")