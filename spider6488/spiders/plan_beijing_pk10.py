# -*- coding: utf-8 -*-
import datetime
import json
import uuid

import scrapy


class PlanBeijingPk10Spider(scrapy.Spider):
    name = 'plan_beijing_pk10'
    allowed_domains = ['api.api861861.com']
    # _date = '2020-01-21'
    _today = datetime.datetime.today().strftime('%Y-%m-%d')
    start_urls = ['http://api.api861861.com/LotteryPlan/getBetInfoList.do?date=%s&lotCode=10001' % _today]
    custom_settings = {
        'ITEM_PIPELINES': {'spider6488.pipelines.PlanBeijingPk10Pipeline': 302}
    }

    def parse(self, response):
        """
        双面推荐 北京pk10
        :param response:
        :return:
        """
        # print(response.url.split("/")[-1].split('?'))
        if 'getBetInfoList.do' == response.url.split("/")[-1].split('?')[0]:
            return self.lottery_number_parse(response)

    def lottery_number_parse(self, response):
        """
        开奖号码
        :param response:
        :return:
        """
        res = json.loads(response.text)
        if res['result']['data']:
            for i in res['result']['data']:
                if i['preDrawCode']:
                    item = {
                        'id': str(uuid.uuid4()).replace("-", ""),
                        'lottery_code': 5001,
                        'lottery_num': i['preDrawIssue'],
                        'lottery_full_no': i['preDrawCode'].replace(",", "-"),
                        'lottery_ball_no': i['ballNum'],
                        'ball_is_big': i['bigOrSmall'],  # 0小1大
                        'ball_is_big_score': i['ballBsBet'],
                        'ball_is_single': i['singleOrDouble'],  # 0双1单数
                        'ball_is_single_score': i['ballSdBet'],
                        'sub_score': i['subtotal'],
                        'sum_score': i['sumtotal'],
                        'draw_date': i['preDrawTime'],
                        'create_date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    }
                    # print(item)
                    yield item
