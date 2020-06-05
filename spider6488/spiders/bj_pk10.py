# -*- coding: utf-8 -*-
import datetime
import json
import uuid

import scrapy

from spider6488.common.common import sum_value_11x5, dragon_tiger_pk10


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

    custom_settings = {
        'ITEM_PIPELINES': {'spider6488.pipelines.BjPk10Pipeline': 313}
    }

    def parse(self, response):
        """
        北京PK10
        :param response:
        :return:
        """
        assets_type = response.url.split("/")[-1].split('?')[0]
        if 'getPksHistoryList.do' == assets_type:       # 开奖号码
            return self.lottery_number_parse(response)
        elif 'queryDrawCodeTrend.do' == assets_type:    # 号码走势
            return self.trend_draw_code(response)
        elif 'queryGysumTrend.do' == assets_type:       # 冠亚和走势
            return self.trend_gysum(response)

    def lottery_number_parse(self, response):
        """
        开奖号码解析
        :return:
        """
        print(response.url)
        res = json.loads(response.text)
        for i in res['result']['data']:
            now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            item = {
                'parse_type': 'lottery_number',
                'id': str(uuid.uuid4()).replace('-', ''),
                'lottery_code': '5001',
                'lottery_num': i['preDrawIssue'],
                'lottery_full_no': i['preDrawCode'].replace(',', '-'),
                'lottery_sum_value': sum_value_11x5(i['sumFS'], i['sumSingleDouble'], i['sumBigSamll']),
                'reserved_bit_one': dragon_tiger_pk10(i['firstDT'], i['secondDT'], i['thirdDT'], i['fourthDT'], i['fifthDT']),
                'lottery_countdown': 1,
                'draw_date': i['preDrawTime'],
                'create_date': now_time,
                'update_date': now_time
            }
            yield item

    def trend_draw_code(self, response):
        """
        号码走势
        :param response:
        :return:
        """
        print(response.url)
        res = json.loads(response.text)
        if res['result']['data']:
            for i in res['result']['data']['bodyList']:
                now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                item = {
                    'parse_type': 'trend_draw_code',
                    'id': str(uuid.uuid4()).replace('-', ''),
                    'lottery_code': '5001',
                    'lottery_num': i['preIssue'],
                    'lottery_full_no': '-'.join(map(lambda x: str(x), i['preDrawCode'])),
                    'lottery_char_type': 9,
                    # 冠军号
                    'reserved_bit_one': ','.join([str(missing) for missing in i['subBodyList'][0]['missing']]).replace('-', '').replace(',', '-'),
                    # 亚军号
                    'reserved_bit_two': ','.join([str(missing) for missing in i['subBodyList'][1]['missing']]).replace('-', '').replace(',', '-'),
                    # 第三名
                    'reserved_bit_three': ','.join([str(missing) for missing in i['subBodyList'][2]['missing']]).replace('-', '').replace(',', '-'),
                    # 第四名
                    'reserved_bit_four': ','.join([str(missing) for missing in i['subBodyList'][3]['missing']]).replace('-', '').replace(',', '-'),
                    # 第五名 后面依次到是第十名
                    'reserved_bit_five': ','.join([str(missing) for missing in i['subBodyList'][4]['missing']]).replace('-', '').replace(',', '-'),
                    'reserved_bit_six': ','.join([str(missing) for missing in i['subBodyList'][5]['missing']]).replace('-', '').replace(',', '-'),
                    'reserved_bit_seven': ','.join([str(missing) for missing in i['subBodyList'][6]['missing']]).replace('-', '').replace(',', '-'),
                    'reserved_bit_eight': ','.join([str(missing) for missing in i['subBodyList'][7]['missing']]).replace('-', '').replace(',', '-'),
                    'reserved_bit_nine': ','.join([str(missing) for missing in i['subBodyList'][8]['missing']]).replace('-', '').replace(',', '-'),
                    'reserved_bit_ten': ','.join([str(missing) for missing in i['subBodyList'][9]['missing']]).replace('-', '').replace(',', '-'),
                    'is_finish': 0,
                    'draw_date': '%(y)s-%(m)s-%(d)s %(h)s:%(minute)s:00' %
                                 {'y': now_time[:4], 'm': i['preDrawTime'][:2], 'd': i['preDrawTime'][3:5],
                                  'h': i['preDrawTime'][6:8], 'minute': i['preDrawTime'][9:11]},
                    'create_date': now_time,
                    'update_date': now_time
                }
                yield item

    def trend_gysum(self, response):
        """
        冠亚和走势
        :param response:
        :return:
        """
        print(response.url)
        res = json.loads(response.text)
        if res['result']['data']:
            for i in res['result']['data']['list']:
                now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                item = {
                    'parse_type': 'trend_gysum',
                    'id': str(uuid.uuid4()).replace('-', ''),
                    'lottery_code': '5001',
                    'lottery_num': i['preIssue'],
                    'lottery_full_no': '-'.join(map(lambda x: str(x), i['preDrawCode'])),
                    'lottery_char_type': 10,
                    # 冠亚和
                    'reserved_bit_one': i['gySum'],
                    # 长号码
                    'reserved_bit_two': ','.join([str(hm_2) for hm_2 in i['missing']][:-4]).replace('-', '').replace(',', '-'),
                    'is_finish': 0,
                    'draw_date': '%(date)s %(time)s' % {'date': now_time[:10], 'time': i['preDrawTime']},
                    'create_date': now_time,
                    'update_date': now_time
                }
                # print(item)
                yield item
