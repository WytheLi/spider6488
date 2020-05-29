# -*- coding: utf-8 -*-
import datetime
import json
import time
import uuid

import scrapy
from scrapy_splash import SplashRequest

from spider6488.common.common import compute_dt_chongq_ssc, compute_three_terms


class ChongqSscSpider(scrapy.Spider):
    name = 'chongq_ssc'
    allowed_domains = ['cqssc.17500.cn']
    start_urls = [
        # 重庆时时彩
        # 开奖号码
        'https://cqssc.17500.cn/tools/getwinlist.html',
        # 号码分布（即基本走势）
        'https://tools.17500.cn/tb/cqssc/hmfb?limit=100',
        # 龙虎走势
        'https://tools.17500.cn/tb/cqssc/lhh?limit=100',
    ]
    custom_settings = {
        'ITEM_PIPELINES': {'spider6488.pipelines.ChongqSscPipeline': 307}
    }

    def start_requests(self):
        """
        重写start_requests()方法
        将url给到Splash解析，同时指定回调方法
        :return:
        """
        # for url in self.start_urls[1:]:
        for url in self.start_urls:
            assets_type = url.split('/')[-1]
            if 'getwinlist.html' == assets_type:
                yield scrapy.Request(   # 直接给scrapy调度器处理
                    url=url,
                    callback=self.parse
                )
            else:
                yield SplashRequest(    # 先经过Splash解析，再让scrapy调度器处理
                    url=url,
                    callback=self.parse,
                    meta={},
                    args={
                        'wait': 1,
                    }
                )

    def parse(self, response):
        """
        https://cqssc.17500.cn/
        重庆时时彩
        开奖号码，号码分布，龙虎
        :param response:
        :return:
        """
        assets_type = response.url.split('/')[-1]
        if 'getwinlist.html' == assets_type:    # 开奖号码
            return self.lottery_number_parse(response)
        elif 'hmfb?limit=100' == assets_type:     # 号码分布（即基本走势）
            return self.trend_issue_parse(response)
        elif 'lhh?limit=100' == assets_type:      # 龙虎走势
            return self.trend_dt_parse(response)

    def lottery_number_parse(self, response):
        """
        开奖号码
        :param response:
        :return:
        """
        print(response.url)
        res = json.loads(response.text)
        for i in res['message']:
            now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            item = {
                'parse_type': 'lottery_number',
                'id': str(uuid.uuid4()).replace('-', ''),
                'lottery_code': '5012',
                'lottery_num': i['_issue'],
                'lottery_full_no': i['winnum'].replace(',', '-'),
                'lottery_sum_value': str(i['sum']) + '-' + ('a' if '大' == i['dx'] else 'b') + '-' + ('c' if '单' == i['ds'] else 'd'),
                # 龙虎 这里需要计算第一和最后一个数得到
                'reserved_bit_one': compute_dt_chongq_ssc(i['winnum'].split(',')) if i['winnum'] else "",
                'reserved_bit_four': compute_three_terms(i['winnum'].split(',')[:3]) + '-' + compute_three_terms(i['winnum'].split(',')[1:4]) + '-' + compute_three_terms(i['winnum'].split(',')[2:]) if i['winnum'] else "",
                'lottery_countdown': 1,
                'draw_date': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(i['time']))),
                'create_date': now_time,
                'update_date': now_time
            }
            yield item

    def trend_issue_parse(self, response):
        """
        号码分布（即基本走势）
        :param response:
        :return:
        """
        print(response.url)
        table = response.xpath("//tbody[@id='body']//tr")
        for tr in table[:-10]:
            # print(tr)
            # print(tr.xpath("./td[1]/text()").extract_first())
            # print('-'.join(tr.xpath("./td[2]/text()").extract_first()))
            # 号码分布 tr.xpath(".//td[@linenum='1']//text()").extract()
            first_seat = tr.xpath(".//td[@linenum='2']//text()").extract()
            second_seat = tr.xpath(".//td[@linenum='3']//text()").extract()
            third_seat = tr.xpath(".//td[@linenum='4']//text()").extract()
            fourthly_seat = tr.xpath(".//td[@linenum='5']//text()").extract()
            fifth_seat = tr.xpath(".//td[@linenum='6']//text()").extract()
            lot_num = tr.xpath("./td[1]/text()").extract_first()
            now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            _time = datetime.datetime.now().strftime('%H:%M:%S')
            item = {
                'parse_type': 'trend_issue',
                'id': str(uuid.uuid4()).replace('-', ''),
                'lottery_code': '5012',
                'lottery_num': lot_num,
                'lottery_full_no': '-'.join(tr.xpath("./td[2]/text()").extract_first()),
                'lottery_char_type': 4,
                'reserved_bit_one': '-'.join(first_seat),
                'reserved_bit_two': '-'.join(second_seat),
                'reserved_bit_three': '-'.join(third_seat),
                'reserved_bit_four': '-'.join(fourthly_seat),
                'reserved_bit_five': '-'.join(fifth_seat),
                'is_finish': 0,
                'draw_date': '%(y)s-%(m)s-%(d)s %(time)s' % {"y": lot_num[:4], 'm': lot_num[4:6], 'd': lot_num[6:8], 'time': _time},
                'create_date': now_time,
                'update_date': now_time
            }
            # print(item)
            yield item

    def trend_dt_parse(self, response):
        """
        龙虎走势
        :param response:
        :return:
        """
        print(response.url)
        table = response.xpath("//tbody[@id='body']//tr")
        for tr in table[:-10]:
            # print(tr.xpath("./td[1]/text()").extract_first())
            first_seat = tr.xpath(".//td[@linenum='2']//text()").extract()
            fifth_seat = tr.xpath(".//td[@linenum='3']//text()").extract()
            dt_code = tr.xpath(".//td[@linenum='4']//text()").extract()
            lot_num = tr.xpath("./td[1]/text()").extract_first()
            now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            _time = datetime.datetime.now().strftime('%H:%M:%S')
            item = {
                'parse_type': 'trend_dt',
                'id': str(uuid.uuid4()).replace('-', ''),
                'lottery_code': '5012',
                'lottery_num': lot_num,
                'lottery_full_no': '-'.join(tr.xpath("./td[2]/text()").extract_first()),
                'lottery_char_type': 6,
                'reserved_bit_one': '-'.join(first_seat),
                'reserved_bit_two': '-'.join(fifth_seat),
                'reserved_bit_three': '-'.join(dt_code).replace("龙", "1").replace("虎", "2").replace("和", "3"),
                'is_finish': 0,
                'draw_date': '%(y)s-%(m)s-%(d)s %(time)s' % {"y": lot_num[:4], 'm': lot_num[4:6], 'd': lot_num[6:8], 'time': _time},
                'create_date': now_time,
                'update_date': now_time
            }
            # print(item)
            yield item
