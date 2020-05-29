# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from scrapy.utils.project import get_project_settings

settings = get_project_settings()
print(settings['MYSQL_POOL_CONFIG'])


class Spider6488Pipeline:
    def process_item(self, item, spider):
        return item


class SgAirshipPipeline:    # 301
    def process_item(self, item, spider):
        """
        SG飞艇
        :param item:
        :param spider:
        :return:
        """
        # print(item)
        conn = pymysql.connect(**settings['MYSQL_POOL_CONFIG'])
        cursor = conn.cursor()
        cursor.execute(
            """select lottery_num from sc_lottery_two_side where lottery_num=%(lottery_num)s and lottery_code=%(lottery_code)s""",
            {'lottery_num': item['lottery_num'], 'lottery_code': item['lottery_code']})
        result = cursor.fetchone()
        # print(result)
        if not result:
            try:
                sql = """
                    insert into sc_lottery_two_side(id, lottery_code, lottery_num, lottery_full_no, 
                                            lottery_ball_no, ball_is_big, ball_is_big_score, ball_is_single, 
                                            ball_is_single_score, sub_score, sum_score, draw_date, 
                                            create_date)
                    values (%(id)s, %(lottery_code)s, %(lottery_num)s, %(lottery_full_no)s,
                            %(lottery_ball_no)s, %(ball_is_big)s, %(ball_is_big_score)s, %(ball_is_single)s,
                            %(ball_is_single_score)s, %(sub_score)s, %(sum_score)s, %(draw_date)s,
                            %(create_date)s)
                """
                cursor.execute(sql, item)
                conn.commit()
            except Exception as e:
                raise e
            else:
                conn.commit()
                # print(item)
            finally:
                cursor.close()
                conn.close()


class PlanBeijingPk10Pipeline:      # 302
    def process_item(self, item, spider):
        """
        双面推荐 pk10
        :param item:
        :param spider:
        :return:
        """
        conn = pymysql.connect(**settings['MYSQL_POOL_CONFIG'])
        cursor = conn.cursor()
        cursor.execute(
            """select lottery_num from sc_lottery_two_side where lottery_num=%(lottery_num)s and lottery_code=%(lottery_code)s""",
            {'lottery_num': item['lottery_num'], 'lottery_code': item['lottery_code']})
        result = cursor.fetchone()
        print(result)
        if not result:
            try:
                sql = """
                    insert into sc_lottery_two_side(id, lottery_code, lottery_num, lottery_full_no, 
                                            lottery_ball_no, ball_is_big, ball_is_big_score, ball_is_single, 
                                            ball_is_single_score, sub_score, sum_score, draw_date, 
                                            create_date)
                    values (%(id)s, %(lottery_code)s, %(lottery_num)s, %(lottery_full_no)s,
                            %(lottery_ball_no)s, %(ball_is_big)s, %(ball_is_big_score)s, %(ball_is_single)s,
                            %(ball_is_single_score)s, %(sub_score)s, %(sum_score)s, %(draw_date)s,
                            %(create_date)s)
                """
                res = cursor.execute(sql, item)
            except Exception as e:
                raise e
            else:
                conn.commit()
                # print({'res_code': res, 'item': item})
            finally:
                cursor.close()
                conn.close()


