# -*- coding: utf-8 -*-
import datetime
import importlib
import json
import logging
import uuid

import scrapy

from spider6488.common.common import sum_value_k3, tag_lot_no_tq_k3, tag_lot_no_big_and_small_k3, big_small_trend_k3, \
    sum_value_form_k3, num_form_k3, odd_even_k3, odd_even_compare_k3
from spider6488.common.constants import lottery_code_map


# 为了动态获取时间，从日志模块中获取
# _date = logging.time.strftime('%Y-%m-%d')
# print(_date)


class Com1680380K3Spider(scrapy.Spider):
    name = 'com1680380_k3'
    allowed_domains = ['api.api861861.com']
    _today = datetime.datetime.today().strftime('%Y-%m-%d')
    start_urls = [
        # 安徽快3
        # 开奖号码
        'https://api.api861861.com/lotteryJSFastThree/getJSFastThreeList.do?date=%s&lotCode=10030' % _today,
        # 定位走势
        'https://api.api861861.com/lotteryJSFastThree/queryOrientationTrend.do?date=&issue=&periods=30&lotCode=10030',
        # 大小走势
        'https://api.api861861.com/lotteryJSFastThree/queryBigAndSmallTrend.do?date=&issue=&periods=30&lotCode=10030',
        # 和值走势
        'https://api.api861861.com/lotteryJSFastThree/querySumTrend.do?date=&issue=&periods=30&lotCode=10030',
        # 基本走势
        'https://api.api861861.com/lotteryJSFastThree/queryBasicTrend.do?date=&issue=&periods=30&lotCode=10030',
        # 奇偶走势
        'https://api.api861861.com/lotteryJSFastThree/queryOddAndEvenTrend.do?date=&issue=&periods=30&lotCode=10030',

        # 北京快3
        # 开奖号码
        'https://api.api861861.com/lotteryJSFastThree/getJSFastThreeList.do?date=%s&lotCode=10033' % _today,
        # 定位走势
        'https://api.api861861.com/lotteryJSFastThree/queryOrientationTrend.do?date=&issue=&periods=30&lotCode=10033',
        # 大小走势
        'https://api.api861861.com/lotteryJSFastThree/queryBigAndSmallTrend.do?date=&issue=&periods=30&lotCode=10033',
        # 和值走势
        'https://api.api861861.com/lotteryJSFastThree/querySumTrend.do?date=&issue=&periods=30&lotCode=10033',
        # 基本走势
        'https://api.api861861.com/lotteryJSFastThree/queryBasicTrend.do?date=&issue=&periods=30&lotCode=10033',
        # 奇偶走势
        'https://api.api861861.com/lotteryJSFastThree/queryOddAndEvenTrend.do?date=&issue=&periods=30&lotCode=10033',

        # # 福建快3
        # # 开奖号码
        # 'https://api.api861861.com/lotteryJSFastThree/getJSFastThreeList.do?date=%s&lotCode=10031' % _today,
        # # 定位走势
        # 'https://api.api861861.com/lotteryJSFastThree/queryOrientationTrend.do?date=&issue=&periods=30&lotCode=10031',
        # # 大小走势
        # 'https://api.api861861.com/lotteryJSFastThree/queryBigAndSmallTrend.do?date=&issue=&periods=30&lotCode=10031',
        # # 和值走势
        # 'https://api.api861861.com/lotteryJSFastThree/querySumTrend.do?date=&issue=&periods=30&lotCode=10031',
        # # 基本走势
        # 'https://api.api861861.com/lotteryJSFastThree/queryBasicTrend.do?date=&issue=&periods=30&lotCode=10031',
        # # 奇偶走势
        # 'https://api.api861861.com/lotteryJSFastThree/queryOddAndEvenTrend.do?date=&issue=&periods=30&lotCode=10031',

        # 甘肃快3
        # 开奖号码
        'https://api.api861861.com/lotteryJSFastThree/getJSFastThreeList.do?date=%s&lotCode=10063' % _today,
        # 定位走势
        'https://api.api861861.com/lotteryJSFastThree/queryOrientationTrend.do?date=&issue=&periods=30&lotCode=10063',
        # 大小走势
        'https://api.api861861.com/lotteryJSFastThree/queryBigAndSmallTrend.do?date=&issue=&periods=30&lotCode=10063',
        # 和值走势
        'https://api.api861861.com/lotteryJSFastThree/querySumTrend.do?date=&issue=&periods=30&lotCode=10063',
        # 基本走势
        'https://api.api861861.com/lotteryJSFastThree/queryBasicTrend.do?date=&issue=&periods=30&lotCode=10063',
        # 奇偶走势
        'https://api.api861861.com/lotteryJSFastThree/queryOddAndEvenTrend.do?date=&issue=&periods=30&lotCode=10063',

        # 广西快3
        # 开奖号码
        'https://api.api861861.com/lotteryJSFastThree/getJSFastThreeList.do?date=%s&lotCode=10026' % _today,
        # 定位走势
        'https://api.api861861.com/lotteryJSFastThree/queryOrientationTrend.do?date=&issue=&periods=30&lotCode=10026',
        # 大小走势
        'https://api.api861861.com/lotteryJSFastThree/queryBigAndSmallTrend.do?date=&issue=&periods=30&lotCode=10026',
        # 和值走势
        'https://api.api861861.com/lotteryJSFastThree/querySumTrend.do?date=&issue=&periods=30&lotCode=10026',
        # 基本走势
        'https://api.api861861.com/lotteryJSFastThree/queryBasicTrend.do?date=&issue=&periods=30&lotCode=10026',
        # 奇偶走势
        'https://api.api861861.com/lotteryJSFastThree/queryOddAndEvenTrend.do?date=&issue=&periods=30&lotCode=10026',

        # 贵州快3
        # 开奖号码
        'https://api.api861861.com/lotteryJSFastThree/getJSFastThreeList.do?date=%s&lotCode=10062' % _today,
        # 定位走势
        'https://api.api861861.com/lotteryJSFastThree/queryOrientationTrend.do?date=&issue=&periods=30&lotCode=10062',
        # 大小走势
        'https://api.api861861.com/lotteryJSFastThree/queryBigAndSmallTrend.do?date=&issue=&periods=30&lotCode=10062',
        # 和值走势
        'https://api.api861861.com/lotteryJSFastThree/querySumTrend.do?date=&issue=&periods=30&lotCode=10062',
        # 基本走势
        'https://api.api861861.com/lotteryJSFastThree/queryBasicTrend.do?date=&issue=&periods=30&lotCode=10062',
        # 奇偶走势
        'https://api.api861861.com/lotteryJSFastThree/queryOddAndEvenTrend.do?date=&issue=&periods=30&lotCode=10062',

        # 河北快3
        # 开奖号码
        'https://api.api861861.com/lotteryJSFastThree/getJSFastThreeList.do?date=%s&lotCode=10028' % _today,
        # 定位走势
        'https://api.api861861.com/lotteryJSFastThree/queryOrientationTrend.do?date=&issue=&periods=30&lotCode=10028',
        # 大小走势
        'https://api.api861861.com/lotteryJSFastThree/queryBigAndSmallTrend.do?date=&issue=&periods=30&lotCode=10028',
        # 和值走势
        'https://api.api861861.com/lotteryJSFastThree/querySumTrend.do?date=&issue=&periods=30&lotCode=10028',
        # 基本走势
        'https://api.api861861.com/lotteryJSFastThree/queryBasicTrend.do?date=&issue=&periods=30&lotCode=10028',
        # 奇偶走势
        'https://api.api861861.com/lotteryJSFastThree/queryOddAndEvenTrend.do?date=&issue=&periods=30&lotCode=10028',

        # 湖北快3
        # 开奖号码
        'https://api.api861861.com/lotteryJSFastThree/getJSFastThreeList.do?date=%s&lotCode=10032' % _today,
        # 定位走势
        'https://api.api861861.com/lotteryJSFastThree/queryOrientationTrend.do?date=&issue=&periods=30&lotCode=10032',
        # 大小走势
        'https://api.api861861.com/lotteryJSFastThree/queryBigAndSmallTrend.do?date=&issue=&periods=30&lotCode=10032',
        # 和值走势
        'https://api.api861861.com/lotteryJSFastThree/querySumTrend.do?date=&issue=&periods=30&lotCode=10032',
        # 基本走势
        'https://api.api861861.com/lotteryJSFastThree/queryBasicTrend.do?date=&issue=&periods=30&lotCode=10032',
        # 奇偶走势
        'https://api.api861861.com/lotteryJSFastThree/queryOddAndEvenTrend.do?date=&issue=&periods=30&lotCode=10032',

        # 吉林快3
        # 开奖号码
        'https://api.api861861.com/lotteryJSFastThree/getJSFastThreeList.do?date=%s&lotCode=10027' % _today,
        # 定位走势
        'https://api.api861861.com/lotteryJSFastThree/queryOrientationTrend.do?date=&issue=&periods=30&lotCode=10027',
        # 大小走势
        'https://api.api861861.com/lotteryJSFastThree/queryBigAndSmallTrend.do?date=&issue=&periods=30&lotCode=10027',
        # 和值走势
        'https://api.api861861.com/lotteryJSFastThree/querySumTrend.do?date=&issue=&periods=30&lotCode=10027',
        # 基本走势
        'https://api.api861861.com/lotteryJSFastThree/queryBasicTrend.do?date=&issue=&periods=30&lotCode=10007',
        # 奇偶走势
        'https://api.api861861.com/lotteryJSFastThree/queryOddAndEvenTrend.do?date=&issue=&periods=30&lotCode=10027',

        # 江苏快3
        # 开奖号码
        'https://api.api861861.com/lotteryJSFastThree/getJSFastThreeList.do?date=%s&lotCode=10007' % _today,
        # 定位走势
        'https://api.api861861.com/lotteryJSFastThree/queryOrientationTrend.do?date=&issue=&periods=90&lotCode=10007',
        # 大小走势
        'https://api.api861861.com/lotteryJSFastThree/queryBigAndSmallTrend.do?date=&issue=&periods=90&lotCode=10007',
        # 和值走势
        'https://api.api861861.com/lotteryJSFastThree/querySumTrend.do?date=&issue=&periods=90&lotCode=10007',
        # 基本走势
        'https://api.api861861.com/lotteryJSFastThree/queryBasicTrend.do?date=&issue=&periods=90&lotCode=10007',
        # 奇偶走势
        'https://api.api861861.com/lotteryJSFastThree/queryOddAndEvenTrend.do?date=&issue=&periods=90&lotCode=10007',

        # # 内蒙古快3
        # # 开奖号码
        # 'https://api.api861861.com/lotteryJSFastThree/getJSFastThreeList.do?date=%s&lotCode=10029' % _today,
        # # 定位走势
        # 'https://api.api861861.com/lotteryJSFastThree/queryOrientationTrend.do?date=&issue=&periods=30&lotCode=10029',
        # # 大小走势
        # 'https://api.api861861.com/lotteryJSFastThree/queryBigAndSmallTrend.do?date=&issue=&periods=30&lotCode=10029',
        # # 和值走势
        # 'https://api.api861861.com/lotteryJSFastThree/querySumTrend.do?date=&issue=&periods=30&lotCode=10029',
        # # 基本走势
        # 'https://api.api861861.com/lotteryJSFastThree/queryBasicTrend.do?date=&issue=&periods=30&lotCode=10029',
        # # 奇偶走势
        # 'https://api.api861861.com/lotteryJSFastThree/queryOddAndEvenTrend.do?date=&issue=&periods=30&lotCode=10029',

        # 上海快3
        # 开奖号码
        'https://api.api861861.com/lotteryJSFastThree/getJSFastThreeList.do?date=%s&lotCode=10061' % _today,
        # 定位走势
        'https://api.api861861.com/lotteryJSFastThree/queryOrientationTrend.do?date=&issue=&periods=30&lotCode=10061',
        # 大小走势
        'https://api.api861861.com/lotteryJSFastThree/queryBigAndSmallTrend.do?date=&issue=&periods=30&lotCode=10061',
        # 和值走势
        'https://api.api861861.com/lotteryJSFastThree/querySumTrend.do?date=&issue=&periods=30&lotCode=10061',
        # 基本走势
        'https://api.api861861.com/lotteryJSFastThree/queryBasicTrend.do?date=&issue=&periods=30&lotCode=10061',
        # 奇偶走势
        'https://api.api861861.com/lotteryJSFastThree/queryOddAndEvenTrend.do?date=&issue=&periods=30&lotCode=10061',
    ]
    custom_settings = {
        'ITEM_PIPELINES': {'spider6488.pipelines.Com1680380K3Pipeline': 304}
    }

    def parse(self, response):
        """
        快3
        :param response:
        :return:
        """
        # print(response.url.split("/")[-1].split('?'))
        assets_type = response.url.split("/")[-1].split('?')[0]
        if 'getJSFastThreeList.do' == assets_type:      # 开奖号码
            return self.lottery_number_parse(response)
        elif 'queryOrientationTrend.do' == assets_type:   # 定位走势
            return self.trend_qrientation_parse(response)
        elif 'queryBigAndSmallTrend.do' == assets_type:   # 大小走势
            return self.trend_big_and_small_parse(response)
        elif 'querySumTrend.do' == assets_type:         # 和值走势
            return self.trend_sum_parse(response)
        elif 'queryBasicTrend.do' == assets_type:        # 基本走势
            return self.trend_basic_parse(response)
        elif 'queryOddAndEvenTrend.do' == assets_type:      # 奇偶走势
            return self.trend_odd_and_even_parse(response)

    def lottery_number_parse(self, response):
        """
        开奖号码
        :param response:
        :return:
        """
        print(response.url)
        res = json.loads(response.text)
        if res['result']['data']:
            for i in res['result']['data']:
                now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                item = {
                    'parse_type': 'lottery_number',
                    'id': str(uuid.uuid4()).replace('-', ''),
                    'lottery_code': lottery_code_map[response.url.split('=')[-1]],
                    'lottery_num': i['preDrawIssue'],
                    'lottery_full_no': i['preDrawCode'].replace(',', '-'),
                    # 总和 0大1小2通吃，0单1双2通吃 --> a大b小c单d双f通吃
                    'lottery_sum_value': sum_value_k3(i['sumNum'], i['sumSingleDouble'], i['sumBigSmall']),
                    # 龙虾蟹 1鱼2虾3葫芦4金钱5蟹6鸡7通吃
                    'reserved_bit_one': str(i['firstSeafood']) + '-' + str(i['secondSeafood']) + '-' + str(i['thirdSeafood']),
                    'lottery_countdown': 1,
                    'draw_date': i['preDrawTime'],
                    'create_date': now_time,
                    'update_date': now_time
                }
                # print(item)
                yield item

    def trend_qrientation_parse(self, response):
        """
        定位走势
        :param response:
        :return:
        """
        print(response.url)
        res = json.loads(response.text)
        if res['result']['data']:
            for i in res['result']['data']['bodyList']:
                now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                # _today = '%(y)s-%(m)s-%(d)s' % {'y': str(i['preIssue'])[:4], 'm': str(i['preIssue'])[4:6], 'd': str(i['preIssue'])[6:8]}
                # _time = now_time[11:]
                item = {
                    'parse_type': 'trend_qrientation',
                    'id': str(uuid.uuid4()).replace('-', ''),
                    'lottery_code': lottery_code_map[response.url.split('=')[-1]],
                    'lottery_num': i['preIssue'],
                    'lottery_full_no': '-'.join(map(lambda x: str(x), i['drawCode'])),
                    'lottery_char_type': 1,
                    'reserved_bit_one': tag_lot_no_tq_k3(i['drawCode'], i['oneCode'], 1),
                    'reserved_bit_two': tag_lot_no_tq_k3(i['drawCode'], i['twoCode'], 2),
                    'reserved_bit_three': tag_lot_no_tq_k3(i['drawCode'], i['threeCode'], 3),
                    'is_finish': 0,
                    'draw_date': now_time,
                    'create_date': now_time,
                    'update_date': now_time

                }
                # print(item)
                yield item

    def trend_big_and_small_parse(self, response):
        """
        大小走势
        :param response:
        :return:
        """
        print(response.url)
        res = json.loads(response.text)
        if res['result']['data']:
            for i in res['result']['data']['bodyList']:
                now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                # _today = '%(y)s-%(m)s-%(d)s' % {'y': str(i['preIssue'])[:4], 'm': str(i['preIssue'])[4:6], 'd': str(i['preIssue'])[6:8]}
                # _time = now_time[11:]
                item = {
                    'parse_type': 'trend_big_and_small',
                    'id': str(uuid.uuid4()).replace('-', ''),
                    'lottery_code': lottery_code_map[response.url.split('=')[-1]],
                    'lottery_num': i['preIssue'],
                    'lottery_full_no': '-'.join(map(lambda x: str(x), i['drawCode'])),
                    'lottery_char_type': 2,
                    # 开奖号码分布
                    'reserved_bit_one': ','.join([str(num) for num in i['numberDistribution']]).replace('-', '').replace(',', '-'),
                    # 百位，十位，个位大小
                    'reserved_bit_two': tag_lot_no_big_and_small_k3(i['drawCode'], i['hundredForm'], 1),
                    'reserved_bit_three': tag_lot_no_big_and_small_k3(i['drawCode'], i['tenForm'], 2),
                    'reserved_bit_four': tag_lot_no_big_and_small_k3(i['drawCode'], i['unitForm'], 3),
                    # 大小比走势
                    'reserved_bit_five': big_small_trend_k3(i['sizeCompare']),
                    # 大数个数
                    'reserved_bit_six': (','.join([str(b) for b in i['bigNumber']]).replace('-', '')).replace(",", "-"),
                    # 小数个数
                    'reserved_bit_seven': (','.join([str(s) for s in i['smallNumber']]).replace('-', '')).replace(",", "-"),
                    'is_finish': 0,
                    'draw_date': now_time,
                    'create_date': now_time,
                    'update_date': now_time,
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
            for i in res['result']['data']['bodyList']:
                now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                # _today = '%(y)s-%(m)s-%(d)s' % {'y': str(i['preIssue'])[:4], 'm': str(i['preIssue'])[4:6], 'd': str(i['preIssue'])[6:8]}
                # _time = now_time[11:]
                item = {
                    'parse_type': 'trend_sum',
                    'id': str(uuid.uuid4()).replace('-', ''),
                    'lottery_code': lottery_code_map[response.url.split('=')[-1]],
                    'lottery_num': i['preIssue'],
                    'lottery_full_no': '-'.join(map(lambda x: str(x), i['drawCode'])),
                    'lottery_char_type': 3,
                    'reserved_bit_one': ('{},{}'.format(i['sumTotal'], ','.join([str(sum) for sum in i['sumNum'][:-4]]).replace('-', ''))).replace(",","-"),
                    'reserved_bit_two': sum_value_form_k3(i['sumTotal'], i['sumNum'][-4:]),
                    'is_finish': 0,
                    'draw_date': now_time,
                    'create_date': now_time,
                    'update_date': now_time
                }
                # print(item)
                yield item

    def trend_basic_parse(self, response):
        """
        基本走势
        :param response:
        :return:
        """
        print(response.url)
        res = json.loads(response.text)
        if res['result']['data']:
            for i in res['result']['data']['bodyList']:
                now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                # _today = '%(y)s-%(m)s-%(d)s' % {'y': str(i['preIssue'])[:4], 'm': str(i['preIssue'])[4:6], 'd': str(i['preIssue'])[6:8]}
                # _time = now_time[11:]
                item = {
                    'parse_type': 'trend_basic',
                    'id': str(uuid.uuid4()).replace('-', ''),
                    'lottery_code': lottery_code_map[response.url.split('=')[-1]],
                    'lottery_num': i['preIssue'],
                    'lottery_full_no': '-'.join(map(lambda x: str(x), i['drawCode'])),
                    'lottery_char_type': 4,
                    # 开奖号码分布
                    'reserved_bit_one': ','.join([str(d) for d in i['distribution']]).replace('-', '').replace(",", "-"),
                    # 号码形态
                    'reserved_bit_two': num_form_k3(i['drawCode'], i['numberForm']),
                    # 和值走势
                    'reserved_bit_three': (','.join([str(s) for s in i['sumNum']]).replace('-', '')).replace(",", "-"),
                    'is_finish': 0,
                    'draw_date': now_time,
                    'create_date': now_time,
                    'update_date': now_time
                }
                # print(item)
                yield item

    def trend_odd_and_even_parse(self, response):
        """
        奇偶走势
        :param response:
        :return:
        """
        print(response.url)
        res = json.loads(response.text)
        if res['result']['data']:
            for i in res['result']['data']['bodyList']:
                now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                # _today = '%(y)s-%(m)s-%(d)s' % {'y': str(i['preIssue'])[:4], 'm': str(i['preIssue'])[4:6], 'd': str(i['preIssue'])[6:8]}
                # _time = now_time[11:]
                item = {
                    'parse_type': 'trend_odd_and_even',
                    'id': str(uuid.uuid4()).replace('-', ''),
                    'lottery_code': lottery_code_map[response.url.split('=')[-1]],
                    'lottery_num': i['preIssue'],
                    'lottery_full_no': '-'.join(map(lambda x: str(x), i['drawCode'])),
                    'lottery_char_type': 5,
                    # 号码分布
                    'reserved_bit_one': ','.join([str(i) for i in i['numberDistribution']]).replace('-', '').replace(',', '-'),
                    # 百位、十位、个位奇偶
                    'reserved_bit_two': odd_even_k3(i['drawCode'][0], i['hundredForm'][-1]),
                    'reserved_bit_three': odd_even_k3(i['drawCode'][1], i['tenForm'][-1]),
                    'reserved_bit_four': odd_even_k3(i['drawCode'][2], i['unitForm'][-1]),
                    # 奇偶比走势
                    'reserved_bit_five': odd_even_compare_k3(i['oddEvenCompare']),
                    # 奇数个数
                    'reserved_bit_six': '-'.join(map(lambda x: str(abs(x)), i['oddNumber'])),
                    # 偶数个数
                    'reserved_bit_seven': '-'.join(map(lambda x: str(abs(x)), i['evenNumber'])),
                    'is_finish': 0,
                    'draw_date': now_time,
                    'create_date': now_time,
                    'update_date': now_time,
                }
                # print(item)
                yield item
