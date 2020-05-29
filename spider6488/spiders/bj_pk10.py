# -*- coding: utf-8 -*-
import scrapy


class BjPk10Spider(scrapy.Spider):
    name = 'bj_pk10'
    allowed_domains = ['api.api861861.com']
    start_urls = [
        # 北京pk10
        # 开奖号码
        'https://api.api861861.com/pks/getPksHistoryList.do?lotCode=10001',
        # 号码走势
        'https://api.api861861.com/pks/queryDrawCodeTrend.do?date=&periods=90&lotCode=10001',
        # 冠亚和走势
        'https://api.api861861.com/pks/queryGysumTrend.do?date=&periods=90&lotCode=10001',
    ]

    def parse(self, response):
        """

        :param response:
        :return:
        """
        pass