class Anhui11x5SpiderPipeline:
    def process_item(self, item, spider):
        """
        安徽11选5
        :param item:
        :param spider:
        :return:
        """
        conn = pymysql.connect(**settings['MYSQL_POOL_CONFIG'])
        cursor = conn.cursor()
        if 'lottery_number' == item[1]:     # 开奖号码
            cursor.execute("""
            select * from sc_lottery_info where lottery_num=%(lottery_num)s and lottery_code=%(lottery_code)s
            """, {'lottery_num': item[0]['lottery_num'], 'lottery_code': item[0]['lottery_code']})
            result = cursor.fetchone()
            if not result:
                try:
                    sql = """
                        insert into sc_lottery_info(id, lottery_code, lottery_num, lottery_full_no, lottery_sum_value,
                        reserved_bit_one, reserved_bit_two, reserved_bit_three, reserved_bit_four, lottery_countdown,
                        draw_date, create_date, update_date)
                        values (%(id)s, %(lottery_code)s, %(lottery_num)s, %(lottery_full_no)s, %(lottery_sum_value)s,
                        %(reserved_bit_one)s, %(reserved_bit_two)s, %(reserved_bit_three)s, %(reserved_bit_four)s, %(lottery_countdown)s,
                        %(draw_date)s, %(create_date)s, %(update_date)s)
                    """
                    res = cursor.execute(sql, item[0])
                except Exception as e:
                    raise e
                else:
                    conn.commit()
                    # print({'res_code': res, 'item': item[0]})
                finally:
                    cursor.close()
                    conn.close()
        elif 'trend_by_issue' == item[1]:   # 基本走势
            cursor.execute("""
                select * from sc_lottery_char where lottery_num=%(lottery_num)s and lottery_code=%(lottery_code)s and lottery_char_type=%(lottery_char_type)s
            """, {'lottery_num': item[0]['lottery_num'], 'lottery_code': item[0]['lottery_code'], 'lottery_char_type': item[0]['lottery_char_type']})
            result = cursor.fetchone()
            if not result:
                try:
                    sql = """
                        insert into sc_lottery_char(id, lottery_code, lottery_num, lottery_full_no, lottery_char_type,
                        reserved_bit_one, reserved_bit_two, reserved_bit_three, reserved_bit_four, reserved_bit_five,
                        is_finish, draw_date, create_date, update_date)
                        values (%(id)s, %(lottery_code)s, %(lottery_num)s, %(lottery_full_no)s, %(lottery_char_type)s,
                        %(reserved_bit_one)s, %(reserved_bit_two)s, %(reserved_bit_three)s, %(reserved_bit_four)s, %(reserved_bit_five)s,
                        %(is_finish)s, %(draw_date)s, %(create_date)s, %(update_date)s)
                    """
                    res = cursor.execute(sql, item[0])
                except Exception as e:
                    raise e
                else:
                    conn.commit()
                    # print({'res_code': res, 'item': item[0]})
                finally:
                    cursor.close()
                    conn.close()

        elif 'trend_dtt' == item[1]:     # 龙虎走势
            cursor.execute("""
                select * from sc_lottery_char where lottery_code=%(lottery_code)s and lottery_num=%(lottery_num)s and lottery_char_type=%(lottery_char_type)s
            """, {'lottery_code': item[0]['lottery_code'], 'lottery_num': item[0]['lottery_num'], 'lottery_char_type': item[0]['lottery_char_type']})
            result = cursor.fetchone()
            if not result:
                try:
                    sql = """
                        insert into sc_lottery_char(id, lottery_code, lottery_num, lottery_full_no, 
                        lottery_char_type, reserved_bit_one, reserved_bit_two, reserved_bit_three, is_finish,
                        draw_date, create_date, update_date)
                        values (%(id)s, %(lottery_code)s, %(lottery_num)s, %(lottery_full_no)s,
                        %(lottery_char_type)s, %(reserved_bit_one)s, %(reserved_bit_two)s, %(reserved_bit_three)s, %(is_finish)s,
                        %(draw_date)s, %(create_date)s, %(update_date)s)
                    """
                    res = cursor.execute(sql, item[0])
                except Exception as e:
                    raise e
                else:
                    conn.commit()
                    # print({'res_code': res, 'item': item[0]})
                finally:
                    cursor.close()
                    conn.close()
        elif 'trend_sum' == item[1]:     # 和值走势
            cursor.execute("""
                select * from sc_lottery_char where lottery_code=%(lottery_code)s and lottery_num=%(lottery_num)s and lottery_char_type=%(lottery_char_type)s
            """, {'lottery_code': item[0]['lottery_code'], 'lottery_num': item[0]['lottery_num'], 'lottery_char_type': item[0]['lottery_char_type']})
            result = cursor.fetchone()
            if not result:
                try:
                    sql = """
                        insert into sc_lottery_char(id, lottery_code, lottery_num, lottery_full_no, 
                        lottery_char_type, reserved_bit_one, reserved_bit_two, reserved_bit_three, is_finish,
                        draw_date, create_date, update_date)
                        values (%(id)s, %(lottery_code)s, %(lottery_num)s, %(lottery_full_no)s,
                        %(lottery_char_type)s, %(reserved_bit_one)s, %(reserved_bit_two)s, %(reserved_bit_three)s, %(is_finish)s,
                        %(draw_date)s, %(create_date)s, %(update_date)s)
                    """
                    res = cursor.execute(sql, item[0])
                except Exception as e:
                    raise e
                else:
                    conn.commit()
                    # print({'res_code': res, 'item': item[0]})
                finally:
                    cursor.close()
                    conn.close()


