# -*- coding: utf-8 -*-
import datetime
import json
import uuid

import pymysql
import scrapy
from scrapy.utils.project import get_project_settings

from spider6488.common.common import sum_value_11x5, dragon_tiger_chongq, init_trend_by_issue_bottom, \
    compute_trend_by_issue_bottom
from spider6488.common.constants import lottery_code_map


settings = get_project_settings()


class GxKl10Spider(scrapy.Spider):
    name = 'gx_kl10'
    allowed_domains = ['api.api861861.com']
    _today = datetime.datetime.today().strftime('%Y-%m-%d')
    start_urls = [
        # 广西快乐十分
        # 历史开奖号码
        "https://api.api861861.com/gxklsf/getHistoryLotteryInfo.do?date=%s&lotCode=10038" % _today,
    ]
    custom_settings = {
        'ITEM_PIPELINES': {'spider6488.pipelines.ChongqLuckFarmPipeline': 311}
    }

    def parse(self, response):
        """
        开奖号码
        :param response:
        :return:
        """
        print(response.url)
        res = json.loads(response.text)
        if res['result']['data']:
            for i in res['result']['data'][::-1]:
                for item in self.trend_by_issue_parse(i):
                    yield item

                now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                item = {
                    'parse_type': 'lottery_number',
                    'id': str(uuid.uuid4()).replace('-', ''),
                    'lottery_code': lottery_code_map[response.url.split('=')[-1]],
                    'lottery_num': i['preDrawIssue'],
                    'lottery_full_no': i['preDrawCode'].replace(',', '-'),
                    # 和值 0小1大 0单1双
                    'lottery_sum_value': sum_value_11x5(i['sumNum'], i['sumSingleDouble'], i['sumBigSmall']),
                    # 尾大小 0尾大1尾小 --> f尾大g尾小
                    'reserved_bit_one': 'g' if i['lastBigSmall'] else 'f',
                    # 龙虎 0龙1虎 --> 1龙2虎
                    'reserved_bit_two': '2' if i['firstDragonTiger'] else '1',
                    'lottery_countdown': 1,
                    'draw_date': i['preDrawTime'],
                    'create_date': now_time,
                    'update_date': now_time
                }
                yield item

    def trend_by_issue_parse(self, i):
        """
        计算基本走势中的号码分布
        :param i:
        :return:
        """
        conn = pymysql.connect(**settings['MYSQL_POOL_CONFIG'])
        cursor = conn.cursor()
        cursor.execute("""
            select lottery_full_no, reserved_bit_one, reserved_bit_two
            from sc_lottery_char
            where lottery_code='5010'
            and lottery_char_type=4
            order by lottery_num desc 
            limit 1
        """)
        res = cursor.fetchone()
        print(res)
        cursor.close()
        conn.close()

        if not res:
            now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            item = {
                'parse_type': 'trend_by_issue',
                'id': str(uuid.uuid4()).replace('-', ''),
                'lottery_code': '5010',
                'lottery_num': i['preDrawIssue'],
                'lottery_full_no': i['preDrawCode'].replace(',', '-'),
                'lottery_char_type': 4,
                # 号码分布
                'reserved_bit_one': init_trend_by_issue_bottom(i['preDrawCode'].split(',')),
                # 总分
                'reserved_bit_two': '',
                'is_finish': 0,
                'draw_date': i['preDrawTime'],
                'create_date': now_time,
                'update_date': now_time
            }
        else:
            now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            item = {
                'parse_type': 'trend_by_issue',
                'id': str(uuid.uuid4()).replace('-', ''),
                'lottery_code': '5010',
                'lottery_num': i['preDrawIssue'],
                'lottery_full_no': i['preDrawCode'].replace(',', '-'),
                'lottery_char_type': 4,
                # 号码分布
                'reserved_bit_one': compute_trend_by_issue_bottom(i['preDrawCode'].split(','), res[1], res[0]),
                # 总分
                'reserved_bit_two': '',
                'is_finish': 0,
                'draw_date': i['preDrawTime'],
                'create_date': now_time,
                'update_date': now_time
            }
        yield item

