# -*- coding: utf-8 -*-
import datetime
import json
import uuid

import pymysql
import scrapy
from scrapy.utils.project import get_project_settings

from spider6488.common.common import sum_value_pc_balls, init_trend_position_bottom_c28, \
    compute_trend_position_bottom_c28

settings = get_project_settings()


class PcBallsLuck28Spider(scrapy.Spider):
    name = 'pc_balls_luck28'
    allowed_domains = ['api.api861861.com']
    _today = datetime.datetime.today().strftime('%Y-%m-%d')
    start_urls = [
        # pc蛋蛋幸运28
        # 开奖号码
        'https://api.api861861.com/LuckTwenty/getPcLucky28List.do?date=%s' % _today,
    ]
    custom_settings = {
        'ITEM_PIPELINES': {'spider6488.pipelines.PcBallsLuck28Pipeline': 306}
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
                for item in self.trend_qrientation_parse(i):
                    yield item

                now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                data = {
                    'parse_type': 'lottery_number',
                    'id': str(uuid.uuid4()).replace('-', ''),
                    'lottery_code': '5011',
                    'lottery_num': i['preDrawIssue'],
                    'lottery_full_no': i['preDrawCode'].replace(',', '-'),
                    # 总和
                    'lottery_sum_value': sum_value_pc_balls(i['sumNum'], i['sumSingleDouble'], i['sumBigSmall']),
                    'lottery_countdown': 1,
                    'draw_date': i['preDrawTime'],
                    'create_date': now_time,
                    'update_date': now_time
                }
                yield data

    def trend_qrientation_parse(self, i):
        """
        定位走势
        :return:
        """
        conn = pymysql.connect(**settings['MYSQL_POOL_CONFIG'])
        cursor = conn.cursor()
        cursor.execute("""
            select lottery_full_no, reserved_bit_one, reserved_bit_two, reserved_bit_three
            from sc_lottery_char
            where lottery_code='5011'
            and lottery_char_type=1
            order by lottery_num desc 
            limit 1
        """)
        res = cursor.fetchone()
        # print(res)
        cursor.close()
        conn.close()

        if not res:
            now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            item = {
                'parse_type': 'trend_qrientation',
                'id': str(uuid.uuid4()).replace('-', ''),
                'lottery_code': '5011',
                'lottery_num': i['preDrawIssue'],
                'lottery_full_no': i['preDrawCode'].replace(',', '-'),
                'lottery_char_type': 1,
                'reserved_bit_one': init_trend_position_bottom_c28(i['preDrawCode'].split(',')[0]),
                'reserved_bit_two': init_trend_position_bottom_c28(i['preDrawCode'].split(',')[1]),
                'reserved_bit_three': init_trend_position_bottom_c28(i['preDrawCode'].split(',')[2]),
                'is_finish': 0,
                'draw_date': i['preDrawTime'],
                'create_date': now_time,
                'update_date': now_time
            }
        else:
            now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            item = {
                'parse_type': 'trend_qrientation',
                'id': str(uuid.uuid4()).replace('-', ''),
                'lottery_code': '5011',
                'lottery_num': i['preDrawIssue'],
                'lottery_full_no': i['preDrawCode'].replace(',', '-'),
                'lottery_char_type': 1,
                'reserved_bit_one': compute_trend_position_bottom_c28(1, i['preDrawCode'].split(',')[0], res[1], res[0]),
                'reserved_bit_two': compute_trend_position_bottom_c28(2, i['preDrawCode'].split(',')[1], res[2], res[0]),
                'reserved_bit_three': compute_trend_position_bottom_c28(3, i['preDrawCode'].split(',')[2], res[3], res[0]),
                'is_finish': 0,
                'draw_date': i['preDrawTime'],
                'create_date': now_time,
                'update_date': now_time
            }
        yield item
