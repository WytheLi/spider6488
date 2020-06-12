# -*- coding: utf-8 -*-
import datetime
import json
import uuid

import scrapy

from spider6488.common.common import kill_right_or_wrong
from spider6488.common.constants import buy_plan_lot_code_map


class KillNoPlanK3Spider(scrapy.Spider):
    name = 'kill_no_plan_k3'
    allowed_domains = ['api.api861861.com']
    _today = datetime.datetime.today().strftime('%Y-%m-%d')
    start_urls = [
        # 江苏快3
        'https://api.api861861.com/KillNum/getFtKillNumList.do?lotCode=10007&rows=30&date=%s' % _today,
        # 广西快3
        'https://api.api861861.com/KillNum/getFtKillNumList.do?lotCode=10026&rows=30&date=%s' % _today,
        # 吉林快3
        'https://api.api861861.com/KillNum/getFtKillNumList.do?lotCode=10027&rows=30&date=%s' % _today,
        # 河北快3
        'https://api.api861861.com/KillNum/getFtKillNumList.do?lotCode=10028&rows=30&date=%s' % _today,
        # # 内蒙古快3
        # 'https://api.api861861.com/KillNum/getFtKillNumList.do?lotCode=10029&rows=30&date=%s' % _today,
        # 安徽快3
        'https://api.api861861.com/KillNum/getFtKillNumList.do?lotCode=10030&rows=30&date=%s' % _today,
        # # 福建快3
        # 'https://api.api861861.com/KillNum/getFtKillNumList.do?lotCode=10031&rows=30&date=%s' % _today,
        # 湖北快3
        'https://api.api861861.com/KillNum/getFtKillNumList.do?lotCode=10032&rows=30&date=%s' % _today,
        # 北京快3
        'https://api.api861861.com/KillNum/getFtKillNumList.do?lotCode=10033&rows=30&date=%s' % _today,
        # 上海快3
        'https://api.api861861.com/KillNum/getFtKillNumList.do?lotCode=10061&rows=30&date=%s' % _today,
        # 贵州快3
        'https://api.api861861.com/KillNum/getFtKillNumList.do?lotCode=10062&rows=30&date=%s' % _today,
        # 甘肃快3
        'https://api.api861861.com/KillNum/getFtKillNumList.do?lotCode=10063&rows=30&date=%s' % _today,
    ]

    custom_settings = {
        'ITEM_PIPELINES': {'spider6488.pipelines.KillNoPlanPipeline': 309}
    }

    def parse(self, response):
        print(response.url)
        lot_code = response.url.split('?')[-1].split('&')[0].split('=')[1]
        res = json.loads(response.text)
        if res['result']['data']:
            for i in res['result']['data']['list']:
                now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                item = {
                    'id': str(uuid.uuid4()).replace('-', ''),
                    'lottery_code': buy_plan_lot_code_map[lot_code],
                    'lottery_num': i['preDrawIssue'],
                    'lottery_full_no': i['preDrawCode'].replace(',', '-') if i['preDrawCode'] else "",
                    'reserved_bit_one': kill_right_or_wrong(i['firstNum']),
                    'reserved_bit_two': kill_right_or_wrong(i['killSumNum']),
                    'reserved_bit_three': "",
                    'reserved_bit_four': "",
                    'reserved_bit_five': "",
                    'reserved_bit_six': "",
                    'reserved_bit_seven': "",
                    'reserved_bit_eight': "",
                    'reserved_bit_nine': "",
                    'reserved_bit_ten': "",
                    'lottery_status': 1 if i['preDrawCode'] else 0,
                    'draw_date': now_time,
                    'create_date': now_time
                }
                # print(item)
                yield item
