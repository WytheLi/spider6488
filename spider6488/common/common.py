import datetime


def lh(draw_code):
    """
    计算龙虎
    :param draw_code: 开奖号列表
    :return:
    """
    temp = []
    for i in range(5):
        x = draw_code[:5]
        y = draw_code[5:][::-1]
        temp.append('1' if x[i] > y[i] else '2')
    return '-'.join(temp)


def gyh(sum_value):
    """
    计算冠亚和
    :param sum_value: 开奖号前两位之和
    :return: <一球二球之和>-<大a小b>-<单c双d>
    """
    res = str(sum_value) + "-" + ('a' if sum_value >= 11 else 'b') + '-' + ('c' if sum_value % 2 != 0 else 'd')
    return res


def released_date(lottery_num, draw_date):
    """
    幸运飞艇
    https://luck-airship.com/history.aspx
    根据开奖号，计算对应开奖时间
    :param lottery_num:
    :param draw_date:
    :return:
    """
    end_no = int(lottery_num[-3:])
    start_time = draw_date + " " + '06:09:00'
    current_time_obj = datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S') + datetime.timedelta(minutes=(end_no-1)*5)
    return datetime.datetime.strftime(current_time_obj, '%Y-%m-%d %H:%M:%S')


def sum_value_11x5(sum_num, sum_single_double, sum_big_small):
    """
    11选5 和值数据
    :param sum_num:
    :param sum_single_double: 0单1双
    :param sum_big_small: 0大1小2和
    :return: <sum_num>-<a大b小e和>-<c单d双>
    """
    assert sum_big_small in [0, 1, 2]
    assert sum_single_double in [0, 1]

    if 0 == sum_big_small:
        sum_big_small = 'a'
    elif 1 == sum_big_small:
        sum_big_small = 'b'
    else:
        sum_big_small = 'e'
    res = str(sum_num) + '-' + sum_big_small + '-' + ('c' if 0 == sum_single_double else 'd')
    return res


def sum_value_kl8(sum_num, sum_single_double, sum_big_small):
    """
    和值 北京快乐8
    :param sum_num:
    :param sum_single_double: -1双1单
    :param sum_big_small: -1小1大
    :return:
    """
    # print(sum_big_small)
    # print(sum_single_double)
    if 1 == sum_big_small:
        sum_big_small = 'a'
    elif -1 == sum_big_small:
        sum_big_small = 'b'
    else:
        sum_big_small = 'e'

    if sum_single_double in [-1, 0]:  # -1小，0和（810）
        sum_single_double = 'd'
    else:
        sum_single_double = 'c'
    res = str(sum_num) + '-' + sum_big_small + '-' + sum_single_double
    return res


def sum_five_elements(single_double_count, front_behind_count, sum_bs_sd, sum_wu_xing):
    """
    五行 其他几项暂略
    :param single_double_count: 0单双和, 1单多, -1双多
    :param front_behind_count: 0前后和, 1前多, -1后多
    :param sum_bs_sd: 1总大单, 2总大双, 3总小单, 4总小双, 5总和
    :param sum_wu_xing: 1'金', 2'木', 3'水', 4'火', 5'土'
    :return:
    """
    pass


def sum_value_k3(sum_num, sum_single_double, sum_big_small):
    """
    快3 和值数据
    :param sum_num:
    :param sum_single_double: 0单1双2通吃
    :param sum_big_small: 0大1小2通吃
    :return: <sum_num>-<a大b小f通吃>-<c单d双f通吃>
    """
    # 此处省略断言参数
    if 0 == sum_big_small:
        sum_big_small = 'a'
    elif 1 == sum_big_small:
        sum_big_small = 'b'
    else:
        sum_big_small = 'f'

    if 0 == sum_single_double:
        sum_single_double = 'c'
    elif 1 == sum_single_double:
        sum_single_double = 'd'
    else:
        sum_single_double = 'f'
    res = str(sum_num) + '-' + sum_big_small + '-' + sum_single_double
    # print(res)
    return res