class Com1680380_11x5Pipeline:  # 303
    def process_item(self, item, spider):
        """
        11选5
        :param item:
        :param spider:
        :return:
        """
        conn = pymysql.connect(**settings['MYSQL_POOL_CONFIG'])
        cursor = conn.cursor()
        if 'lottery_number' == item['parse_type']:     # 开奖号码
            cursor.execute("""
            select * from sc_lottery_info where lottery_num=%(lottery_num)s and lottery_code=%(lottery_code)s
            """, {'lottery_num': item['lottery_num'], 'lottery_code': item['lottery_code']})
            result = cursor.fetchone()
            if not result:
                try:
                    sql = """
                        insert into sc_lottery_info(id, lottery_code, lottery_num, lottery_full_no, lottery_sum_value,
                        reserved_bit_one, reserved_bit_two, reserved_bit_three, reserved_bit_four, lottery_countdown,
                        draw_date, create_date, update_date)
                        values (%(id)s, %(lottery_code)s, %(lottery_num)s, %(lottery_full_no)s, %(lottery_sum_value)s,
                        %(reserved_bit_one)s, %(reserved_bit_two)s, %(reserved_bit_three)s, %(reserved_bit_four)s, %(lottery_countdown)s,
                        %(draw_date)s, %(create_date)s, %(update_date)s)
                    """
                    cursor.execute(sql, item)
                except Exception as e:
                    raise e
                else:
                    conn.commit()
                    # print(item)
                finally:
                    cursor.close()
                    conn.close()
        elif 'trend_by_issue' == item['parse_type']:   # 基本走势
            cursor.execute("""
                select * from sc_lottery_char where lottery_num=%(lottery_num)s and lottery_code=%(lottery_code)s and lottery_char_type=%(lottery_char_type)s
            """, {'lottery_num': item['lottery_num'], 'lottery_code': item['lottery_code'], 'lottery_char_type': item['lottery_char_type']})
            result = cursor.fetchone()
            if not result:
                try:
                    sql = """
                        insert into sc_lottery_char(id, lottery_code, lottery_num, lottery_full_no, lottery_char_type,
                        reserved_bit_one, reserved_bit_two, reserved_bit_three, reserved_bit_four, reserved_bit_five,
                        is_finish, draw_date, create_date, update_date)
                        values (%(id)s, %(lottery_code)s, %(lottery_num)s, %(lottery_full_no)s, %(lottery_char_type)s,
                        %(reserved_bit_one)s, %(reserved_bit_two)s, %(reserved_bit_three)s, %(reserved_bit_four)s, %(reserved_bit_five)s,
                        %(is_finish)s, %(draw_date)s, %(create_date)s, %(update_date)s)
                    """
                    cursor.execute(sql, item)
                except Exception as e:
                    raise e
                else:
                    conn.commit()
                    # print(item)
                finally:
                    cursor.close()
                    conn.close()

        elif 'trend_dtt' == item['parse_type']:     # 龙虎走势
            cursor.execute("""
                select * from sc_lottery_char 
                where lottery_code=%(lottery_code)s 
                and lottery_num=%(lottery_num)s 
                and lottery_char_type=%(lottery_char_type)s
            """, {'lottery_code': item['lottery_code'], 'lottery_num': item['lottery_num'], 'lottery_char_type': item['lottery_char_type']})
            result = cursor.fetchone()
            if not result:
                try:
                    sql = """
                        insert into sc_lottery_char(id, lottery_code, lottery_num, lottery_full_no, 
                        lottery_char_type, reserved_bit_one, reserved_bit_two, reserved_bit_three, 
                        is_finish, draw_date, create_date, update_date)
                        values (%(id)s, %(lottery_code)s, %(lottery_num)s, %(lottery_full_no)s,
                        %(lottery_char_type)s, %(reserved_bit_one)s, %(reserved_bit_two)s, %(reserved_bit_three)s, 
                        %(is_finish)s, %(draw_date)s, %(create_date)s, %(update_date)s)
                    """
                    cursor.execute(sql, item)
                except Exception as e:
                    raise e
                else:
                    conn.commit()
                    # print(item)
                finally:
                    cursor.close()
                    conn.close()
        elif 'trend_sum' == item['parse_type']:     # 和值走势
            cursor.execute("""
                select * from sc_lottery_char where lottery_code=%(lottery_code)s and lottery_num=%(lottery_num)s and lottery_char_type=%(lottery_char_type)s
            """, {'lottery_code': item['lottery_code'], 'lottery_num': item['lottery_num'], 'lottery_char_type': item['lottery_char_type']})
            result = cursor.fetchone()
            if not result:
                try:
                    sql = """
                        insert into sc_lottery_char(id, lottery_code, lottery_num, lottery_full_no, 
                        lottery_char_type, reserved_bit_one, reserved_bit_two, reserved_bit_three, is_finish,
                        draw_date, create_date, update_date)
                        values (%(id)s, %(lottery_code)s, %(lottery_num)s, %(lottery_full_no)s,
                        %(lottery_char_type)s, %(reserved_bit_one)s, %(reserved_bit_two)s, %(reserved_bit_three)s, %(is_finish)s,
                        %(draw_date)s, %(create_date)s, %(update_date)s)
                    """
                    cursor.execute(sql, item)
                except Exception as e:
                    raise e
                else:
                    conn.commit()
                    # print(item)
                finally:
                    cursor.close()
                    conn.close()


