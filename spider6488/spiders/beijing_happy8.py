# -*- coding: utf-8 -*-
import datetime
import json
import time
import uuid

import pymysql
import scrapy
from scrapy.utils.project import get_project_settings

from spider6488.common.common import sum_value_kl8, init_trend_sum_parse_bottom_bjkl8, \
    compute_trend_sum_parse_bottom_bjkl8

settings = get_project_settings()


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
            # for i in res['result']['data']:
            for i in res['result']['data'][::-1]:
                # 和值形态数据
                for item in self.trend_sum_parse(i):
                    yield item

                now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                item = {
                    'parse_type': 'lottery_number',
                    'id': str(uuid.uuid4()).replace('-', ''),
                    'lottery_code': '2006',
                    'lottery_num': i['preDrawIssue'],
                    'lottery_full_no': i['preDrawCode'].replace(',', '-'),
                    # 和值 1大-1小 1单-1双  --> a大b小c单d双
                    'lottery_sum_value': sum_value_kl8(i['sumNum'], i['sumSingleDouble'], i['sumBigSmall']),
                    # 五行 1金2木3水4火5土
                    'reserved_bit_one': i['sumWuXing'],
                    'lottery_countdown': 1,
                    'lottery_status': 1,
                    'draw_date': i['preDrawTime'],
                    'create_date': now_time,
                    'update_date': now_time
                }
                # print(item)
                yield item

    def trend_sum_parse(self, i):
        """
        和值走势
        :param i:
        :return:
        """
        conn = pymysql.connect(**settings['MYSQL_POOL_CONFIG'])
        cursor = conn.cursor()
        cursor.execute("""
            select lottery_full_no, reserved_bit_two
            from sc_lottery_char
            where lottery_code='2006'
            and lottery_char_type=3
            order by lottery_num desc 
            limit 1
        """)
        res = cursor.fetchone()
        # print(res)
        cursor.close()
        conn.close()
        # print(i['preDrawCode'].split(','))
        if not res:
            now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            item = {
                'parse_type': 'trend_sum',
                'id': str(uuid.uuid4()).replace('-', ''),
                'lottery_code': '2006',
                'lottery_num': i['preDrawIssue'],
                'lottery_full_no': i['preDrawCode'].replace(',', '-'),
                'lottery_char_type': 3,
                # 走势底号
                'reserved_bit_one': sum(map(lambda x: int(x), i['preDrawCode'].split(',')[:-1])),     # 和值
                'reserved_bit_two': init_trend_sum_parse_bottom_bjkl8(i['preDrawCode'].split(',')[:-1]),
                'is_finish': 0,
                'draw_date': i['preDrawTime'],
                'create_date': now_time,
                'update_date': now_time
            }
        else:
            now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            item = {
                'parse_type': 'trend_sum',
                'id': str(uuid.uuid4()).replace('-', ''),
                'lottery_code': '2006',
                'lottery_num': i['preDrawIssue'],
                'lottery_full_no': i['preDrawCode'].replace(',', '-'),
                'lottery_char_type': 3,
                # 走势底号
                'reserved_bit_one': sum(map(lambda x: int(x), i['preDrawCode'].split(',')[:-1])),     # 和值
                'reserved_bit_two': compute_trend_sum_parse_bottom_bjkl8(i['preDrawCode'].split(',')[:-1], res[1]),
                'is_finish': 0,
                'draw_date': i['preDrawTime'],
                'create_date': now_time,
                'update_date': now_time
            }
        yield item