def sum_value_pc_balls(sum_num, sum_single_double, sum_big_small):
    """
    总和
    pc蛋蛋
    :param sum_num:
    :param sum_single_double: -1双1单
    :param sum_big_small: -1小1大
    :return:
    """
    if 1 == sum_big_small:
        sum_big_small = 'a'
    elif -1 == sum_big_small:
        sum_big_small = 'b'

    if 1 == sum_single_double:
        sum_single_double = 'c'
    elif -1 == sum_single_double:
        sum_single_double = 'd'
    res = str(sum_num) + '-' + sum_big_small + '-' + sum_single_double
    return res


def sum_value_canada28(sum_num, sum_single_double, sum_big_small):
    """
    总和
    加拿大28
    :param sum_num:
    :param sum_single_double: 1单2双
    :param sum_big_small: 1大2小
    :return:
    """
    if 1 == sum_big_small:
        sum_big_small = 'a'
    elif 2 == sum_big_small:
        sum_big_small = 'b'

    if 1 == sum_single_double:
        sum_single_double = 'c'
    elif 2 == sum_single_double:
        sum_single_double = 'd'
    res = str(sum_num) + '-' + sum_big_small + '-' + sum_single_double
    return res


def tag_lot_no_tq_k3(draw_code, code, sequence):
    """
    某位开奖号的定位走势数据
    :param draw_code:
    :param code:
    :param sequence: 第几位号码走势 1、2、3
    :return: bedeck_code
    """
    bedeck_code = []
    # a大b小c单d双
    tag_lot_code = draw_code[sequence-1]
    lot_code_big_small = 'b' if tag_lot_code in [1, 2, 3] else 'a'  # 1,2,3小 4,5,6大
    lot_code_single_double = 'c' if tag_lot_code in [1, 3, 5] else 'd'
    for index, value in enumerate(code):
        if 6 == index and 'a' == lot_code_big_small:
            value = lot_code_big_small
        elif 7 == index and 'b' == lot_code_big_small:
            value = lot_code_big_small
        elif 8 == index and 'c' == lot_code_single_double:
            value = lot_code_single_double
        elif 9 == index and 'd' == lot_code_single_double:
            value = lot_code_single_double
        bedeck_code.append(str(value))
    bedeck_code = ','.join(bedeck_code).replace('-', '').replace(',', '-')
    return bedeck_code


def tag_lot_no_big_and_small_k3(draw_code, code, sequence):
    """
    某位开奖号的大小
    :param draw_code:
    :param code:
    :param sequence:
    :return:
    """
    bedeck_code = []
    tag_lot_code = draw_code[sequence - 1]
    lot_code_big_small = 'b' if tag_lot_code in [1, 2, 3] else 'a'
    for i in code:
        if 'a' == lot_code_big_small:
            bedeck_code.append(lot_code_big_small)
            bedeck_code.append(str(i))
        elif 'b' == lot_code_big_small:
            bedeck_code.append(str(i))
            bedeck_code.append(lot_code_big_small)
        break
    return ','.join(bedeck_code).replace('-', '').replace(',', '-')


def big_small_trend_k3(size_compare):
    """
    大小比走势
    :param size_compare:
    :return:
    """
    ratio_map = ['3:0', '2:1', '1:2', '0:3']
    res = ','.join([ratio_map[index] if value > 0 else str(value) for index, value in enumerate(size_compare)]).replace('-', '').replace(',', '-')
    return res


def sum_value_form_k3(sum_total, form_no):
    """
    和值形态
    :param sum_total:
    :param form_no:
    :return:
    """
    if sum_total >= 11:
        form_no[0] = 'a'
    elif sum_total < 11:
        form_no[1] = 'b'

    if sum_total % 2 != 0:
        form_no[2] = 'c'
    elif sum_total % 2 == 0:
        form_no[3] = 'd'
    res = ','.join([str(val) for val in form_no]).replace('-', '').replace(',', '-')
    return res