class Com1680380K3Pipeline:     #  304
    def process_item(self, item, spider):
        """
        快3
        :param item:
        :param spider:
        :return:
        """
        conn = pymysql.connect(**settings['MYSQL_POOL_CONFIG'])
        cursor = conn.cursor()
        if 'lottery_number' == item['parse_type']:     # 开奖号码
            cursor.execute("""
            select * from sc_lottery_info 
            where lottery_num=%(lottery_num)s and lottery_code=%(lottery_code)s
            """, {'lottery_num': item['lottery_num'], 'lottery_code': item['lottery_code']})
            result = cursor.fetchone()
            if not result:
                try:
                    sql = """
                        insert into sc_lottery_info(id, lottery_code, lottery_num, lottery_full_no,
                        lottery_sum_value, reserved_bit_one, lottery_countdown,
                        draw_date, create_date, update_date)
                        values (%(id)s, %(lottery_code)s, %(lottery_num)s, %(lottery_full_no)s,
                        %(lottery_sum_value)s, %(reserved_bit_one)s, %(lottery_countdown)s,
                        %(draw_date)s, %(create_date)s, %(update_date)s)
                    """
                    cursor.execute(sql, item)
                except Exception as e:
                    raise e
                else:
                    conn.commit()
                    # print(item)
                finally:
                    cursor.close()
                    conn.close()
        elif 'trend_qrientation' == item['parse_type']:    # 定位走势
            cursor.execute("""
                select * from sc_lottery_char 
                where lottery_num=%(lottery_num)s 
                and lottery_code=%(lottery_code)s 
                and lottery_char_type=%(lottery_char_type)s
            """, {'lottery_num': item['lottery_num'], 'lottery_code': item['lottery_code'], 'lottery_char_type': item['lottery_char_type']})
            result = cursor.fetchone()
            if not result:
                try:
                    sql = """
                        insert into sc_lottery_char(id, lottery_code, lottery_num, lottery_full_no,
                        lottery_char_type, reserved_bit_one, reserved_bit_two, reserved_bit_three,
                        is_finish, draw_date, create_date, update_date)
                        values (%(id)s, %(lottery_code)s, %(lottery_num)s, %(lottery_full_no)s,
                        %(lottery_char_type)s, %(reserved_bit_one)s, %(reserved_bit_two)s, %(reserved_bit_three)s,
                        %(is_finish)s, %(draw_date)s, %(create_date)s, %(update_date)s)
                    """
                    cursor.execute(sql, item)
                except Exception as e:
                    raise e
                else:
                    conn.commit()
                    # print(item)
                finally:
                    cursor.close()
                    conn.close()
        elif 'trend_big_and_small' == item['parse_type']:  # 大小走势
            cursor.execute("""
                select * from sc_lottery_char 
                where lottery_num=%(lottery_num)s 
                and lottery_code=%(lottery_code)s 
                and lottery_char_type=%(lottery_char_type)s
            """, {'lottery_num': item['lottery_num'], 'lottery_code': item['lottery_code'], 'lottery_char_type': item['lottery_char_type']})
            result = cursor.fetchone()
            if not result:
                try:
                    sql = """
                        insert into sc_lottery_char(id, lottery_code, lottery_num, lottery_full_no, lottery_char_type,
                        reserved_bit_one, reserved_bit_two, reserved_bit_three, reserved_bit_four,
                        reserved_bit_five, reserved_bit_six, reserved_bit_seven, is_finish,
                        draw_date, create_date, update_date)
                        values (%(id)s, %(lottery_code)s, %(lottery_num)s, %(lottery_full_no)s, %(lottery_char_type)s,
                        %(reserved_bit_one)s, %(reserved_bit_two)s, %(reserved_bit_three)s, %(reserved_bit_four)s,
                        %(reserved_bit_five)s, %(reserved_bit_six)s, %(reserved_bit_seven)s, %(is_finish)s,
                        %(draw_date)s, %(create_date)s, %(update_date)s)
                    """
                    cursor.execute(sql, item)
                except Exception as e:
                    raise e
                else:
                    conn.commit()
                    # print(item)
                finally:
                    cursor.close()
                    conn.close()
        elif 'trend_sum' == item['parse_type']:    # 和值走势
            cursor.execute("""
                select * from sc_lottery_char 
                where lottery_num=%(lottery_num)s 
                and lottery_code=%(lottery_code)s 
                and lottery_char_type=%(lottery_char_type)s
            """, {'lottery_num': item['lottery_num'], 'lottery_code': item['lottery_code'], 'lottery_char_type': item['lottery_char_type']})
            result = cursor.fetchone()
            if not result:
                try:
                    sql = """
                        insert into sc_lottery_char(id, lottery_code, lottery_num, lottery_full_no, lottery_char_type,
                        reserved_bit_one, reserved_bit_two, is_finish, draw_date, create_date, update_date)
                        values (%(id)s, %(lottery_code)s, %(lottery_num)s, %(lottery_full_no)s, %(lottery_char_type)s,
                        %(reserved_bit_one)s, %(reserved_bit_two)s, %(is_finish)s, %(draw_date)s, %(create_date)s, %(update_date)s)
                    """
                    cursor.execute(sql, item)
                except Exception as e:
                    raise e
                else:
                    conn.commit()
                    # print(item)
                finally:
                    cursor.close()
                    conn.close()
        elif 'trend_basic' == item['parse_type']:  # 基本走势
            cursor.execute("""
                select * from sc_lottery_char 
                where lottery_num=%(lottery_num)s 
                and lottery_code=%(lottery_code)s 
                and lottery_char_type=%(lottery_char_type)s
            """, {'lottery_num': item['lottery_num'], 'lottery_code': item['lottery_code'], 'lottery_char_type': item['lottery_char_type']})
            result = cursor.fetchone()
            if not result:
                try:
                    sql = """
                        insert into sc_lottery_char(id, lottery_code, lottery_num, lottery_full_no,
                        lottery_char_type, reserved_bit_one, reserved_bit_two, reserved_bit_three,
                        is_finish, draw_date, create_date, update_date)
                        values (%(id)s, %(lottery_code)s, %(lottery_num)s, %(lottery_full_no)s,
                        %(lottery_char_type)s, %(reserved_bit_one)s, %(reserved_bit_two)s, %(reserved_bit_three)s,
                        %(is_finish)s, %(draw_date)s, %(create_date)s, %(update_date)s)
                    """
                    cursor.execute(sql, item)
                except Exception as e:
                    raise e
                else:
                    conn.commit()
                    # print(item)
                finally:
                    cursor.close()
                    conn.close()
        elif 'trend_odd_and_even' == item['parse_type']:   # 基偶走势
            try:
                cursor.execute("""
                    select * from sc_lottery_char 
                    where lottery_num=%(lottery_num)s 
                    and lottery_code=%(lottery_code)s 
                    and lottery_char_type=%(lottery_char_type)s
                """, {'lottery_num': item['lottery_num'], 'lottery_code': item['lottery_code'], 'lottery_char_type': item['lottery_char_type']})
                result = cursor.fetchone()
                if not result:
                    sql = """
                        insert into sc_lottery_char(id, lottery_code, lottery_num, lottery_full_no, lottery_char_type,
                        reserved_bit_one, reserved_bit_two, reserved_bit_three, reserved_bit_four,
                        reserved_bit_five, reserved_bit_six, reserved_bit_seven, is_finish,
                        draw_date, create_date, update_date)
                        values (%(id)s, %(lottery_code)s, %(lottery_num)s, %(lottery_full_no)s, %(lottery_char_type)s,
                        %(reserved_bit_one)s, %(reserved_bit_two)s, %(reserved_bit_three)s, %(reserved_bit_four)s,
                        %(reserved_bit_five)s, %(reserved_bit_six)s, %(reserved_bit_seven)s, %(is_finish)s,
                        %(draw_date)s, %(create_date)s, %(update_date)s)
                    """
                    cursor.execute(sql, item)
            except Exception as e:
                raise e
            else:
                conn.commit()
                # print(item)
            finally:
                cursor.close()
                conn.close()


