# -*- coding: utf-8 -*-
import datetime
import json
import uuid

import scrapy

from spider6488.common.common import sum_value_canada28


_today = datetime.datetime.today().strftime('%Y-%m-%d')


class Canada28Spider(scrapy.Spider):
    name = 'canada28'
    allowed_domains = ['cp9328.com']
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
        for i in result:
            now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            item = {
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