def num_form_k3(draw_code, number_form):
    """
    号码形态     a豹子b三不同c对子
    :param draw_code:
    :param number_form:
    :return:
    """
    if 1 == len(set(draw_code)):
        number_form[0] = 'a'
    elif 2 == len(set(draw_code)):
        number_form[2] = 'c'
    elif 3 == len(set(draw_code)):
        number_form[1] = 'b'
    res = ','.join([str(val) for val in number_form]).replace('-', '').replace(',', '-')
    return res


def odd_even_k3(tag_code, num_form):
    """
    计算指定位置彩票号码的奇偶
    :param tag_code: 指定位置的彩票号码
    :param num_form:
    :return:
    """
    temp = ['c', 'd']   # c奇d偶
    if tag_code % 2 == 0:
        temp[0] = str(abs(num_form))
    else:
        temp[1] = str(abs(num_form))
    return '-'.join(temp)


def odd_even_compare_k3(odd_even_compare):
    """
    奇偶比
    :param odd_even_compare:
    :return:
    """
    compare_val_map = ['3:0', '2:1', '1:2', '0:3']
    for index, value in enumerate(odd_even_compare):
        if value > 0:
            odd_even_compare[index] = compare_val_map[index]
    res = ','.join([str(i) for i in odd_even_compare]).replace('-', '').replace(',', '-')
    return res


def three_terms_11x5(num):
    """
    前三，中三，后三    的计算
    :param num: 0杂六1半顺2顺子
    :return: 1半顺2顺子5杂六
    """
    if 0 == num:
        return '5'
    elif 1 == num:
        return '1'
    elif 2 == num:
        return '2'


def three_terms_ssc(num):
    """
    三项
    0杂六1半顺2顺子3对子4豹子 --> 1半顺2顺子3豹子4对子5杂六
    :param num:
    :return:
    """
    assert num in [0, 1, 2, 3, 4]

    if 0 == num:
        return '5'
    elif 1 == num:
        return '1'
    elif 2 == num:
        return '2'
    elif 3 == num:
        return '4'
    elif 4 == num:
        return '3'


def big_small_ssc(big_small_list):
    """
    大小
    :param big_small_list: 0大1小
    :return: a大b小
    """
    res = '-'.join(map(lambda x: 'a' if 0 == x else 'b', big_small_list))
    return res


def single_double_ssc(single_double_list):
    """
    单双
    :param single_double_list: 0单1双
    :return: c单d双
    """
    res = '-'.join(map(lambda x: 'c' if 0 == x else 'd', single_double_list))
    return res


def dragon_tiger_11x5(draw_code, array_last_two):
    """
    开奖号第一个大于第二个则为龙，反之为虎
    :param draw_code:
    :param array_last_two:
    :return:
    """

    lot_no_list = list(map(lambda x: int(x), draw_code.split(',')))
    if lot_no_list[0] > lot_no_list[-1]:
        temp = ['1', str(abs(array_last_two[1]))]
    else:
        temp = [str(abs(array_last_two[0])), '2']
    return '-'.join(temp)


def dragon_tiger_chongq(first_dt, second_dt, third_dt, fourth_dt):
    """
    龙虎数据  重庆幸运农场
    0龙 1虎 -->  1龙2虎
    :param first_dt:
    :param second_dt:
    :param third_dt:
    :param fourth_dt:
    :return:
    """
    temp = []
    temp.append('2') if first_dt else temp.append('1')
    temp.append('2') if second_dt else temp.append('1')
    temp.append('2') if third_dt else temp.append('1')
    temp.append('2') if fourth_dt else temp.append('1')
    res = '-'.join(temp)
    # print(res)
    return res


def dragon_tiger_pk10(first_dt, second_dt, third_dt, fourth_dt, fifth_dt):
    """
    龙虎数据 北京pk10
    :param first_dt:
    :param second_dt:
    :param third_dt:
    :param fourth_dt:
    :param fifth_dt:
    :return:
    """
    temp = []
    temp.append('2') if first_dt else temp.append('1')
    temp.append('2') if second_dt else temp.append('1')
    temp.append('2') if third_dt else temp.append('1')
    temp.append('2') if fourth_dt else temp.append('1')
    temp.append('2') if fifth_dt else temp.append('1')
    res = '-'.join(temp)
    # print(res)
    return res