class LuckAirshipPipeline:  # 305
    def process_item(self, item, spider):
        """
        幸运飞艇
        :param item:
        :param spider:
        :return:
        """
        conn = pymysql.connect(**settings['MYSQL_POOL_CONFIG'])
        cursor = conn.cursor()
        cursor.execute(
            """select * from sc_lottery_info where lottery_num=%(lottery_num)s and lottery_code=%(lottery_code)s""",
            {'lottery_num': item['lottery_num'], 'lottery_code': item['lottery_code']})
        result = cursor.fetchone()
        if not result:
            try:
                sql = """
                    insert into sc_lottery_info(id, lottery_code, lottery_num, lottery_full_no, 
                    lottery_sum_value, reserved_bit_one, lottery_countdown,
                    draw_date, create_date, update_date)
                    values (%(id)s, %(lottery_code)s, %(lottery_num)s, %(lottery_full_no)s,
                    %(lottery_sum_value)s, %(reserved_bit_one)s, %(lottery_countdown)s,
                    %(draw_date)s, %(create_date)s, %(update_date)s)
                """
                res = cursor.execute(sql, item)
                conn.commit()
            except Exception as e:
                raise e
            else:
                conn.commit()
                # print({'res_code': res, 'item': item})
            finally:
                cursor.close()
                conn.close()


class PcBallsLuck28Pipeline:        # 306
    def process_item(self, item, spider):
        """
        PC蛋蛋幸运28
        :param item:
        :param spider:
        :return:
        """
        conn = pymysql.connect(**settings['MYSQL_POOL_CONFIG'])
        cursor = conn.cursor()
        cursor.execute(
            """select * from sc_lottery_info where lottery_num=%(lottery_num)s and lottery_code=%(lottery_code)s""",
            {'lottery_num': item['lottery_num'], 'lottery_code': item['lottery_code']})
        result = cursor.fetchone()
        if not result:
            try:
                sql = """
                    insert into sc_lottery_info(id, lottery_code, lottery_num, lottery_full_no, 
                    lottery_sum_value, lottery_countdown,
                    draw_date, create_date, update_date)
                    values (%(id)s, %(lottery_code)s, %(lottery_num)s, %(lottery_full_no)s,
                    %(lottery_sum_value)s, %(lottery_countdown)s,
                    %(draw_date)s, %(create_date)s, %(update_date)s)
                """
                res = cursor.execute(sql, item)
                # conn.commit()
            except Exception as e:
                raise e
            else:
                conn.commit()
                # print({'res_code': res, 'item': item})
            finally:
                cursor.close()
                conn.close()


