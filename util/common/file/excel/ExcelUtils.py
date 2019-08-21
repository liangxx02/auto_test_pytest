# -*- coding:utf-8 -*-
import xlrd


def load_excel(file_path='./test.xlsx', sheet_index=0):
    """
    读取excel文件，并添加至json对象中
    :param sheet_index:
    :param file_path:
    :return:
    """
    if file_path:
        excel_data = []
        workbook = xlrd.open_workbook(file_path)
        # 这里设置读取excel中的第几个sheet
        table = workbook.sheets()[sheet_index]
        for row in range(table.nrows):
            excel_data.append(table.row_values(row))
        return excel_data
    else:
        print('file path is empty , please check it')


def get_all_data(excel_data, filter_str='N'):
    """
    获取excel头和除了第一行之外的所有数据(过滤条件可生效)
    :param filter_str: 过滤的字符，例 N Y
    :param excel_data:
    :return:
    """
    data_keys = []
    data_rows = []

    i = 0
    # 这里的data是一个数组，是excel中的某一行的所有列的数据，
    # 如 ['A', 'B', 'C', 'D', '是否可用'] [1.0, 2.0, 3.0, 4.0, 'N'] [2.0, 3.0, 4.0, 5.0, 'Y']
    for data in excel_data:
        if i == 0:
            # 第一行直接添加到keys里
            data_keys.append(data)
        else:
            # 第二行，如果有过滤条件走过滤条件，如果没有就直接返回全部
            if filter_str:
                # 获取最后一个元素内容 Y N
                last_column_val = data[len(data) - 1]
                if last_column_val != filter_str:
                    data_rows.append(data)
            else:
                data_rows.append(data)
        i += 1
    return data_keys, data_rows


def get_filter_data(file_path, filter_str='N', sheet_index=0):
    """
    通过过滤条件，获取excel中有用的数据
    :param sheet_index: 默认使用第一个sheet
    :param file_path: excel文件路径
    :param filter_str: 过滤字符 默认N
    :return:
    """
    excel_data = load_excel(file_path, sheet_index)
    data_keys, data_rows = get_all_data(excel_data, filter_str)
    return data_keys, data_rows


def get_tailor_data(data, tailor_start=0, tailor_end=0):
    """
    获取剪裁过的数据，
    例如
    ['A', 'B', 'C', 'D', '是否可用'] [1.0, 2.0, 3.0, 4.0, 'N'] [2.0, 3.0, 4.0, 5.0, 'Y']
    剪裁成 0, -1
    如 ['A', 'B', 'C', 'D'] [1.0, 2.0, 3.0, 4.0] [2.0, 3.0, 4.0, 5.0]
    剪裁成 0, -2
    如 ['A', 'B', 'C'] [1.0, 2.0, 3.0] [2.0, 3.0, 4.0]
    剪裁成 1, -2
    如 ['B', 'C'] [2.0, 3.0] [3.0, 4.0]

    :param tailor_end: 开始
    :param tailor_start: 结束
    :param data:
    :return:
    """
    data_tailor = []
    for item in data:
        item_tmp = item[tailor_start:tailor_end]
        data_tailor.append(item_tmp)
    return data_tailor


def test_load_excel():
    """
    测试读取excel方法
    :return:
    """
    file_path = '/Users/yandongjun/Documents/workspace/private/auto_test_pytest/test/test_files/test.xlsx'
    excel_data = load_excel(file_path=file_path)
    # \n 表示换行
    print('\ntest_load_excel get excel data is ', excel_data)


def test_filter_data():
    """
    测试过滤数据
    :return:
    """
    file_path = '/Users/yandongjun/Documents/workspace/private/auto_test_pytest/test/test_files/test.xlsx'
    data_keys, data_rows = get_filter_data(file_path=file_path)
    print('\ndata_keys is ', data_keys)
    print('\ndata_rows is ', data_rows)


def test_tailor_data():
    """
    测试剪裁数组
    :return:
    """
    file_path = '/Users/yandongjun/Documents/workspace/private/auto_test_pytest/test/test_files/test.xlsx'
    data_keys, data_rows = get_filter_data(file_path=file_path)
    data_keys_tailor1 = get_tailor_data(data_rows, 0, -1)
    print('data_keys_tailor1 is ', data_keys_tailor1)
    data_keys_tailor2 = get_tailor_data(data_rows, 0, -2)
    print('data_keys_tailor2 is ', data_keys_tailor2)
    data_keys_tailor3 = get_tailor_data(data_rows, 1, -1)
    print('data_keys_tailor3 is ', data_keys_tailor3)
    data_keys_tailor4 = get_tailor_data(data_rows, 1, -2)
    print('data_keys_tailor4 is ', data_keys_tailor4)
