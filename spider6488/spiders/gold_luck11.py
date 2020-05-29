# -*- coding: utf-8 -*-
import datetime
import json
import uuid

import scrapy

from spider6488.common.common import sum_value_11x5, three_terms_11x5, dragon_tiger_11x5


class GoldLuck11Spider(scrapy.Spider):
    name = 'gold_luck11'
    allowed_domains = ['api.api861861.com']
    _today = datetime.datetime.now().strftime('%Y-%m-%d')
    start_urls = [
        # 十一运夺金
        # 开奖号码
        'https://api.api861861.com/ElevenFive/getElevenFiveList.do?date=%s&lotCode=10008' % _today,
        # 基本走势
        'https://api.api861861.com/ElevenFive/queryElevnFiveTrendByIssue.do?issue=90&date=&lotCode=10008',
        # 定位走势 修改num可以查看1-5求的数据
        'https://api.api861861.com/ElevenFive/queryElevnFiveLocalTrend.do?num=1&issue=90&date=&lotCode=10008',
        # 龙虎走势
        'https://api.api861861.com/ElevenFive/queryElevnFiveDTTrend.do?issue=90&date=&lotCode=10008',
        # 和值走势
        'https://api.api861861.com/ElevenFive/queryElevnFiveSumTrend.do?issue=90&date=&lotCode=10008',
    ]
    custom_settings = {
        'ITEM_PIPELINES': {'spider6488.pipelines.Com1680380_11x5Pipeline': 303}
    }

    def parse(self, response):
        """
        十一运夺金
        :param response:
        :return:
        """
        # print(response.url.split("/")[-1].split('?'))
        assets_type = response.url.split("/")[-1].split('?')[0]
        if 'getElevenFiveList.do' == assets_type:           # 开奖号码
            return self.lottery_number_parse(response)
        elif 'queryElevnFiveTrendByIssue.do' == assets_type:    # 基本走势
            return self.trend_by_issue_parse(response)
        elif 'queryElevnFiveLocalTrend.do' == assets_type:  # 定位走势
            return self.trend_local_parse(response)
        elif 'queryElevnFiveDTTrend.do' == assets_type:     # 龙虎走势
            return self.trend_dt_parse(response)
        elif 'queryElevnFiveSumTrend.do' == assets_type:    # 和值走势
            return self.trend_sum_parse(response)

    def lottery_number_parse(self, response):
        """
        开奖号码
        :param response:
        :return:
        """
        print(response.url)
        res = json.loads(response.text)
        for i in res['result']['data']:
            now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            item = {
                'parse_type': 'lottery_number',
                'id': str(uuid.uuid4()).replace('-', ''),
                'lottery_code': '2004',
                'lottery_num': i['preDrawIssue'],
                'lottery_full_no': i['preDrawCode'].replace(',', '-'),
                'lottery_sum_value': sum_value_11x5(i['sumNum'], i['sumSingleDouble'], i['sumBigSmall']),
                # 龙虎 0龙1虎 --> 1龙2虎
                'reserved_bit_one': 1 if 0 == i['dragonTiger'] else 2,
                # 三项
                'reserved_bit_two': three_terms_11x5(i['behindThree']),
                'reserved_bit_three': three_terms_11x5(i['betweenThree']),
                'reserved_bit_four': three_terms_11x5(i['lastThree']),
                'lottery_countdown': 1,
                'draw_date': i['preDrawTime'],
                'create_date': now_time,
                'update_date': now_time
            }
            # print(item)
            yield item

    def trend_by_issue_parse(self, response):
        """
        基本走势
        :param response:
        :return:
        """
        print(response.url)
        res = json.loads(response.text)
        if res['result']['data']:
            for i in res['result']['data'][0]['bodyList']:
                now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                _date = '20%(y)s-%(m)s-%(d)s' % {'y': i['issue'][:2], 'm': i['issue'][2:4], 'd': i['issue'][4:6]}
                _time = datetime.datetime.now().strftime("%H:%M:%S")
                item = {
                    'parse_type': 'trend_by_issue',
                    'id': str(uuid.uuid4()).replace('-', ''),
                    'lottery_code': '2004',
                    'lottery_num': i['issue'],
                    'lottery_full_no': i['code'].replace(',', '-'),
                    'lottery_char_type': 4,
                    # 第一、二、三、四、五球
                    'reserved_bit_one': ','.join([str(i) for i in i['array'][:11]]).replace('-', '').replace(',', '-'),
                    'reserved_bit_two': ','.join([str(i) for i in i['array'][11:22]]).replace('-', '').replace(',', '-'),
                    'reserved_bit_three': ','.join([str(i) for i in i['array'][22:33]]).replace('-', '').replace(',','-'),
                    'reserved_bit_four': ','.join([str(i) for i in i['array'][33:44]]).replace('-', '').replace(',','-'),
                    'reserved_bit_five': ','.join([str(i) for i in i['array'][44:]]).replace('-', '').replace(',', '-'),
                    'is_finish': 0,
                    'draw_date': _date + " " + _time,
                    'create_date': now_time,
                    'update_date': now_time
                }
                # print(item)
                yield item

    def trend_local_parse(self, response):
        """
        定位走势
        :param response:
        :return:
        """
        print(response.url)

    def trend_dt_parse(self, response):
        """
        龙虎走势
        :param response:
        :return:
        """
        print(response.url)
        res = json.loads(response.text)
        if res['result']['data']:
            for i in res['result']['data'][0]['bodyList']:
                now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                _date = '20%(y)s-%(m)s-%(d)s' % {'y': i['issue'][:2], 'm': i['issue'][2:4], 'd': i['issue'][4:6]}
                _time = datetime.datetime.now().strftime('%H:%M:%S')
                item = {
                    'parse_type': 'trend_dtt',
                    'id': str(uuid.uuid4()).replace('-', ''),
                    'lottery_code': '2004',
                    'lottery_num': i['issue'],
                    'lottery_full_no': i['code'].replace(',', '-'),
                    'lottery_char_type': 6,
                    'reserved_bit_one': ','.join([str(i) for i in i['array'][:11]]).replace('-', '').replace(',', '-'),
                    'reserved_bit_two': ','.join([str(i) for i in i['array'][11:22]]).replace('-', '').replace(',', '-'),
                    'reserved_bit_three': dragon_tiger_11x5(i['code'], i['array'][22:]),
                    'is_finish': 0,
                    'draw_date': _date + " " + _time,
                    'create_date': now_time,
                    'update_date': now_time
                }
                # print(item)
                yield item

    def trend_sum_parse(self, response):
        """
        和值走势
        :param response:
        :return:
        """
        print(response.url)
        res = json.loads(response.text)
        if res['result']['data']:
            for i in res['result']['data'][0]['bodyList']:
                now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                _date = '20%(y)s-%(m)s-%(d)s' % {'y': i['issue'][:2], 'm': i['issue'][2:4], 'd': i['issue'][4:6]}
                _time = datetime.datetime.now().strftime('%H:%M:%S')
                item = {
                    'parse_type': 'trend_sum',
                    'id': str(uuid.uuid4()).replace('-', ''),
                    'lottery_code': '2004',
                    'lottery_num': i['issue'],
                    'lottery_full_no': i['code'].replace(',', '-'),
                    'lottery_char_type': 3,
                    # 和值走势
                    'reserved_bit_one': ','.join([str(d_1) for d_1 in i['array'][:31]]).replace('-', '').replace(',', '-'),
                    'reserved_bit_two': i['array'][31],     # 和值
                    'reserved_bit_three': i['array'][32],  # 和尾
                    'is_finish': 0,
                    'draw_date': _date + " " + _time,
                    'create_date': now_time,
                    'update_date': now_time
                }
                # print(item)
                yield item