class ChongqSscPipeline:    # 307
    def process_item(self, item, spider):
        """
        重庆时时彩
        :param item:
        :param spider:
        :return:
        """
        conn = pymysql.connect(**settings['MYSQL_POOL_CONFIG'])
        cursor = conn.cursor()
        if 'lottery_number' == item['parse_type']:     # 开奖号码
            cursor.execute("""
            select * from sc_lottery_info where lottery_num=%(lottery_num)s and lottery_code=%(lottery_code)s
            """, {'lottery_num': item['lottery_num'], 'lottery_code': item['lottery_code']})
            result = cursor.fetchone()
            if not result:
                try:
                    sql = """
                        insert into sc_lottery_info(id, lottery_code, lottery_num, lottery_full_no,
                        lottery_sum_value, reserved_bit_one, reserved_bit_four, lottery_countdown, 
                        draw_date, create_date, update_date)
                        values (%(id)s, %(lottery_code)s, %(lottery_num)s, %(lottery_full_no)s,
                        %(lottery_sum_value)s, %(reserved_bit_one)s, %(reserved_bit_four)s, %(lottery_countdown)s, 
                        %(draw_date)s, %(create_date)s, %(update_date)s)
                    """
                    res = cursor.execute(sql, item)
                except Exception as e:
                    raise e
                else:
                    conn.commit()
                    # print({'res_code': res, 'data': item})
                finally:
                    cursor.close()
                    conn.close()
        elif 'trend_issue' == item['parse_type']:
            cursor.execute("""
                select * from sc_lottery_char where lottery_num=%(lottery_num)s and lottery_code=%(lottery_code)s and lottery_char_type=%(lottery_char_type)s
            """, {'lottery_num': item['lottery_num'], 'lottery_code': item['lottery_code'], 'lottery_char_type': item['lottery_char_type']})
            result = cursor.fetchone()
            if not result:
                try:
                    sql = """
                        insert into sc_lottery_char(id, lottery_code, lottery_num, lottery_full_no, lottery_char_type,
                        reserved_bit_one, reserved_bit_two, reserved_bit_three, reserved_bit_four, reserved_bit_five,
                        is_finish, draw_date, create_date, update_date)
                        values (%(id)s, %(lottery_code)s, %(lottery_num)s, %(lottery_full_no)s, %(lottery_char_type)s,
                        %(reserved_bit_one)s, %(reserved_bit_two)s, %(reserved_bit_three)s, %(reserved_bit_four)s, %(reserved_bit_five)s,
                        %(is_finish)s, %(draw_date)s, %(create_date)s, %(update_date)s)
                    """
                    res = cursor.execute(sql, item)
                except Exception as e:
                    raise e
                else:
                    conn.commit()
                    # print({'res_code': res, 'item': item})
                finally:
                    cursor.close()
                    conn.close()
        elif 'trend_dt' == item['parse_type']:
            cursor.execute("""
                select * from sc_lottery_char where lottery_num=%(lottery_num)s and lottery_code=%(lottery_code)s and lottery_char_type=%(lottery_char_type)s
            """, {'lottery_num': item['lottery_num'], 'lottery_code': item['lottery_code'], 'lottery_char_type': item['lottery_char_type']})
            result = cursor.fetchone()
            if not result:
                try:
                    sql = """
                        insert into sc_lottery_char(id, lottery_code, lottery_num, lottery_full_no, lottery_char_type,
                        reserved_bit_one, reserved_bit_two, reserved_bit_three,
                        is_finish, draw_date, create_date, update_date)
                        values (%(id)s, %(lottery_code)s, %(lottery_num)s, %(lottery_full_no)s, %(lottery_char_type)s,
                        %(reserved_bit_one)s, %(reserved_bit_two)s, %(reserved_bit_three)s,
                        %(is_finish)s, %(draw_date)s, %(create_date)s, %(update_date)s)
                    """
                    res = cursor.execute(sql, item)
                except Exception as e:
                    raise e
                else:
                    conn.commit()
                    # print({'res_code': res, 'item': item})
                finally:
                    cursor.close()
                    conn.close()


class BuyLotteryPlanPipeline:   # 308
    def process_item(self, item, spider):
        conn = pymysql.connect(**settings['MYSQL_POOL_CONFIG'])
        cursor = conn.cursor()
        try:
            cursor.execute("""
            select lottery_code, lottery_num, lottery_status from sc_lottery_buy_plan 
            where lottery_num=%(lottery_num)s and lottery_code=%(lottery_code)s
            """, {'lottery_num': item['lottery_num'], 'lottery_code': item['lottery_code']})
            result = cursor.fetchone()
            if not result:  # 记录不存在，插入
                sql = """
                    insert into sc_lottery_buy_plan(id, lottery_code, lottery_num, lottery_full_no,
                    lottery_plan_a, lottery_plan_b, lottery_plan_c,
                    lottery_cost_current_a, lottery_cost_current_b, lottery_cost_current_c,
                    lottery_cost_total_a, lottery_cost_total_b, lottery_cost_total_c,
                    lottery_profit_a, lottery_profit_b, lottery_profit_c,
                    lottery_status, draw_date, create_date)
                    values (%(id)s, %(lottery_code)s, %(lottery_num)s, %(lottery_full_no)s,
                    %(lottery_plan_a)s, %(lottery_plan_b)s, %(lottery_plan_c)s,
                    %(lottery_cost_current_a)s, %(lottery_cost_current_b)s, %(lottery_cost_current_c)s,
                    %(lottery_cost_total_a)s, %(lottery_cost_total_b)s, %(lottery_cost_total_c)s,
                    %(lottery_profit_a)s, %(lottery_profit_b)s, %(lottery_profit_c)s,
                    %(lottery_status)s, %(draw_date)s, %(create_date)s)
                """
                cursor.execute(sql, item)
            else:   # 记录存在
                if 0 == result[2]:  # 待开
                    sql = """
                        update sc_lottery_buy_plan 
                        set lottery_full_no=%(lottery_full_no)s, lottery_status=%(lottery_status)s
                        where lottery_code=%(lottery_code)s and lottery_num=%(lottery_num)s
                    """
                    cursor.execute(sql, item)
        except Exception as e:
            raise e
        else:
            conn.commit()
            # print(item)
        finally:
            cursor.close()
            conn.close()


