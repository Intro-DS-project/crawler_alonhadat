# Scrapy settings for crawler_alonhadat project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "crawler_alonhadat"

SPIDER_MODULES = ["crawler_alonhadat.spiders"]
NEWSPIDER_MODULE = "crawler_alonhadat.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "crawler_alonhadat (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 4

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Retry many times since proxies often fail
# RETRY_TIMES = 10


# Proxy list containing entries like
# http://username:password@ip:port
# PROXY_LIST = [
#     '188.74.210.207:6286:sxwgbmxt:3e2ws8klwh3r',
#     '188.74.183.10:8279:sxwgbmxt:3e2ws8klwh3r',
#     '188.74.210.21:6100:sxwgbmxt:3e2ws8klwh3r',
#     '45.155.68.129:8133:sxwgbmxt:3e2ws8klwh3r',
#     '154.95.36.199:6893:sxwgbmxt:3e2ws8klwh3r',
#     '45.94.47.66:8110:sxwgbmxt:3e2ws8klwh3r'
# ]


# Proxy mode
# 0 = Every requests have different proxy
# 1 = Take only one proxy from the list and use it
# 2 = Put a custom proxy to use in the settings
# PROXY_MODE = 0
# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
   "Accept-Language": "en",
}


USER_AGENT_LIST = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'
]



# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    "crawler_alonhadat.middlewares.CrawlerAlonhadatSpiderMiddleware": 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#       'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
#    "crawler_alonhadat.middlewares.CrawlerAlonhadatDownloaderMiddleware": 543,
# }


# DOWNLOADER_MIDDLEWARES = {
#     'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
#     'crawler_alonhadat.middlewares.RandomUserAgentMiddleware': 400,
#     'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
#     'crawler_alonhadat.middlewares.ProxyMiddleware': 100,
#        "crawler_alonhadat.middlewares.CrawlerAlonhadatDownloaderMiddleware": 543
# }



# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    "crawler_alonhadat.pipelines.CrawlerAlonhadatPipeline": 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