def big_small_chongq(lot_num, big_small_code):
    """
    大小 重庆幸运农场
    1-10为小 11-20为大
    :param lot_num:
    :param big_small_code:
    :return:
    """
    if lot_num <= 10:
        temp = [str(abs(big_small_code[0])), 'b']
    else:
        temp = ['a', str(abs(big_small_code[1]))]
    res = '-'.join(temp)
    return res


def trend_big_small_chongq(missing):
    """
    大小比走势
    :param missing:
    :return:
    """
    assert isinstance(missing, list)

    temp = ['0:8', '1:7', '2:6', '3:5', '4:4', '5:3', '6:2', '7:1', '8:0']
    for index, value in enumerate(missing):
        if value < 0:
            temp[index] = str(abs(value))
    res = '-'.join(temp)
    return res


def single_double_chongq(lot_num, single_double_list):
    """
    奇偶  c奇d偶
    :param lot_num:
    :param single_double_list:
    :return:
    """
    if lot_num % 2 == 0:
        temp = [str(abs(single_double_list[0])), 'd']
    else:
        temp = ['c', str(abs(single_double_list[1]))]
    res = '-'.join(temp)
    return res


def trend_single_double_chongq(missing):
    """
    奇偶比走势
    :param missing:
    :return:
    """
    assert isinstance(missing, list)

    temp = ['0:8', '1:7', '2:6', '3:5', '4:4', '5:3', '6:2', '7:1', '8:0']
    for index, value in enumerate(missing):
        if value < 0:       # 1, 2
            temp[index] = str(abs(value))
    res = '-'.join(temp)
    return res


def trend_by_issue_total(missing):
    """
    总分 重庆幸运农场
    a大b小 c单d双 e和 a尾大b尾小
    :param missing:
    :return:
    """
    pdhz = ['大', '小', '和']
    ds = ['单', '双']
    w_ds = ['大', '小']
    hz = missing[20]  # 和值
    if hz == 84:  # 和
        pdhz[0] = missing[21]
        pdhz[1] = missing[22]
    elif hz <= 132 and hz >= 85:  # 大
        pdhz[1] = missing[22]
        pdhz[2] = missing[23]
    elif hz <= 83 and hz >= 36:  # 小
        pdhz[0] = missing[21]
        pdhz[2] = missing[23]

    dxh_ = ','.join([str(i) for i in pdhz]).replace('-', '')  # 大小和

    if missing[20] % 2 == 0:
        ds[0] = ''.join(str(missing[24])).replace('-', '')
    else:
        ds[1] = ''.join(str(missing[25])).replace('-', '')
    ds_ds = ','.join(ds)  # 单双

    if int([i for i in str(hz)][1]) >= 5:
        w_ds[1] = missing[27]
    else:
        w_ds[0] = missing[26]
    w = ','.join([str(i) for i in w_ds]).replace('-', '')  # 尾大小
    data_count = str(hz) + ',' + dxh_ + ',' + ds_ds + ',' + w
    # print(data_count)
    data_count = data_count.replace("大", "a").replace("小", "b").replace("单", "c").replace("双", "d").replace("和","e").replace(",", "-"),
    return data_count


def compute_dt_chongq_ssc(draw_code):
    """
    根据彩票号码计算龙虎和
    :param draw_code: for example ["8", "8", "8", "6", "1"]
    :return: 1龙2虎3合
    """
    assert isinstance(draw_code, list)

    if draw_code[0] == draw_code[-1]:
        code = 3
    elif draw_code[0] > draw_code[-1]:
        code = 1
    else:
        code = 2
    return code


