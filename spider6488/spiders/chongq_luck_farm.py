# -*- coding: utf-8 -*-
import datetime
import json
import uuid

import scrapy

from spider6488.common.common import sum_value_11x5, dragon_tiger_chongq, big_small_chongq, trend_big_small_chongq, \
    single_double_chongq, trend_single_double_chongq, trend_by_issue_total


class ChongqLuckFarmSpider(scrapy.Spider):
    name = 'chongq_luck_farm'
    allowed_domains = ['api.api861861.com']
    _today = datetime.datetime.today().strftime('%Y-%m-%d')
    start_urls = [
        # 重庆幸运农场
        # 开奖号码
        "https://api.api861861.com/klsf/getHistoryLotteryInfo.do?date=%s&lotCode=10009" % _today,
        # 双面统计
        'https://api.api861861.com/klsf/queryNewestDataForDsdx.do?lotCode=10009',
        # 基本走势
        'https://api.api861861.com/klsf/queryDrawCodeTrend.do?periods=90&date=&lotCode=10009',
        # 大小走势
        'https://api.api861861.com/klsf/queryKslfDxTrend.do?periods=90&date=&lotCode=10009',
        # 单双走势
        'https://api.api861861.com/klsf/queryKslfDsTrend.do?periods=90&date=&lotCode=10009',
    ]
    custom_settings = {
        'ITEM_PIPELINES': {'spider6488.pipelines.ChongqLuckFarmPipeline': 311}
    }

    def parse(self, response):
        """
        重庆幸运农场
        :param response:
        :return:
        """
        # print(response.url.split("/")[-1].split('?'))
        assets_type = response.url.split("/")[-1].split('?')[0]
        if 'getHistoryLotteryInfo.do' == assets_type:       # 开奖号码
            return self.lot_num_parse(response)
        elif 'queryNewestDataForDsdx.do' == assets_type:    # 双面统计
            return self.double_statistics_parse(response)
        elif 'queryDrawCodeTrend.do' == assets_type:        # 基本走势
            return self.trend_by_issue_parse(response)
        elif 'queryKslfDxTrend.do' == assets_type:          # 大小走势
            return self.trend_big_small_parse(response)
        elif 'queryKslfDsTrend.do' == assets_type:          # 单双走势
            return self.trend_single_double_parse(response)

    def lot_num_parse(self, response):
        """
        开奖号码
        :param response:
        :return:
        """
        print(response.url)
        res = json.loads(response.text)
        for i in res["result"]["data"]:
            now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            item = {
                'parse_type': 'lottery_number',
                'id': str(uuid.uuid4()).replace('-', ''),
                'lottery_code': '2005',
                'lottery_num': i['preDrawIssue'],
                'lottery_full_no': i['preDrawCode'].replace(',', '-'),
                'lottery_sum_value': sum_value_11x5(i['sumNum'], i['sumSingleDouble'], i['sumBigSmall']),
                # 0尾大 1尾小 --> f尾大 g尾小
                'reserved_bit_one': 'g' if i['lastBigSmall'] else 'f',
                # 0龙 1虎 -->  1龙2虎
                'reserved_bit_two': dragon_tiger_chongq(i['firstDragonTiger'], i['secondDragonTiger'], i['thirdDragonTiger'], i['fourthDragonTiger']),
                'lottery_countdown': 1,
                'draw_date': i['preDrawTime'],
                'create_date': now_time,
                'update_date': now_time
            }
            # print(item)
            yield item

    def double_statistics_parse(self, response):
        """
        双面统计
        :param response:
        :return:
        """
        print(response.url)

    def trend_by_issue_parse(self, response):
        """
        基本走势
        :param response:
        :return:
        """
        print(response.url)
        res = json.loads(response.text)
        if res['result']['data']:
            for i in res['result']['data']['list']:
                now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                item = {
                    'parse_type': 'trend_by_issue',
                    'id': str(uuid.uuid4()).replace('-', ''),
                    'lottery_code': '2005',
                    'lottery_num': i['preDrawIssue'],
                    'lottery_full_no': '-'.join(map(lambda x: '%02d' % x, i['preDrawCode'])),
                    'lottery_char_type': 4,
                    # 号码分布
                    'reserved_bit_one': ','.join(str(i) for i in i['missing'][:20]).replace('-', '').replace(',', '-'),
                    # 总分
                    'reserved_bit_two': trend_by_issue_total(i['missing']),
                    'is_finish': 0,
                    'draw_date': i['preDrawDate'],
                    'create_date': now_time,
                    'update_date': now_time
                }
                # print(item)
                yield item

    def trend_big_small_parse(self, response):
        """
        大小走势
        :param response:
        :return:
        """
        print(response.url)
        res = json.loads(response.text)
        if res['result']['data']:
            for i in res['result']['data']['list']:
                _date = '%(y)s-%(m)s-%(d)s' % {'y': str(i['preDrawIssue'])[:4], 'm': str(i['preDrawIssue'])[4:6], 'd': str(i['preDrawIssue'])[6:8]}
                _time = datetime.datetime.now().strftime("%H:%M:%S")
                now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                item = {
                    'parse_type': 'trend_big_small',
                    'id': str(uuid.uuid4()).replace('-', ''),
                    'lottery_code': '2005',
                    'lottery_num': i['preDrawIssue'],
                    'lottery_full_no': '-'.join(map(lambda x: '%02d' % x, i['preDrawCode'])),
                    'lottery_char_type': 2,
                    'reserved_bit_one': big_small_chongq(i['preDrawCode'][0], i['missing'][:2]),
                    'reserved_bit_two': big_small_chongq(i['preDrawCode'][1], i['missing'][2:4]),
                    'reserved_bit_three': big_small_chongq(i['preDrawCode'][2], i['missing'][4:6]),
                    'reserved_bit_four': big_small_chongq(i['preDrawCode'][3], i['missing'][6:8]),
                    'reserved_bit_five': big_small_chongq(i['preDrawCode'][4], i['missing'][8:10]),
                    'reserved_bit_six': big_small_chongq(i['preDrawCode'][5], i['missing'][10:12]),
                    'reserved_bit_seven': big_small_chongq(i['preDrawCode'][6], i['missing'][12:14]),
                    'reserved_bit_eight': big_small_chongq(i['preDrawCode'][7], i['missing'][14:16]),
                    'reserved_bit_nine': trend_big_small_chongq(i['missing'][16:]),
                    'is_finish': 0,
                    'draw_date': _date + " " + _time,
                    'create_date': now_time,
                    'update_date': now_time
                }
                # print(item)
                yield item

    def trend_single_double_parse(self, response):
        """
        单双走势
        :param response:
        :return:
        """
        print(response.url)
        res = json.loads(response.text)
        if res['result']['data']:
            for i in res['result']['data']['list']:
                now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                _date = '%(y)s-%(m)s-%(d)s' % {'y': str(i['preDrawIssue'])[:4], 'm': str(i['preDrawIssue'])[4:6], 'd': str(i['preDrawIssue'])[6:8]}
                _time = datetime.datetime.now().strftime("%H:%M:%S")
                item = {
                    'parse_type': 'trend_single_double',
                    'id': str(uuid.uuid4()).replace('-', ''),
                    'lottery_code': '2005',
                    'lottery_num': i['preDrawIssue'],
                    'lottery_full_no': '-'.join(map(lambda x: '%02d' % x, i['preDrawCode'])),
                    'lottery_char_type': 8,
                    'reserved_bit_one': single_double_chongq(i['preDrawCode'][0], i['missing'][:2]),
                    'reserved_bit_two': single_double_chongq(i['preDrawCode'][1], i['missing'][2:4]),
                    'reserved_bit_three': single_double_chongq(i['preDrawCode'][2], i['missing'][4:6]),
                    'reserved_bit_four': single_double_chongq(i['preDrawCode'][3], i['missing'][6:8]),
                    'reserved_bit_five': single_double_chongq(i['preDrawCode'][4], i['missing'][8:10]),
                    'reserved_bit_six': single_double_chongq(i['preDrawCode'][5], i['missing'][10:12]),
                    'reserved_bit_seven': single_double_chongq(i['preDrawCode'][6], i['missing'][12:14]),
                    'reserved_bit_eight': single_double_chongq(i['preDrawCode'][7], i['missing'][14:16]),
                    'reserved_bit_nine': trend_single_double_chongq(i['missing'][16:]),
                    'is_finish': 0,
                    'draw_date': _date + " " + _time,
                    'create_date': now_time,
                    'update_date': now_time
                }
                # print(item)
                yield item
