# -*- coding: utf-8 -*-
import datetime
import uuid

import scrapy

from spider6488.common.common import gyh, lh, released_date


class LuckAirshipSpider(scrapy.Spider):
    name = 'luck_airship'
    allowed_domains = ['luck-airship.com']
    start_urls = ['https://luck-airship.com/history.aspx']
    custom_settings = {
        'ITEM_PIPELINES': {'spider6488.pipelines.LuckAirshipPipeline': 305}
    }

    def parse(self, response):
        """
        幸运飞艇
        :param response:
        :return:
        """
        print(response.url)
        table = response.xpath('//table//tr')
        for tr in table[1:]:
            # tr.xpath('./td//text()').extract()
            draw_date = tr.xpath('./td[1]/text()').extract_first()
            lottery_num = tr.xpath('./td[2]/text()').extract_first()
            td3 = tr.xpath('./td[3]//text()').extract()
            lottery_full_no = ['{:0>2}'.format(i.strip()) for i in td3 if i.strip()]
            # print(lottery_full_no)
            crown_and_num = int(lottery_full_no[0]) + int(lottery_full_no[1])
            now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            item = {
                'id': str(uuid.uuid4()).replace("-", ""),
                'lottery_code': 5004,
                'lottery_num': lottery_num,
                'lottery_full_no': "-".join(lottery_full_no),
                # 冠亚和 <一球二球之和>-<大a小b>-<单c双d>
                'lottery_sum_value': gyh(crown_and_num),
                # 1龙2虎
                'reserved_bit_one': lh(lottery_full_no),
                'lottery_countdown': 1,
                'draw_date': released_date(lottery_num, draw_date),
                'create_date': now_time,
                'update_date': now_time
            }
            # print(item)
            yield item
        next_url = response.xpath('//a[text()="Next"]/@href').extract_first()
        # print(next_url)     # history.aspx?i=2
        if int(next_url.split('=')[-1]) < 10:
            yield scrapy.Request('https://luck-airship.com/'+next_url, callback=self.parse, dont_filter=False)