def compute_three_terms(three_terms_code):
    """
    根据彩票号码计算三项
    1半顺2顺子3豹子4对子5杂六
    :param three_terms_code: for example ["8", "8", "8"]
    :return: 3
    """
    assert isinstance(three_terms_code, list)
    three_terms_code.sort(reverse=True)     # 将列表倒序
    if 1 == len(set(three_terms_code)):     # 豹子
        res = '3'
    elif 2 == len(set(three_terms_code)):   # 对子
        res = '4'
    elif int(three_terms_code[0]) - int(three_terms_code[1]) == 1 and int(three_terms_code[1]) - int(three_terms_code[2]) == 1:     # 顺子
        res = '2'
    elif int(three_terms_code[0]) - int(three_terms_code[1]) == 1 or int(three_terms_code[1]) - int(three_terms_code[2]) == 1:  # 半顺
        res = '1'
    else:
        res = '5'
    return res


def kill_right_or_wrong(num_enum):
    """
    杀号计划 杀对杀错字符
    :param num_enum:
    :return:
    """
    temp = []
    for i in range(0, len(num_enum), 2):
        temp.append(str(num_enum[i:i+2][0])+'-'+('1' if num_enum[i:i+2][1] == 1 else '2'))
    res = '-'.join(temp)
    # print(res)
    return res


def dragon_tiger_ssc(dragon_tiger):
    """
    龙虎 时时彩
    :param dragon_tiger: 0龙1虎2和
    :return: 1龙2虎3和
    """
    assert dragon_tiger in [0, 1, 2]
    if 0 == dragon_tiger:
        return '1'
    elif 1 == dragon_tiger:
        return '2'
    else:
        return '3'


def dragon_tiger_equal_ssc(draw_code, array_last_two):
    """
    龙虎和
    :param draw_code:
    :param array_last_two:
    :return:
    """
    lot_no_list = list(map(lambda x: int(x), draw_code.split(',')))
    if lot_no_list[0] > lot_no_list[-1]:
        temp = ['1', str(abs(array_last_two[1])), str(abs(array_last_two[2]))]
    elif lot_no_list[0] < lot_no_list[-1]:
        temp = [str(abs(array_last_two[0])), '2', str(abs(array_last_two[2]))]
    else:
        temp = [str(abs(array_last_two[0])), str(abs(array_last_two[1])), '3']
    return '-'.join(temp)


def is_guess(result):
    """
    猜中与否
    :param result: ""、"中"、"错"
    :return: 1待开 2中 3未中
    """
    if result not in ['', '中', '错']:
        raise ValueError
    if not result:
        return '1'
    elif '中' == result:
        return '2'
    else:
        return '3'


def init_trend_lot_full_no_bottom(sequence, tag_lottery_num):
    """
    号码走势 初始化底号
    :param sequence: 第几球
    :param tag_lottery_num: 当前球 球号 例如：05
    :return:
    """
    init_value = [1] * 10
    init_value[int(tag_lottery_num)-1] = int(tag_lottery_num)
    res = '-'.join(map(lambda x: str(x), init_value))
    return res


def compute_trend_lot_full_no_bottom(sequence, tag_lottery_num, prev_bottom_no, prev_lot_full_no):
    """
    号码走势 计算底号
    :param sequence: 第几球 1
    :param tag_lottery_num: 当前球球号 05
    :param prev_bottom_no: 前一期底号 1-18-5-2-22-1-3-10-7-29
    :param prev_lot_full_no: 前一期开奖号
    :return:
    """
    # ['01', '10', '05', '06', '07', '04', '09', '08', '02', '03']
    prev_lot_full_no = prev_lot_full_no.split('-')

    bottom_no = list(map(lambda x: int(x), prev_bottom_no.split('-')))
    # 前一期的开奖号对应的索引位，重新从1计数
    bottom_no[int(prev_lot_full_no[sequence-1]) - 1] = 1

    for index, value in enumerate(bottom_no):
        # 目标球号等于，索引位加一
        if int(tag_lottery_num) == index + 1:
            bottom_no[index] = int(tag_lottery_num)
        else:
            if int(prev_lot_full_no[sequence-1]) - 1 == index:
                continue
            bottom_no[index] += 1
    res = '-'.join(map(lambda x: str(x), bottom_no))
    return res