class KillNoPlanPipeline:   # 309
    def process_item(self, item, spider):
        conn = pymysql.connect(**settings['MYSQL_POOL_CONFIG'])
        cursor = conn.cursor()
        try:
            cursor.execute("""
            select lottery_code, lottery_num, lottery_status from sc_lottery_kill_plan 
            where lottery_num=%(lottery_num)s and lottery_code=%(lottery_code)s
            """, {'lottery_num': item['lottery_num'], 'lottery_code': item['lottery_code']})
            result = cursor.fetchone()
            if not result:
                sql = """
                    insert into sc_lottery_kill_plan(id, lottery_code, lottery_num, lottery_full_no,
                    reserved_bit_one, reserved_bit_two, reserved_bit_three, reserved_bit_four, reserved_bit_five,
                    reserved_bit_six, reserved_bit_seven, reserved_bit_eight, reserved_bit_nine, reserved_bit_ten,
                    lottery_status, draw_date, create_date)
                    values (%(id)s, %(lottery_code)s, %(lottery_num)s, %(lottery_full_no)s,
                    %(reserved_bit_one)s, %(reserved_bit_two)s, %(reserved_bit_three)s, %(reserved_bit_four)s, %(reserved_bit_five)s,
                    %(reserved_bit_six)s, %(reserved_bit_seven)s, %(reserved_bit_eight)s, %(reserved_bit_nine)s, %(reserved_bit_ten)s,
                    %(lottery_status)s, %(draw_date)s, %(create_date)s)
                """
                cursor.execute(sql, item)
            else:
                if 0 == result[2]:
                    sql = """
                        update sc_lottery_kill_plan
                        set lottery_full_no=%(lottery_full_no)s, lottery_status=%(lottery_status)s,
                        reserved_bit_one=%(reserved_bit_one)s, reserved_bit_two=%(reserved_bit_two)s,
                        reserved_bit_three=%(reserved_bit_three)s, reserved_bit_four=%(reserved_bit_four)s,
                        reserved_bit_five=%(reserved_bit_five)s, reserved_bit_six=%(reserved_bit_six)s,
                        reserved_bit_seven=%(reserved_bit_seven)s, reserved_bit_eight=%(reserved_bit_eight)s,
                        reserved_bit_nine=%(reserved_bit_nine)s, reserved_bit_ten=%(reserved_bit_ten)s
                        where lottery_code=%(lottery_code)s and lottery_num=%(lottery_num)s
                    """
                    cursor.execute(sql, item)
        except Exception as e:
            raise e
        else:
            conn.commit()
            # print(item)
        finally:
            cursor.close()
            conn.close()


class BeijingHappy8Pipeline:    # 310
    def process_item(self, item, spider):
        conn = pymysql.connect(**settings['MYSQL_POOL_CONFIG'])
        cursor = conn.cursor()
        try:
            cursor.execute(
                """select * from sc_lottery_info where lottery_num=%(lottery_num)s and lottery_code=%(lottery_code)s""",
                {'lottery_num': item['lottery_num'], 'lottery_code': item['lottery_code']})
            result = cursor.fetchone()
            if not result:
                sql = """
                        insert into sc_lottery_info(id, lottery_code, lottery_num, lottery_full_no, 
                        lottery_sum_value, reserved_bit_one, lottery_countdown,
                        draw_date, create_date, update_date)
                        values (%(id)s, %(lottery_code)s, %(lottery_num)s, %(lottery_full_no)s,
                        %(lottery_sum_value)s, %(reserved_bit_one)s, %(lottery_countdown)s,
                        %(draw_date)s, %(create_date)s, %(update_date)s)
                """
                cursor.execute(sql, item)
                conn.commit()
        except Exception as e:
            raise e
        else:
            conn.commit()
            # print(item)
        finally:
            cursor.close()
            conn.close()


class ChongqLuckFarmPipeline:   # 311
    def process_item(self, item, spider):
        conn = pymysql.connect(**settings['MYSQL_POOL_CONFIG'])
        cursor = conn.cursor()
        try:
            if 'lottery_number' == item['parse_type']:  # 开奖号码
                cursor.execute("""
                select * from sc_lottery_info where lottery_num=%(lottery_num)s and lottery_code=%(lottery_code)s
                """, {'lottery_num': item['lottery_num'], 'lottery_code': item['lottery_code']})
                result = cursor.fetchone()
                if not result:
                    sql = """
                        insert into sc_lottery_info(id, lottery_code, lottery_num, lottery_full_no,
                        lottery_sum_value, reserved_bit_one, reserved_bit_two, lottery_countdown, 
                        draw_date, create_date, update_date)
                        values (%(id)s, %(lottery_code)s, %(lottery_num)s, %(lottery_full_no)s,
                        %(lottery_sum_value)s, %(reserved_bit_one)s, %(reserved_bit_two)s, %(lottery_countdown)s, 
                        %(draw_date)s, %(create_date)s, %(update_date)s)
                    """
                    cursor.execute(sql, item)
            elif 'double_statistics' == item['parse_type']:     # 双面统计
                pass
            elif 'trend_by_issue' == item['parse_type']:        # 基本走势
                cursor.execute("""
                    select * from sc_lottery_char where lottery_num=%(lottery_num)s and lottery_code=%(lottery_code)s and lottery_char_type=%(lottery_char_type)s
                """, {'lottery_num': item['lottery_num'], 'lottery_code': item['lottery_code'], 'lottery_char_type': item['lottery_char_type']})
                result = cursor.fetchone()
                if not result:
                    sql = """
                        insert into sc_lottery_char(id, lottery_code, lottery_num, lottery_full_no, lottery_char_type,
                        reserved_bit_one, reserved_bit_two,
                        is_finish, draw_date, create_date, update_date)
                        values (%(id)s, %(lottery_code)s, %(lottery_num)s, %(lottery_full_no)s, %(lottery_char_type)s,
                        %(reserved_bit_one)s, %(reserved_bit_two)s,
                        %(is_finish)s, %(draw_date)s, %(create_date)s, %(update_date)s)
                    """
                    cursor.execute(sql, item)
            elif item['parse_type'] in ['trend_big_small', 'trend_single_double']:       # 大小走势 \ 单双走势
                cursor.execute("""
                    select * from sc_lottery_char where lottery_num=%(lottery_num)s and lottery_code=%(lottery_code)s and lottery_char_type=%(lottery_char_type)s
                """, {'lottery_num': item['lottery_num'], 'lottery_code': item['lottery_code'], 'lottery_char_type': item['lottery_char_type']})
                result = cursor.fetchone()
                if not result:
                    sql = """
                        insert into sc_lottery_char(id, lottery_code, lottery_num, lottery_full_no, lottery_char_type,
                        reserved_bit_one, reserved_bit_two, reserved_bit_three, reserved_bit_four, reserved_bit_five,
                        reserved_bit_six, reserved_bit_seven, reserved_bit_eight, reserved_bit_nine,
                        is_finish, draw_date, create_date, update_date)
                        values (%(id)s, %(lottery_code)s, %(lottery_num)s, %(lottery_full_no)s, %(lottery_char_type)s,
                        %(reserved_bit_one)s, %(reserved_bit_two)s, %(reserved_bit_three)s, %(reserved_bit_four)s, %(reserved_bit_five)s,
                        %(reserved_bit_six)s, %(reserved_bit_seven)s, %(reserved_bit_eight)s, %(reserved_bit_nine)s,
                        %(is_finish)s, %(draw_date)s, %(create_date)s, %(update_date)s)
                    """
                    cursor.execute(sql, item)
        except Exception as e:
            raise e
        else:
            conn.commit()
            # print(item)
        finally:
            cursor.close()
            conn.close()


