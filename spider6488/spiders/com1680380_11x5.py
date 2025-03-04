# -*- coding: utf-8 -*-
import datetime
import json
import uuid

import scrapy

from spider6488.common.common import sum_value_11x5, three_terms_11x5, dragon_tiger_11x5
from spider6488.common.constants import lottery_code_map


class Com_1680380_11x5Spider(scrapy.Spider):
    name = 'com_1680380_11x5'
    allowed_domains = ['api.api861861.com']
    _today = datetime.datetime.today().strftime('%Y-%m-%d')
    _yesterday = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    start_urls = [
        # 安徽11选5 开奖号码
        'https://api.api861861.com/ElevenFive/getElevenFiveList.do?date=%s&lotCode=10017' % _today,
        # 安徽11选5 基本走势
        'https://api.api861861.com/ElevenFive/queryElevnFiveTrendByIssue.do?issue=30&date=&lotCode=10017',
        # 安徽11选5 龙虎走势
        'https://api.api861861.com/ElevenFive/queryElevnFiveDTTrend.do?issue=30&date=&lotCode=10017',
        # 安徽11选5 和值走势
        'https://api.api861861.com/ElevenFive/queryElevnFiveSumTrend.do?issue=30&date=&lotCode=10017',

        # 广东11x5 开奖号码
        'https://api.api861861.com/ElevenFive/getElevenFiveList.do?date=%s&lotCode=10006' % _today,
        # 广东11x5 基本走势
        'https://api.api861861.com/ElevenFive/queryElevnFiveTrendByIssue.do?issue=30&date=&lotCode=10006',
        # 广东11x5 龙虎走势
        'https://api.api861861.com/ElevenFive/queryElevnFiveDTTrend.do?issue=30&date=&lotCode=10006',
        # 广东11x5 和值走势
        'https://api.api861861.com/ElevenFive/queryElevnFiveSumTrend.do?issue=30&date=&lotCode=10006',

        # 广西11x5
        # 开奖号码
        'https://api.api861861.com/ElevenFive/getElevenFiveList.do?date=%s&lotCode=10022' % _today,
        # 基本走势
        'https://api.api861861.com/ElevenFive/queryElevnFiveTrendByIssue.do?issue=30&date=&lotCode=10022',
        # 龙虎走势
        'https://api.api861861.com/ElevenFive/queryElevnFiveDTTrend.do?issue=30&date=&lotCode=10022',
        # 和值走势
        'https://api.api861861.com/ElevenFive/queryElevnFiveSumTrend.do?issue=30&date=&lotCode=10022',

        # 湖北11选5
        # 开奖号码
        'https://api.api861861.com/ElevenFive/getElevenFiveList.do?date=%s&lotCode=10020' % _today,
        # 基本走势
        'https://api.api861861.com/ElevenFive/queryElevnFiveTrendByIssue.do?issue=30&date=&lotCode=10020',
        # 龙虎走势
        'https://api.api861861.com/ElevenFive/queryElevnFiveDTTrend.do?issue=30&date=&lotCode=10020',
        # 和值走势
        'https://api.api861861.com/ElevenFive/queryElevnFiveSumTrend.do?issue=30&date=&lotCode=10020',

        # 吉林11选5
        # 开奖号码
        'https://api.api861861.com/ElevenFive/getElevenFiveList.do?date=%s&lotCode=10023' % _today,
        # 基本走势
        'https://api.api861861.com/ElevenFive/queryElevnFiveTrendByIssue.do?issue=30&date=&lotCode=10023',
        # 龙虎走势
        'https://api.api861861.com/ElevenFive/queryElevnFiveDTTrend.do?issue=30&date=&lotCode=10015',
        # 和值走势
        'https://api.api861861.com/ElevenFive/queryElevnFiveSumTrend.do?issue=30&date=&lotCode=10015',

        # 江苏11选5
        # 开奖号码
        'https://api.api861861.com/ElevenFive/getElevenFiveList.do?date=%s&lotCode=10016' % _today,
        # 基本走势
        'https://api.api861861.com/ElevenFive/queryElevnFiveTrendByIssue.do?issue=30&date=&lotCode=10016',
        # 龙虎走势
        'https://api.api861861.com/ElevenFive/queryElevnFiveDTTrend.do?issue=30&date=&lotCode=10016',
        # 和值走势
        'https://api.api861861.com/ElevenFive/queryElevnFiveSumTrend.do?issue=30&date=&lotCode=10016',

        # 江西11选5
        # 开奖号码
        'https://api.api861861.com/ElevenFive/getElevenFiveList.do?date=%s&lotCode=10015' % _today,
        # 基本走势
        'https://api.api861861.com/ElevenFive/queryElevnFiveTrendByIssue.do?issue=90&date=&lotCode=10015',
        # 龙虎走势
        'https://api.api861861.com/ElevenFive/queryElevnFiveDTTrend.do?issue=90&date=&lotCode=10015',
        # 和值走势
        'https://api.api861861.com/ElevenFive/queryElevnFiveSumTrend.do?issue=90&date=&lotCode=10015',

        # 辽宁11选5
        # 开奖号码
        'https://api.api861861.com/ElevenFive/getElevenFiveList.do?date=%s&lotCode=10019' % _today,
        # 基本走势
        'https://api.api861861.com/ElevenFive/queryElevnFiveTrendByIssue.do?issue=30&date=&lotCode=10019',
        # 龙虎走势
        'https://api.api861861.com/ElevenFive/queryElevnFiveDTTrend.do?issue=30&date=&lotCode=10019',
        # 和值走势
        'https://api.api861861.com/ElevenFive/queryElevnFiveSumTrend.do?issue=30&date=&lotCode=10019',

        # 内蒙古11选5
        # 开奖号码
        'https://api.api861861.com/ElevenFive/getElevenFiveList.do?date=%s&lotCode=10024' % _today,
        # 基本走势
        'https://api.api861861.com/ElevenFive/queryElevnFiveTrendByIssue.do?issue=30&date=&lotCode=10024',
        # 龙虎走势
        'https://api.api861861.com/ElevenFive/queryElevnFiveDTTrend.do?issue=30&date=&lotCode=10024',
        # 和值走势
        'https://api.api861861.com/ElevenFive/queryElevnFiveSumTrend.do?issue=30&date=&lotCode=10024',

        # 上海11选5
        # 开奖号码
        'https://api.api861861.com/ElevenFive/getElevenFiveList.do?date=%s&lotCode=10018' % _today,
        'https://api.api861861.com/ElevenFive/getElevenFiveList.do?date=%s&lotCode=10018' % _yesterday,
        # 基本走势
        'https://api.api861861.com/ElevenFive/queryElevnFiveTrendByIssue.do?issue=30&date=&lotCode=10018',
        # 龙虎走势
        'https://api.api861861.com/ElevenFive/queryElevnFiveDTTrend.do?issue=30&date=&lotCode=10018',
        # 和值走势
        'https://api.api861861.com/ElevenFive/queryElevnFiveSumTrend.do?issue=30&date=&lotCode=10018',

        # 浙江11选5
        # 开奖号码
        'https://api.api861861.com/ElevenFive/getElevenFiveList.do?date=%s&lotCode=10025' % _today,
        # 基本走势
        'https://api.api861861.com/ElevenFive/queryElevnFiveTrendByIssue.do?issue=30&date=&lotCode=10025',
        # 龙虎走势
        'https://api.api861861.com/ElevenFive/queryElevnFiveDTTrend.do?issue=30&date=&lotCode=10025',
        # 和值走势
        'https://api.api861861.com/ElevenFive/queryElevnFiveSumTrend.do?issue=30&date=&lotCode=10025',
    ]
    custom_settings = {
        'ITEM_PIPELINES': {'spider6488.pipelines.Com1680380_11x5Pipeline': 303}
    }

    def parse(self, response):
        """
        https://www.1680380.com/
        11选5
        开奖号码，基本走势，龙虎走势，和值走势
        :param response:
        :return:
        """
        # print(response.url.split("/")[-1].split('?'))
        assets_type = response.url.split("/")[-1].split('?')[0]
        if 'getElevenFiveList.do' == assets_type:       # 开奖号码
            return self.lottery_number_parse(response)
        elif 'queryElevnFiveTrendByIssue.do' == assets_type:    # 基本走势
            return self.trend_by_issue_parse(response)
        elif 'queryElevnFiveDTTrend.do' == assets_type:         # 龙虎走势
            return self.trend_dt_parse(response)
        elif 'queryElevnFiveSumTrend.do' == assets_type:        # 和值走势
            return self.trend_sum_parse(response)

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
                    # 总和规则：c单d双，a大b小e和
                    'lottery_sum_value': sum_value_11x5(i['sumNum'], i['sumSingleDouble'], i['sumBigSmall']),
                    # 龙虎：1龙0虎 --> 1龙2虎
                    'reserved_bit_one': 1 if 1 == i['dragonTiger'] else 2,
                    # 前三、中三、后三  0杂六1半顺2顺子--> 1半顺2顺子5杂六
                    'reserved_bit_two': three_terms_11x5(i['behindThree']),
                    'reserved_bit_three': three_terms_11x5(i['betweenThree']),
                    'reserved_bit_four': three_terms_11x5(i['lastThree']),
                    'lottery_countdown': 1,
                    'draw_date': i['preDrawTime'],
                    'create_date': now_time,
                    'update_date': now_time
                }
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
                item = {
                    'parse_type': 'trend_by_issue',
                    'id': str(uuid.uuid4()).replace('-', ''),
                    'lottery_code': lottery_code_map[response.url.split('=')[-1]],
                    'lottery_num': i['issue'],
                    'lottery_full_no': i['code'].replace(",", "-"),
                    'lottery_char_type': 4,
                    # 第一球
                    'reserved_bit_one': ','.join([str(i) for i in i['array'][:11]]).replace('-', '').replace(',', '-'),
                    # 第二球
                    'reserved_bit_two': ','.join([str(i) for i in i['array'][11:22]]).replace('-', '').replace(',', '-'),
                    # 第三球
                    'reserved_bit_three': ','.join([str(i) for i in i['array'][22:33]]).replace('-', '').replace(',', '-'),
                    # 第四球
                    'reserved_bit_four': ','.join([str(i) for i in i['array'][33:44]]).replace('-', '').replace(',', '-'),
                    # 第五球
                    'reserved_bit_five': ','.join([str(i) for i in i['array'][44:]]).replace('-', '').replace(',', '-'),
                    'is_finish': 0,
                    # 'draw_date': '20%(y)s-%(m)s-%(d)s' % {'y': i['issue'][:2], 'm': i['issue'][2:4], 'd': i['issue'][4:6]},
                    'draw_date': now_time,
                    'create_date': now_time,
                    'update_date': now_time
                }
                yield item

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
                now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                item = {
                    'parse_type': 'trend_dtt',
                    'id': str(uuid.uuid4()).replace('-', ''),
                    'lottery_code': lottery_code_map[response.url.split('=')[-1]],
                    'lottery_num': i['issue'],
                    'lottery_full_no': i['code'].replace(',', '-'),
                    'lottery_char_type': 6,
                    # 第一球
                    'reserved_bit_one': ','.join([str(i) for i in i['array'][:11]]).replace('-', '').replace(',', '-'),
                    # 第五球
                    'reserved_bit_two': ','.join([str(i) for i in i['array'][11:22]]).replace('-', '').replace(',', '-'),
                    'reserved_bit_three': dragon_tiger_11x5(i['code'], i['array'][22:24]),
                    'is_finish': 0,
                    # 'draw_date': '20%(y)s-%(m)s-%(d)s' % {'y': i['issue'][:2], 'm': i['issue'][2:4], 'd': i['issue'][4:6]},
                    'draw_date': now_time,
                    'create_date': now_time,
                    'update_date': now_time
                }
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
                item = {
                    'parse_type': 'trend_sum',
                    'id': str(uuid.uuid4()).replace('-', ''),
                    'lottery_code': lottery_code_map[response.url.split('=')[-1]],
                    'lottery_num': i['issue'],
                    'lottery_full_no': i['code'].replace(',', '-'),
                    'lottery_char_type': 3,
                    # 和值走势
                    'reserved_bit_one': ','.join([str(d_1) for d_1 in i['array'][:31]]).replace('-', '').replace(',', '-'),
                    'reserved_bit_two': i['array'][31],     # 和值
                    'reserved_bit_three': i['array'][32],   # 和尾
                    'is_finish': 0,
                    # 'draw_date': '20%(y)s-%(m)s-%(d)s' % {'y': i['issue'][:2], 'm': i['issue'][2:4], 'd': i['issue'][4:6]},
                    'draw_date': now_time,
                    'create_date': now_time,
                    'update_date': now_time
                }
                yield item