def init_trend_gysum_bottom(lot_full_no):
    """
    冠亚和 初始化底号
    :param lot_full_no: 开奖号码 ['01', '10', '05', '06', '07', '04', '09', '08', '02', '03']
    :return:
    """
    init_value = [1] * 17
    # 冠亚和 第一 第二球之和
    sum_value = int(lot_full_no[0]) + int(lot_full_no[1])
    for index, value in enumerate(init_value):
        if sum_value-3 == index:
            init_value[index] = sum_value
    res = '-'.join(map(lambda x: str(x), init_value))
    return res


def compute_trend_gysum_bottom(lot_full_no, prev_bottom_no, prev_lot_full_no):
    """
    冠亚和 计算底号
    :param lot_full_no: 开奖号码 ['01', '10', '05', '06', '07', '04', '09', '08', '02', '03']
    :param prev_bottom_no: 上期底号 22-13-67-1-59-1-7-8-3-2-11-9-55-62-4-56-30
    :param prev_lot_full_no: 上期开奖号
    :return:
    """
    # ['01', '10', '05', '06', '07', '04', '09', '08', '02', '03']
    prev_lot_full_no = prev_lot_full_no.split('-')

    bottom_no = list(map(lambda x: int(x), prev_bottom_no.split('-')))
    # 本期和值
    sum_value = int(lot_full_no[0]) + int(lot_full_no[1])
    # 上期和值
    prev_sum_value = int(prev_lot_full_no[0]) + int(prev_lot_full_no[1])
    # 上期和值位置 底号值，重置为1
    bottom_no[prev_sum_value-3] = 1

    for index, value in enumerate(bottom_no):
        if sum_value-3 == index:
            bottom_no[index] = sum_value
        else:
            if prev_sum_value-3 == index:
                continue
            bottom_no[index] += 1
    res = '-'.join(map(lambda x: str(x), bottom_no))
    return res


def init_trend_sum_parse_bottom_bjkl8(lot_full_no):
    """
    和值走势
    :param lot_full_no: ['1', '2', '3']
    :return:
    """
    values = ['1'] * 5
    sum_value = sum(map(lambda x: int(x), lot_full_no))
    # 数据区间01~80
    # 810以上为大  810以下为小  810为和
    if sum_value == 810:
        values[4] = 'e'
    if sum_value > 810:
        values[0] = 'a'
    if sum_value < 810:
        values[1] = 'b'

    if sum_value % 2 != 0:
        values[2] = 'c'
    if sum_value % 2 == 0:
        values[3] = 'd'
    res = '-'.join(values)
    return res


def compute_trend_sum_parse_bottom_bjkl8(lot_full_no, prev_bottom_no):
    """

    :param lot_full_no: 本期开奖数据 ['06', '09', '13', '14', '19', '21', '22', '27', '31', '33', '34', '37', '49', '63', '64', '66', '67', '69', '76', '80', '01']
    :param prev_bottom_no: 上期底号 801-1-b-c-1-1
    :return:
    """
    bottom_no = list(map(lambda x: 0 if x in ['a', 'b', 'c', 'd', 'e'] else int(x), prev_bottom_no.split('-')))
    print(bottom_no)
    sum_value = sum(map(lambda x: int(x), lot_full_no))

    for index, value in enumerate(bottom_no):
        bottom_no[index] += 1

    # 数据区间01~80
    # 810以上为大  810以下为小  810为和
    if sum_value == 810:
        bottom_no[4] = 'e'
    if sum_value > 810:
        bottom_no[0] = 'a'
    if sum_value < 810:
        bottom_no[1] = 'b'

    if sum_value % 2 != 0:
        bottom_no[2] = 'c'
    if sum_value % 2 == 0:
        bottom_no[3] = 'd'
    res = '-'.join(map(lambda x: str(x), bottom_no))
    return res


def init_trend_position_bottom_c28(tag_lottery_num):
    """
    定位走势 初始化 底号
    :param tag_lottery_num:
    :return:
    """
    init_value = [1] * 14
    init_value[int(tag_lottery_num)] = int(tag_lottery_num)
    if int(tag_lottery_num) >= 5:
        init_value[-4] = 'a'
    else:
        init_value[-3] = 'b'

    if int(tag_lottery_num) % 2 != 0:
        init_value[-2] = 'c'
    else:
        init_value[-1] = 'd'
    res = '-'.join(map(lambda x: str(x), init_value))
    return res


