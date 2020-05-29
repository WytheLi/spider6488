# -*- coding: utf-8 -*-
import datetime
import json
import time
import uuid

import scrapy

from spider6488.common.common import sum_value_kl8


class BeijingHappy8Spider(scrapy.Spider):
    name = 'beijing_happy8'
    allowed_domains = ['api.api861861.com']
    _today = datetime.datetime.today().strftime('%Y-%m-%d')
    start_urls = [
        # 北京快乐8
        # 开奖号码
        'https://api.api861861.com/LuckTwenty/getBaseLuckTwentyList.do?date=%s&lotCode=10014' % _today,
    ]
    custom_settings = {
        'ITEM_PIPELINES': {'spider6488.pipelines.BeijingHappy8Pipeline': 310}
    }

    # def start_requests(self):
    #     """
    #     重写start_requests()方法
    #     动态的指定爬取日期
    #     :return:
    #     """
    #     # for url in self.start_urls[1:]:
    #     for url in self.start_urls:
    #         yield scrapy.Request(   # 直接给scrapy调度器处理
    #             url=url.format(datetime.datetime.today().strftime('%Y-%m-%d')),
    #             callback=self.parse
    #         )

    def parse(self, response):
        print(response.url)
        res = json.loads(response.text)
        if res['result']['data']:
            for i in res['result']['data']:
                now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                item = {
                    'id': str(uuid.uuid4()).replace('-', ''),
                    'lottery_code': '2006',
                    'lottery_num': i['preDrawIssue'],
                    'lottery_full_no': i['preDrawCode'].replace(',', '-'),
                    # 和值 1大-1小 1单-1双  --> a大b小c单d双
                    'lottery_sum_value': sum_value_kl8(i['sumNum'], i['sumSingleDouble'], i['sumBigSmall']),
                    # 五行 1金2木3水4火5土
                    'reserved_bit_one': i['sumWuXing'],
                    'lottery_countdown': 1,
                    'draw_date': i['preDrawTime'],
                    'create_date': now_time,
                    'update_date': now_time
                }
                # print(item)
                yield item


