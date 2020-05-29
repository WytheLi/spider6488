# -*- coding: utf-8 -*-
import datetime
import json
import uuid

import scrapy

from spider6488.common.common import sum_value_pc_balls


_today = datetime.datetime.today().strftime('%Y-%m-%d')


class PcBallsLuck28Spider(scrapy.Spider):
    name = 'pc_balls_luck28'
    allowed_domains = ['api.api861861.com']
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
            for i in res['result']['data']:
                now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                data = {
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
