# -*- coding: utf-8 -*-
import datetime
import json
import uuid

import pymysql
import scrapy
from scrapy.utils.project import get_project_settings

from spider6488.common.common import sum_value_canada28, init_trend_position_bottom_c28, \
    compute_trend_position_bottom_c28

settings = get_project_settings()


class Canada28Spider(scrapy.Spider):
    name = 'canada28'
    allowed_domains = ['cp9328.com']
    _today = datetime.datetime.today().strftime('%Y-%m-%d')
    _yesterday = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    start_urls = [
        # 加拿大28
        # 开奖号码
        'https://cp9328.com/data/jndpc28/lotteryList/%s.json' % _yesterday,
        'https://cp9328.com/data/jndpc28/lotteryList/%s.json' % _today,
    ]
    custom_settings = {
        'ITEM_PIPELINES': {'spider6488.pipelines.PcBallsLuck28Pipeline': 306}
    }

    def parse(self, response):
        print(response.url)
        result = json.loads(response.text)
        # for i in result:
        # for i in result[20::-1]:
        for i in result[::-1]:
            # 定位走势
            for item in self.trend_qrientation_parse(i):
                yield item

            now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            item = {
                'parse_type': 'lottery_number',
                'id': str(uuid.uuid4()).replace('-', ''),
                'lottery_code': '5013',
                'lottery_num': i['issue'],
                'lottery_full_no': '-'.join(map(lambda x: str(x), i['openNum'])),
                'lottery_sum_value': sum_value_canada28(i['sumArr'][0], i['sumArr'][1], i['sumArr'][2]),
                'lottery_countdown': 1,
                'draw_date': i['openDateTime'],
                'create_date': now_time,
                'update_date': now_time
            }
            # print(item)
            yield item

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
            where lottery_code='5013'
            and lottery_char_type=1
            order by lottery_num desc 
            limit 1
        """)
        res = cursor.fetchone()
        # print(res)
        cursor.close()
        conn.close()

        if not res:     # 没有底数 去初始化底数
            now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            item = {
                'parse_type': 'trend_qrientation',
                'id': str(uuid.uuid4()).replace('-', ''),
                'lottery_code': '5013',
                'lottery_num': i['issue'],
                'lottery_full_no': '-'.join(map(lambda x: str(x), i['openNum'])),
                'lottery_char_type': 1,
                'reserved_bit_one': init_trend_position_bottom_c28(i['openNum'][0]),
                'reserved_bit_two': init_trend_position_bottom_c28(i['openNum'][1]),
                'reserved_bit_three': init_trend_position_bottom_c28(i['openNum'][2]),
                'is_finish': 0,
                'draw_date': i['openDateTime'],
                'create_date': now_time,
                'update_date': now_time
            }
        else:
            now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            item = {
                'parse_type': 'trend_qrientation',
                'id': str(uuid.uuid4()).replace('-', ''),
                'lottery_code': '5013',
                'lottery_num': i['issue'],
                'lottery_full_no': '-'.join(map(lambda x: str(x), i['openNum'])),
                'lottery_char_type': 1,
                'reserved_bit_one': compute_trend_position_bottom_c28(1, i['openNum'][0], res[1], res[0]),
                'reserved_bit_two': compute_trend_position_bottom_c28(2, i['openNum'][1], res[2], res[0]),
                'reserved_bit_three': compute_trend_position_bottom_c28(3, i['openNum'][2], res[3], res[0]),
                'is_finish': 0,
                'draw_date': i['openDateTime'],
                'create_date': now_time,
                'update_date': now_time
            }
            # print(item)
        yield item
