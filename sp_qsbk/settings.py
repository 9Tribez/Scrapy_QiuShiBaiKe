# -*- coding: utf-8 -*-

# Scrapy settings for sp_qsbk project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'sp_qsbk'

SPIDER_MODULES = ['sp_qsbk.spiders']
NEWSPIDER_MODULE = 'sp_qsbk.spiders'

# LOG_LEVEL = 'WARNING'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'sp_qsbk (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/76.0.3809.100 Safari/537.36',

}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'sp_qsbk.middlewares.SpQsbkSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'sp_qsbk.middlewares.SpQsbkDownloaderMiddleware': 543,
    'sp_qsbk.middlewares.ProxyMiddleware': 500,
    'sp_qsbk.middlewares.RandomUserAgentMiddleware': 520,
    # 设置不参与scrapy的自动重试的动作
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
    # 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': 600,
    'sp_qsbk.middlewares.AutoProxyDownloaderMiddleware': 601,
    # 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 750,

}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'sp_qsbk.pipelines.SpQsbkPipeline': 300,
    'sp_qsbk.pipelines.SaveMongodbPipeline': 400,
    # 'sp_qsbk.pipelines.SaveMysqlPipeline': 500,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# 禁用Cookies
COOKIES_ENABLED = False

# 延迟下载（/秒）
# DOWNLOAD_DELAY = 1.5

# The params of connecting the mongodb
MONGO_URI = 'mongodb://127.0.0.1:27017'
MONGO_DB = 'SpQsbk'

# The params of connecting the mysql
MYSQL_HOST = 'localhost'
MYSQL_PORT = 3306
MYSQL_DB_NAME = 'SPQSBK_DB'
MYSQL_USER = 'root'
MYSQL_PASSWORD = '1321'

# 状态码列表
PROXY_STATUS = [302, 403]
