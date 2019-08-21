# -*- coding:utf-8 -*-

"""
该脚本旨在学习使用excel读取和数据过滤
1. excel读取(xlsx)
2. 数据过滤(最终生成json)
"""
from util.common.file.excel.ExcelUtils import get_filter_data


def test_filter_data():
    file_path = '/Users/yandongjun/Documents/workspace/private/auto_test_pytest/test/test_files/test.xlsx'
    data_keys, data_rows = get_filter_data(file_path=file_path)
    print('\ndata_keys is ', data_keys)
    print('\ndata_rows is ', data_rows)