def compute_trend_position_bottom_c28(sequence, tag_lottery_num, prev_bottom_no, prev_lot_full_no):
    """
    定位走势计算 加拿大28
    :param sequence: 第几球 1
    :param tag_lottery_num: 当前球球号 5
    :param prev_bottom_no: 前一期底号 1-18-5-2-22-1-3-10-7-29-a-2-c-7
    :param prev_lot_full_no: 前一期开奖号
    :return:
    """
    # 3-3-4 --> ['3', '3', '4']
    prev_lot_full_no = prev_lot_full_no.split('-')

    bottom_no = list(map(lambda x: 0 if x in ['a', 'b', 'c', 'd'] else int(x), prev_bottom_no.split('-')))
    # 前一期的开奖号对应的索引位，重新从1计数
    bottom_no[int(prev_lot_full_no[sequence-1])] = 1
    # # a、b、c、d位更改为0
    # bottom_no[-1] = 0 if bottom_no[-1] == 'd' else None
    # bottom_no[-2] = 0 if bottom_no[-2] == 'c' else None
    # bottom_no[-3] = 0 if bottom_no[-3] == 'b' else None
    # bottom_no[-4] = 0 if bottom_no[-4] == 'a' else None

    for index, value in enumerate(bottom_no):
        # 目标球号等于，索引位
        if int(tag_lottery_num) == index:
            bottom_no[index] = int(tag_lottery_num)
        else:
            if int(prev_lot_full_no[sequence-1]) == index:
                continue
            bottom_no[index] += 1

    # 大小单双
    if int(tag_lottery_num) >= 5:
        bottom_no[-4] = 'a'
    else:
        bottom_no[-3] = 'b'

    if int(tag_lottery_num) % 2 != 0:
        bottom_no[-2] = 'c'
    else:
        bottom_no[-1] = 'd'
    res = '-'.join(map(lambda x: str(x), bottom_no))
    return res


def init_trend_by_issue_bottom(lot_full_no):
    """
    初始化基本走势中的号码分布 广西快乐十分 1~21
    :param lot_full_no:
    :return:
    """
    values = [1] * 21
    for lot_no in lot_full_no:
        values[int(lot_no)-1] = int(lot_no)
    res = '-'.join(map(lambda x: str(x), values))
    return res


def compute_trend_by_issue_bottom(lot_full_no, prev_bottom_no, prev_lot_full_no):
    """

    :param lot_full_no:
    :param prev_bottom_no:
    :param prev_lot_full_no:
    :return:
    """
    lot_full_no = list(map(lambda x: int(x), lot_full_no))
    prev_lot_full_no = list(map(lambda x: int(x), prev_lot_full_no.split('-')))
    bottom_no = list(map(lambda x: int(x), prev_bottom_no.split('-')))
    for index, value in enumerate(bottom_no):
        if value in prev_lot_full_no and index + 1 == value:
            bottom_no[index] = 0
    for index, value in enumerate(bottom_no):
        if index + 1 in lot_full_no:
            bottom_no[index] = index + 1
            continue
        bottom_no[index] += 1
    res = '-'.join(map(lambda x: str(x), bottom_no))
    return res


if __name__ == '__main__':
    res = compute_trend_lot_full_no_bottom(1, '05', '1-18-5-2-22-1-3-10-7-29', ['01', '10', '05', '06', '07', '04', '09', '08', '02', '03'])
    print(res)

    print(init_trend_gysum_bottom(['01', '10', '05', '06', '07', '04', '09', '08', '02', '03']))

    print(compute_trend_gysum_bottom(['01', '10', '05', '06', '07', '04', '09', '08', '02', '03'],
                                     '22-13-67-1-59-1-7-8-3-2-11-9-55-62-4-56-30',
                                     ['01', '10', '05', '06', '07', '04', '09', '08', '02', '03']))



