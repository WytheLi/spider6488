# -*- coding: utf-8 -*-
import datetime
import json
import uuid

import scrapy

from spider6488.common.common import sum_value_11x5, dragon_tiger_ssc,  \
    three_terms_ssc, big_small_ssc, single_double_ssc, dragon_tiger_equal_ssc
from spider6488.common.constants import lottery_code_map


class Com1680380SscSpider(scrapy.Spider):
    name = 'com1680380_ssc'
    allowed_domains = ['api.api861861.com']
    _today = datetime.datetime.today().strftime('%Y-%m-%d')
    _yesterday = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    start_urls = [
        # 天津时时彩
        # 开奖号码  综合分析
        'https://api.api861861.com/CQShiCai/getBaseCQShiCaiList.do?date=%s&lotCode=10003' % _today,
        # 双面统计
        'https://api.api861861.com/CQShiCai/queryNewestDataForDsdx.do?lotCode=10003',
        # 龙虎走势
        'https://api.api861861.com/CQShiCai/queryCQShiCaiTrendByDT.do?issue=30&date=&lotCode=10003',
        # 形态走势 前三形态: type 1 中三形态:2 后三形态:3
        'https://api.api861861.com/CQShiCai/queryCQShiCaiTrendByType.do?type=1&issue=30&date=&lotCode=10003',
        # 基本走势
        'https://api.api861861.com/CQShiCai/queryCQShiCaiTrendByIssue.do?issue=30&date=&lotCode=10003',
        # 定位走势 修改num可以查看1-5求的数据
        'https://api.api861861.com/CQShiCai/queryCQShiCaiTrendByLocation.do?num=1&issue=30&date=&lotCode=10003',
        # 综合分析
        # 'https://api.api861861.com/CQShiCai/getBaseCQShiCaiList.do?date=%s&lotCode=10003',

        # 新疆时时彩
        # 开奖号码  综合分析
        'https://api.api861861.com/CQShiCai/getBaseCQShiCaiList.do?date=%s&lotCode=10004' % _today,
        'https://api.api861861.com/CQShiCai/getBaseCQShiCaiList.do?date=%s&lotCode=10004' % _yesterday,
        # 双面统计
        'https://api.api861861.com/CQShiCai/queryNewestDataForDsdx.do?lotCode=10004',
        # 龙虎走势
        'https://api.api861861.com/CQShiCai/queryCQShiCaiTrendByDT.do?issue=100&date=&lotCode=10004',
        # 形态走势 type 前三形态:1 中三形态:2 后三形态:3
        'https://api.api861861.com/CQShiCai/queryCQShiCaiTrendByType.do?type=1&issue=100&date=&lotCode=10004',
        # 基本走势
        'https://api.api861861.com/CQShiCai/queryCQShiCaiTrendByIssue.do?issue=90&date=&lotCode=10004',
        # 定位走势 修改num可以查看1-5求的数据
        'https://api.api861861.com/CQShiCai/queryCQShiCaiTrendByLocation.do?num=1&issue=30&date=&lotCode=10004',
        # 综合分析
        # 'https://api.api861861.com/CQShiCai/getBaseCQShiCaiList.do?date=%s&lotCode=10004',
    ]
    custom_settings = {
        'ITEM_PIPELINES': {'spider6488.pipelines.Com1680380SscPipeline': 312}
    }

    def parse(self, response):
        """
        时时彩
        :param response:
        :return:
        """
        # print(response.url.split("/")[-1].split('?'))
        assets_type = response.url.split("/")[-1].split('?')[0]
        if 'getBaseCQShiCaiList.do' == assets_type:         # 开奖号码
            return self.lot_num_parse(response)
        elif 'queryNewestDataForDsdx.do' == assets_type:    # 双面统计
            return self.double_statistics_parse(response)
        elif 'queryCQShiCaiTrendByDT.do' == assets_type:    # 龙虎走势
            return self.trend_dt_parse(response)
        elif 'queryCQShiCaiTrendByType.do' == assets_type:  # 形态走势
            return self.trend_by_type_parse(response)
        elif 'queryCQShiCaiTrendByIssue.do' == assets_type:  # 基本走势
            return self.trend_by_issue_parse(response)
        elif 'queryCQShiCaiTrendByLocation.do' == assets_type:  # 定位走势
            return self.trend_local_parse(response)

    def lot_num_parse(self, response):
        """
        开奖号码 &综合分析数据
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
                'lottery_code': lottery_code_map[response.url.split('=')[-1]],
                'lottery_num': i['preDrawIssue'],
                'lottery_full_no': i['preDrawCode'].replace(',', '-'),
                # 和值
                'lottery_sum_value': sum_value_11x5(i['sumNum'], i['sumSingleDouble'], i['sumBigSmall']),
                # 龙虎和 0龙1虎2和  -->  1龙2虎3和
                'reserved_bit_one': dragon_tiger_ssc(i['dragonTiger']),
                # 1-5大小 0大1小 --> a大b小
                'reserved_bit_two': big_small_ssc([i['firstBigSmall'], i['secondBigSmall'], i['thirdBigSmall'], i['fourthBigSmall'], i['fifthBigSmall']]),
                # 1-5单双 0单1双 --> c单d双
                'reserved_bit_three': single_double_ssc([i['firstSingleDouble'], i['secondSingleDouble'], i['thirdSingleDouble'], i['fourthSingleDouble'], i['fifthSingleDouble']]),
                # 三项
                'reserved_bit_four': three_terms_ssc(i['behindThree']) +"-"+ three_terms_ssc(i['betweenThree'])+"-"+three_terms_ssc(i['lastThree']),
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
                _date = '%(y)s-%(m)s-%(d)s' % {'y': i['issue'][:4], 'm': i['issue'][4:6], 'd': i['issue'][6:8]}
                _time = datetime.datetime.now().strftime('%H:%M:%S')
                item = {
                    'parse_type': 'trend_dtt',
                    'id': str(uuid.uuid4()).replace('-', ''),
                    'lottery_code': lottery_code_map[response.url.split('=')[-1]],
                    'lottery_num': i['issue'],
                    'lottery_full_no': i['code'].replace(',', '-'),
                    'lottery_char_type': 6,
                    # 第一球
                    'reserved_bit_one': ','.join([str(i) for i in i['array'][:10]]).replace('-', '').replace(',', '-'),
                    # 第五球
                    'reserved_bit_two': ','.join([str(i) for i in i['array'][10:20]]).replace('-', '').replace(',', '-'),
                    # 龙虎和
                    'reserved_bit_three': dragon_tiger_equal_ssc(i['code'], i['array'][20:]),
                    'is_finish': 0,
                    'draw_date': _date + ' ' + _time,
                    'create_date': now_time,
                    'update_date': now_time
                }
                # print(item)
                yield item

    def trend_by_type_parse(self, response):
        """
        形态走势
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
            for i in res['result']['data'][0]['bodyList']:
                now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                _date = '%(y)s-%(m)s-%(d)s' % {'y': i['issue'][:4], 'm': i['issue'][4:6], 'd': i['issue'][6:8]}
                _time = datetime.datetime.now().strftime("%H:%M:%S")
                item = {
                    'parse_type': 'trend_by_issue',
                    'id': str(uuid.uuid4()).replace('-', ''),
                    'lottery_code': lottery_code_map[response.url.split('=')[-1]],
                    'lottery_num': i['issue'],
                    'lottery_full_no': i['code'].replace(",", "-"),
                    'lottery_char_type': 4,
                    # 第一球
                    'reserved_bit_one': ','.join([str(i) for i in i['array'][:10]]).replace('-', '').replace(',', '-'),
                    # 第二球
                    'reserved_bit_two': ','.join([str(i) for i in i['array'][10:20]]).replace('-', '').replace(',', '-'),
                    # 第三球
                    'reserved_bit_three': ','.join([str(i) for i in i['array'][20:30]]).replace('-', '').replace(',', '-'),
                    # 第四球
                    'reserved_bit_four': ','.join([str(i) for i in i['array'][30:40]]).replace('-', '').replace(',', '-'),
                    # 第五球
                    'reserved_bit_five': ','.join([str(i) for i in i['array'][40:]]).replace('-', '').replace(',', '-'),
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

