# -*- coding: utf-8 -*-
import datetime
import uuid

import pymysql
import scrapy
from scrapy.utils.project import get_project_settings

from spider6488.common.common import gyh, lh, released_date, init_trend_lot_full_no_bottom, \
    compute_trend_lot_full_no_bottom, init_trend_gysum_bottom, compute_trend_gysum_bottom

settings = get_project_settings()


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
                'parse_type': 'lottery_number',
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

        # 计算冠亚和走势
        for j in self._compute_trend_gysum(table):
            yield j

        # 计算号码走势
        for i in self._compute_trend_lot_full_no(table):
            yield i

        # 翻页 稳定爬取之后注释以提升爬虫性能
        # next_url = response.xpath('//a[text()="Next"]/@href').extract_first()
        # # print(next_url)     # history.aspx?i=2
        # if int(next_url.split('=')[-1]) < 10:
        #     yield scrapy.Request('https://luck-airship.com/'+next_url, callback=self.parse, dont_filter=False)

    def _compute_trend_lot_full_no(self, table):
        """
        根据开奖号，去计算号码走势
        :param lottery_num:
        :param lot_full_no:
        :return:
        """
        # table = response.xpath('//table//tr')
        for tr in table[-1:0:-1]:
            lottery_num = tr.xpath('./td[2]/text()').extract_first()
            print(lottery_num)
            td3 = tr.xpath('./td[3]//text()').extract()
            lot_full_no = ['{:0>2}'.format(i.strip()) for i in td3 if i.strip()]

            conn = pymysql.connect(**settings['MYSQL_POOL_CONFIG'])
            cursor = conn.cursor()
            cursor.execute("""
                select lottery_full_no, reserved_bit_one, reserved_bit_two, reserved_bit_three, reserved_bit_four,
                reserved_bit_five, reserved_bit_six, reserved_bit_seven, reserved_bit_eight, reserved_bit_nine, reserved_bit_ten
                from sc_lottery_char
                where lottery_code='5004'
                and lottery_char_type=9
                order by lottery_num desc 
                limit 1
            """)
            res = cursor.fetchone()
            # print('##############', res)
            cursor.close()
            conn.close()

            if not res:     # 没有底数 去初始化底数
                now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                item = {
                    'parse_type': 'trend_draw_code',    # 号码走势
                    'id': str(uuid.uuid4()).replace('-', ''),
                    'lottery_code': '5004',
                    'lottery_num': lottery_num,
                    'lottery_full_no': "-".join(lot_full_no),
                    'lottery_char_type': 9,
                    # 第一球
                    'reserved_bit_one': init_trend_lot_full_no_bottom(1, lot_full_no[0]),
                    # 第二球
                    'reserved_bit_two': init_trend_lot_full_no_bottom(2, lot_full_no[1]),
                    # 第三球 依次到第十球
                    'reserved_bit_three': init_trend_lot_full_no_bottom(3, lot_full_no[2]),
                    'reserved_bit_four': init_trend_lot_full_no_bottom(4, lot_full_no[3]),
                    'reserved_bit_five': init_trend_lot_full_no_bottom(5, lot_full_no[4]),
                    'reserved_bit_six': init_trend_lot_full_no_bottom(6, lot_full_no[5]),
                    'reserved_bit_seven': init_trend_lot_full_no_bottom(7, lot_full_no[6]),
                    'reserved_bit_eight': init_trend_lot_full_no_bottom(8, lot_full_no[7]),
                    'reserved_bit_nine': init_trend_lot_full_no_bottom(9, lot_full_no[8]),
                    'reserved_bit_ten': init_trend_lot_full_no_bottom(10, lot_full_no[9]),
                    'is_finish': 0,
                    'draw_date': now_time,
                    'create_date': now_time,
                    'update_date': now_time
                }
            else:
                now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                item = {
                    'parse_type': 'trend_draw_code',    # 号码走势
                    'id': str(uuid.uuid4()).replace('-', ''),
                    'lottery_code': '5004',
                    'lottery_num': lottery_num,
                    'lottery_full_no': "-".join(lot_full_no),
                    'lottery_char_type': 9,
                    # 第一球
                    'reserved_bit_one': compute_trend_lot_full_no_bottom(1, lot_full_no[0], res[1], res[0]),
                    # 第二球
                    'reserved_bit_two': compute_trend_lot_full_no_bottom(2, lot_full_no[1], res[2], res[0]),
                    # 第三球 依次到第十球
                    'reserved_bit_three': compute_trend_lot_full_no_bottom(3, lot_full_no[2], res[3], res[0]),
                    'reserved_bit_four': compute_trend_lot_full_no_bottom(4, lot_full_no[3], res[4], res[0]),
                    'reserved_bit_five': compute_trend_lot_full_no_bottom(5, lot_full_no[4], res[5], res[0]),
                    'reserved_bit_six': compute_trend_lot_full_no_bottom(6, lot_full_no[5], res[6], res[0]),
                    'reserved_bit_seven': compute_trend_lot_full_no_bottom(7, lot_full_no[6], res[7], res[0]),
                    'reserved_bit_eight': compute_trend_lot_full_no_bottom(8, lot_full_no[7], res[8], res[0]),
                    'reserved_bit_nine': compute_trend_lot_full_no_bottom(9, lot_full_no[8], res[9], res[0]),
                    'reserved_bit_ten': compute_trend_lot_full_no_bottom(10, lot_full_no[9], res[10], res[0]),
                    'is_finish': 0,
                    'draw_date': now_time,
                    'create_date': now_time,
                    'update_date': now_time
                }
            # print(item)
            yield item

    def _compute_trend_gysum(self, table):
        """
        根据开奖号去计算
        :param lottery_num:
        :param lot_full_no:
        :return:
        """
        # table = response.xpath('//table//tr')
        for tr in table[-1:0:-1]:
            lottery_num = tr.xpath('./td[2]/text()').extract_first()
            td3 = tr.xpath('./td[3]//text()').extract()
            lot_full_no = ['{:0>2}'.format(i.strip()) for i in td3 if i.strip()]

            conn = pymysql.connect(**settings['MYSQL_POOL_CONFIG'])
            cursor = conn.cursor()
            cursor.execute("""
                select lottery_full_no, reserved_bit_two
                from sc_lottery_char
                where lottery_code='5004'
                and lottery_char_type=10
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
                    'parse_type': 'trend_gysum',
                    'id': str(uuid.uuid4()).replace('-', ''),
                    'lottery_code': '5004',
                    'lottery_num': lottery_num,
                    'lottery_full_no': "-".join(lot_full_no),
                    'lottery_char_type': 10,
                    # 冠亚和
                    'reserved_bit_one': int(lot_full_no[0]) + int(lot_full_no[1]),
                    # 长号码
                    'reserved_bit_two': init_trend_gysum_bottom(lot_full_no),
                    'is_finish': 0,
                    'draw_date': now_time,
                    'create_date': now_time,
                    'update_date': now_time
                }
            else:
                now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                item = {
                    'parse_type': 'trend_gysum',
                    'id': str(uuid.uuid4()).replace('-', ''),
                    'lottery_code': '5004',
                    'lottery_num': lottery_num,
                    'lottery_full_no': "-".join(lot_full_no),
                    'lottery_char_type': 10,
                    # 冠亚和
                    'reserved_bit_one': int(lot_full_no[0]) + int(lot_full_no[1]),
                    # 长号码
                    'reserved_bit_two': compute_trend_gysum_bottom(lot_full_no, res[1], res[0]),
                    'is_finish': 0,
                    'draw_date': now_time,
                    'create_date': now_time,
                    'update_date': now_time
                }
            yield item
