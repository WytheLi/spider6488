# -*- coding: utf-8 -*-
import datetime
import json
import uuid

import scrapy

from spider6488.common.constants import buy_plan_lot_code_map


_today = datetime.datetime.today().strftime('%Y-%m-%d')


class BuyLotteryPlanSpider(scrapy.Spider):
    name = 'buy_lottery_plan'
    allowed_domains = ['api.api861861.com']
    start_urls = [
        # 购彩计划
        # # SG飞艇
        # 'https://api.api861861.com/LotteryPlan/getPksPlanList.do?lotCode=10058&rows=100&date=%s' % _today,
        # 北京PK10
        'https://api.api861861.com/LotteryPlan/getPksPlanList.do?lotCode=10001&rows=100&date=%s' % _today,
        # # 极速赛车
        # 'https://api.api861861.com/LotteryPlan/getPksPlanList.do?lotCode=10037&rows=100&date=%s' % _today,
        # # 澳洲幸运十
        # 'https://api.api861861.com/LotteryPlan/getPksPlanList.do?lotCode=10012&rows=100&date=%s' % _today,
        # # 极速飞艇
        # 'https://api.api861861.com/LotteryPlan/getPksPlanList.do?lotCode=10035&rows=100&date=%s' % _today,
    
        # # 重庆欢乐生肖
        # 'https://api.api861861.com/LotteryPlan/getSscPlanList.do?lotCode=10060&rows=100&date=%s' % _today,
        # # 幸运时时彩
        # 'https://api.api861861.com/LotteryPlan/getSscPlanList.do?lotCode=10059&rows=100&date=%s' % _today,
        # 天津时时彩
        'https://api.api861861.com/LotteryPlan/getSscPlanList.do?lotCode=10003&rows=100&date=%s' % _today,
        # # 台湾5分彩
        # 'https://api.api861861.com/LotteryPlan/getSscPlanList.do?lotCode=10064&rows=100&date=%s' % _today,
        # 新疆时时彩
        'https://api.api861861.com/LotteryPlan/getSscPlanList.do?lotCode=10004&rows=100&date=%s' % _today,
        # # 极速时时彩
        # 'https://api.api861861.com/LotteryPlan/getSscPlanList.do?lotCode=10036&rows=100&date=%s' % _today,
        # # 澳洲幸运5
        # 'https://api.api861861.com/LotteryPlan/getSscPlanList.do?lotCode=10010&rows=100&date=%s' % _today,
    
        # 广东11选5
        'https://api.api861861.com/LotteryPlan/getEfPlanList.do?lotCode=10006&rows=100&date=%s' % _today,
        # 浙江11选5
        'https://api.api861861.com/LotteryPlan/getEfPlanList.do?lotCode=10025&rows=100&date=%s' % _today,
        # 江西11选5
        'https://api.api861861.com/LotteryPlan/getEfPlanList.do?lotCode=10015&rows=100&date=%s' % _today,
        # 江苏11选5
        'https://api.api861861.com/LotteryPlan/getEfPlanList.do?lotCode=10016&rows=100&date=%s' % _today,
        # 安徽11选5
        'https://api.api861861.com/LotteryPlan/getEfPlanList.do?lotCode=10017&rows=100&date=%s' % _today,
        # 上海11选5
        'https://api.api861861.com/LotteryPlan/getEfPlanList.do?lotCode=10018&rows=100&date=%s' % _today,
        # 辽宁11选5
        'https://api.api861861.com/LotteryPlan/getEfPlanList.do?lotCode=10019&rows=100&date=%s' % _today,
        # 湖北11选5
        'https://api.api861861.com/LotteryPlan/getEfPlanList.do?lotCode=10020&rows=100&date=%s' % _today,
        # 广西11选5
        'https://api.api861861.com/LotteryPlan/getEfPlanList.do?lotCode=10022&rows=100&date=%s' % _today,
        # 吉林11选5
        'https://api.api861861.com/LotteryPlan/getEfPlanList.do?lotCode=10023&rows=100&date=%s' % _today,
        # 内蒙古11选5
        'https://api.api861861.com/LotteryPlan/getEfPlanList.do?lotCode=10024&rows=100&date=%s' % _today,
        # 十一运夺金
        'https://api.api861861.com/LotteryPlan/getEfPlanList.do?lotCode=10008&rows=100&date=%s' % _today,
    
        # 江苏快3
        'https://api.api861861.com/LotteryPlan/getKsPlanList.do?lotCode=10007&rows=100&date=%s' % _today,
        # 广西快3
        'https://api.api861861.com/LotteryPlan/getKsPlanList.do?lotCode=10026&rows=100&date=%s' % _today,
        # 吉林快3
        'https://api.api861861.com/LotteryPlan/getKsPlanList.do?lotCode=10027&rows=100&date=%s' % _today,
        # 河北快3
        'https://api.api861861.com/LotteryPlan/getKsPlanList.do?lotCode=10028&rows=100&date=%s' % _today,
        # # 内蒙古快3
        # 'https://api.api861861.com/LotteryPlan/getKsPlanList.do?lotCode=10029&rows=100&date=%s' % _today,
        # 安徽快3
        'https://api.api861861.com/LotteryPlan/getKsPlanList.do?lotCode=10030&rows=100&date=%s' % _today,
        # # 福建快3
        # 'https://api.api861861.com/LotteryPlan/getKsPlanList.do?lotCode=10031&rows=100&date=%s' % _today,
        # 湖北快3
        'https://api.api861861.com/LotteryPlan/getKsPlanList.do?lotCode=10032&rows=100&date=%s' % _today,
        # 北京快3
        'https://api.api861861.com/LotteryPlan/getKsPlanList.do?lotCode=10033&rows=100&date=%s' % _today,
        # 上海快3
        'https://api.api861861.com/LotteryPlan/getKsPlanList.do?lotCode=10061&rows=100&date=%s' % _today,
        # 贵州快3
        'https://api.api861861.com/LotteryPlan/getKsPlanList.do?lotCode=10062&rows=100&date=%s' % _today,
        # 甘肃快3
        'https://api.api861861.com/LotteryPlan/getKsPlanList.do?lotCode=10063&rows=100&date=%s' % _today,
    
        # PC蛋蛋幸运28
        'https://api.api861861.com/LotteryPlan/getPc28PlanList.do?lotCode=10046&rows=100&date=%s' % _today,
    
        # 广东快乐十分
        'https://api.api861861.com/LotteryPlan/getKlsfPlanList.do?lotCode=10005&rows=100&date=%s' % _today,
        # 天津快乐十分
        'https://api.api861861.com/LotteryPlan/getKlsfPlanList.do?lotCode=10034&rows=100&date=%s' % _today,
        # # 澳洲幸运8
        # 'https://api.api861861.com/LotteryPlan/getKlsfPlanList.do?lotCode=10011&rows=100&date=%s' % _today,
        # 重庆幸运农场
        'https://api.api861861.com/LotteryPlan/getKlsfPlanList.do?lotCode=10009&rows=100&date=%s' % _today,
    ]
    custom_settings = {
        'ITEM_PIPELINES': {'spider6488.pipelines.BuyLotteryPlanPipeline': 308}
    }

    def parse(self, response):
        print(response.url)
        lot_code = response.url.split('?')[-1].split('&')[0].split('=')[1]
        res = json.loads(response.text)
        if res['result']['data']:
            for i in res['result']['data']:
                # 由于不是所有彩票期号都包含日期信息 所以这里获取爬虫的当前日期
                # _date = '%(y)s-%(m)s-%(d)s' % {'y': i['preDrawIssue'][:4], 'm': i['preDrawIssue'][4:6], 'd': i['preDrawIssue'][6:8]}
                _date = datetime.datetime.now().strftime('%Y-%m-%d')
                now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                item = {
                    'id': str(uuid.uuid4()).replace('-', ''),
                    'lottery_code': buy_plan_lot_code_map[lot_code],
                    'lottery_num': i['preDrawIssue'],
                    'lottery_full_no': i['preDrawCode'].replace(',', '-'),
                    'lottery_plan_a': i['planA'].replace(',', '-'),
                    'lottery_plan_b': i['planB'].replace(',', '-'),
                    'lottery_plan_c': i['planC'].replace(',', '-'),
                    'lottery_cost_current_a': i['lotteryCostA'],
                    'lottery_cost_current_b': i['lotteryCostB'],
                    'lottery_cost_current_c': i['lotteryCostC'],
                    'lottery_cost_total_a': i['lotteryCostAllA'],
                    'lottery_cost_total_b': i['lotteryCostAllB'],
                    'lottery_cost_total_c': i['lotteryCostAllC'],
                    'lottery_profit_a': i['profitA'],
                    'lottery_profit_b': i['profitB'],
                    'lottery_profit_c': i['profitC'],
                    'lottery_status': 1 if i['preDrawCode'] else 0,     # 0待开 1已开
                    'draw_date': _date + ' ' + i['preDrawTime'],
                    'create_date': now_time
                }
                # print(item)
                yield item