class Com1680380SscPipeline:        # 312
    def process_item(self, item, spider):
        conn = pymysql.connect(**settings['MYSQL_POOL_CONFIG'])
        cursor = conn.cursor()
        try:
            if 'lottery_number' == item['parse_type']:
                cursor.execute("""
                select * from sc_lottery_info where lottery_num=%(lottery_num)s and lottery_code=%(lottery_code)s
                """, {'lottery_num': item['lottery_num'], 'lottery_code': item['lottery_code']})
                result = cursor.fetchone()
                if not result:
                    sql = """
                        insert into sc_lottery_info(id, lottery_code, lottery_num, lottery_full_no, lottery_sum_value, 
                        reserved_bit_one, reserved_bit_two, reserved_bit_three, reserved_bit_four,
                        lottery_countdown, draw_date, create_date, update_date)
                        values (%(id)s, %(lottery_code)s, %(lottery_num)s, %(lottery_full_no)s, %(lottery_sum_value)s, 
                        %(reserved_bit_one)s, %(reserved_bit_two)s, %(reserved_bit_three)s, %(reserved_bit_four)s,
                        %(lottery_countdown)s, %(draw_date)s, %(create_date)s, %(update_date)s)
                    """
                    cursor.execute(sql, item)
            elif 'trend_dtt' == item['parse_type']:
                cursor.execute("""
                    select * from sc_lottery_char where lottery_num=%(lottery_num)s and lottery_code=%(lottery_code)s and lottery_char_type=%(lottery_char_type)s
                """, {'lottery_num': item['lottery_num'], 'lottery_code': item['lottery_code'],
                      'lottery_char_type': item['lottery_char_type']})
                result = cursor.fetchone()
                if not result:
                    sql = """
                        insert into sc_lottery_char(id, lottery_code, lottery_num, lottery_full_no, lottery_char_type,
                        reserved_bit_one, reserved_bit_two, reserved_bit_three,
                        is_finish, draw_date, create_date, update_date)
                        values (%(id)s, %(lottery_code)s, %(lottery_num)s, %(lottery_full_no)s, %(lottery_char_type)s,
                        %(reserved_bit_one)s, %(reserved_bit_two)s, %(reserved_bit_three)s,
                        %(is_finish)s, %(draw_date)s, %(create_date)s, %(update_date)s)
                    """
                    cursor.execute(sql, item)
            elif 'trend_by_issue' == item['parse_type']:
                cursor.execute("""
                    select * from sc_lottery_char where lottery_num=%(lottery_num)s and lottery_code=%(lottery_code)s and lottery_char_type=%(lottery_char_type)s
                """, {'lottery_num': item['lottery_num'], 'lottery_code': item['lottery_code'],
                      'lottery_char_type': item['lottery_char_type']})
                result = cursor.fetchone()
                if not result:
                    sql = """
                        insert into sc_lottery_char(id, lottery_code, lottery_num, lottery_full_no, lottery_char_type,
                        reserved_bit_one, reserved_bit_two, reserved_bit_three, reserved_bit_four, reserved_bit_five,
                        is_finish, draw_date, create_date, update_date)
                        values (%(id)s, %(lottery_code)s, %(lottery_num)s, %(lottery_full_no)s, %(lottery_char_type)s,
                        %(reserved_bit_one)s, %(reserved_bit_two)s, %(reserved_bit_three)s, %(reserved_bit_four)s, %(reserved_bit_five)s,
                        %(is_finish)s, %(draw_date)s, %(create_date)s, %(update_date)s)
                    """
                    cursor.execute(sql, item)
        except Exception as e:
            raise e
        else:
            conn.commit()
            # print(item)
        finally:
            cursor.close()
            conn.close()


