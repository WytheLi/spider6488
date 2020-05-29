# -*- coding: utf-8 -*-
import datetime
import json
import uuid

import scrapy

from spider6488.common.common import kill_right_or_wrong
from spider6488.common.constants import buy_plan_lot_code_map


_today = datetime.datetime.today().strftime('%Y-%m-%d')


class KillNoPlanSpider(scrapy.Spider):
    name = 'kill_no_plan'
    allowed_domains = ['api.api861861.com']
    start_urls = [
        # 杀号计划
        # # SG飞艇
        # 'https://api.api861861.com/KillNum/getPksKillNumList.do?lotCode=10058&rows=30&date=%s' % _today,
        # 北京PK10
        'https://api.api861861.com/KillNum/getPksKillNumList.do?lotCode=10001&rows=30&date=%s' % _today,
        # # 极速赛车
        # 'https://api.api861861.com/KillNum/getPksKillNumList.do?lotCode=10037&rows=30&date=%s' % _today,
        # # 澳洲幸运十
        # 'https://api.api861861.com/KillNum/getPksKillNumList.do?lotCode=10012&rows=30&date=%s' % _today,

        # # 重庆欢乐生肖
        # 'https://api.api861861.com/KillNum/getSscKillNumList.do?lotCode=10060&rows=30&date=%s' % _today,
        # # 幸运时时彩
        # 'https://api.api861861.com/KillNum/getSscKillNumList.do?lotCode=10059&rows=30&date=%s' % _today,
        # 天津时时彩
        'https://api.api861861.com/KillNum/getSscKillNumList.do?lotCode=10003&rows=30&date=%s' % _today,
        # # 台湾5分彩
        # 'https://api.api861861.com/KillNum/getSscKillNumList.do?lotCode=10064&rows=30&date=%s' % _today,
        # 新疆时时彩
        'https://api.api861861.com/KillNum/getSscKillNumList.do?lotCode=10004&rows=30&date=%s' % _today,
        # # 极速时时彩
        # 'https://api.api861861.com/KillNum/getSscKillNumList.do?lotCode=10036&rows=30&date=%s' % _today,
        # # 澳洲幸运5
        # 'https://api.api861861.com/KillNum/getSscKillNumList.do?lotCode=10010&rows=30&date=%s' % _today,

        # 广东11选5
        'https://api.api861861.com/KillNum/getEfKillNumList.do?lotCode=10006&rows=30&date=%s' % _today,
        # 浙江11选5
        'https://api.api861861.com/KillNum/getEfKillNumList.do?lotCode=10025&rows=30&date=%s' % _today,
        # 江西11选5
        'https://api.api861861.com/KillNum/getEfKillNumList.do?lotCode=10015&rows=30&date=%s' % _today,
        # 江苏11选5
        'https://api.api861861.com/KillNum/getEfKillNumList.do?lotCode=10016&rows=30&date=%s' % _today,
        # 安徽11选5
        'https://api.api861861.com/KillNum/getEfKillNumList.do?lotCode=10017&rows=30&date=%s' % _today,
        # 上海11选5
        'https://api.api861861.com/KillNum/getEfKillNumList.do?lotCode=10018&rows=30&date=%s' % _today,
        # 辽宁11选5
        'https://api.api861861.com/KillNum/getEfKillNumList.do?lotCode=10019&rows=30&date=%s' % _today,
        # 湖北11选5
        'https://api.api861861.com/KillNum/getEfKillNumList.do?lotCode=10020&rows=30&date=%s' % _today,
        # 广西11选5
        'https://api.api861861.com/KillNum/getEfKillNumList.do?lotCode=10022&rows=30&date=%s' % _today,
        # 吉林11选5
        'https://api.api861861.com/KillNum/getEfKillNumList.do?lotCode=10023&rows=30&date=%s' % _today,
        # 内蒙古11选5
        'https://api.api861861.com/KillNum/getEfKillNumList.do?lotCode=10024&rows=30&date=%s' % _today,
        # 十一运夺金
        'https://api.api861861.com/KillNum/getEfKillNumList.do?lotCode=10008&rows=30&date=%s' % _today,

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
                    'reserved_bit_one': kill_right_or_wrong(i['firstNum']) if i.get('firstNum') else "",
                    'reserved_bit_two': kill_right_or_wrong(i['secondNum']) if i.get('secondNum') else "",
                    'reserved_bit_three': kill_right_or_wrong(i['thirdNum']) if i.get('thirdNum') else "",
                    'reserved_bit_four': kill_right_or_wrong(i['fourthNum']) if i.get('fourthNum') else "",
                    'reserved_bit_five': kill_right_or_wrong(i['fifthNum']) if i.get('fifthNum') else "",
                    'reserved_bit_six': kill_right_or_wrong(i['sixthNum']) if i.get('sixthNum') else "",
                    'reserved_bit_seven': kill_right_or_wrong(i['sevenNum']) if i.get('sevenNum') else "",
                    'reserved_bit_eight': kill_right_or_wrong(i['eightNum']) if i.get('eightNum') else "",
                    'reserved_bit_nine': kill_right_or_wrong(i['nineNum']) if i.get('nineNum') else "",
                    'reserved_bit_ten': kill_right_or_wrong(i['tenNum']) if i.get('tenNum') else "",
                    'lottery_status': 1 if i['preDrawCode'] else 0,
                    'draw_date': now_time,
                    'create_date': now_time
                }
                # print(item)
                yield item
