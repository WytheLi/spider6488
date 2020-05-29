# -*- coding: utf-8 -*-

# Scrapy settings for spider6488 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import pymysql

BOT_NAME = 'spider6488'

SPIDER_MODULES = ['spider6488.spiders']
NEWSPIDER_MODULE = 'spider6488.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
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
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
   'spider6488.middlewares.Spider6488SpiderMiddleware': 543,

    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'spider6488.middlewares.Spider6488DownloaderMiddleware': 543,

    # Splash
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'spider6488.pipelines.Spider6488Pipeline': 300,
#}

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
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# log
LOG_LEVEL = 'WARNING'
# LOG_FILE = 'logs/spider6488.log'

# scrapy启动多个爬虫配置 [scrapy crawlall运行]
COMMANDS_MODULE = 'spider6488.commands'

# Splash
SPLASH_URL = 'http://47.101.37.196:8050/'
# 去重类
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
# Cache存储
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'

# mysql
MYSQL_POOL_CONFIG = {   # test for use db
    'host': '192.168.10.15',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'database': 'test',
    # 'cursorclass': pymysql.cursors.DictCursor,   # 默认 pymysql.cursors.Cursor
    'autocommit': 'True',       # default False
    'connect_timeout': 30,      # default 10s
}

# MYSQL_POOL_CONFIG = {   # online for use db
#     # 'host': '152.32.240.219',
#     'host': '10.7.191.163',
#     'port': 5001,
#     'user': 'root',
#     'password': 'lsbb6488.',
#     'database': '6488v3',
#     # 'cursorclass': pymysql.cursors.DictCursor,   # 默认 pymysql.cursors.Cursor
#     'autocommit': 'True',       # default False
#     'connect_timeout': 30,      # default 10s
# }

# MYSQL_POOL_CONFIG = {   # 个人电脑
#     'host': '127.0.0.1',
#     'port': 3306,
#     'user': 'root',
#     'password': 'mysql',
#     'database': 'xh6488v3',
#     # 'cursorclass': pymysql.cursors.DictCursor,   # 默认 pymysql.cursors.Cursor
#     'autocommit': 'True',       # default False
#     'connect_timeout': 30,      # default 10s
# }




