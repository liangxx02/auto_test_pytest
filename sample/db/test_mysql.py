# -*- coding:utf-8 -*-

"""
此脚本主要介绍mysql工具类的使用方式
1. 创建测试表
"""

# 先初始化数据库
from util.common.db.mysql import MySqlHelper

mysqlFactory = MySqlHelper(user_name='root', password='dashu0701', database='test', host='localhost')


def test_add_single():
    """
    测试单个增
    :return:
    """
    # TODO


def test_add_batch():
    """
    测试批量增
    :return:
    """
    # TODO


def test_delete():
    """
    测试删
    :return:
    """
    # TODO


def test_modify():
    """
    测试改
    :return:
    """
    # TODO


def test_query():
    """
    测试查询
    :return:
    """
    # TODO
