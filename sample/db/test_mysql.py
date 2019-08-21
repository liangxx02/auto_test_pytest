# -*- coding:utf-8 -*-

"""
此脚本主要介绍mysql工具类的使用方式
1. 创建测试表
create table pytest_user_info
(
    id         int auto_increment primary key ,
    user_name  varchar(32)                         not null,
    age        int       default 0                 null,
    address    varchar(64)                         null,
    created_at timestamp default current_timestamp,
    updated_at timestamp default current_timestamp on update current_timestamp
)
    comment '测试用用户信息表';

create unique index pytest_user_info_id_uindex
    on pytest_user_info (id);

create unique index pytest_user_info_user_name_uindex
    on pytest_user_info (user_name);

2. 使用方法测试
"""

# 先初始化数据库

# 这是数据库连接池写法
from util.common.db.mysql.MySqlHelper import MysqlHelper, get_single_insert_sql, get_multi_insert_sql

mysql = MysqlHelper(user_name='root', password='dashu0701', database='pytest_test', host='192.168.5.241')


def test_add_single():
    """
        测试单个增
        :return:
        """
    table_name = 'pytest_user_info'
    table_columns = ['user_name', 'age', 'address']
    value = ('1', 2, 'Hangzhou')
    sql_insert = get_single_insert_sql(table_name, table_columns)
    # 这里调用的是insert
    mysql.insert(sql_insert, value)


def test_add_batch():
    """
    测试批量增
    :return:
    """
    table_name = 'pytest_user_info'
    table_columns = ['user_name', 'age', 'address']
    values = [('1', 2, 'Hangzhou'), ('2', 3, 'Xiamen')]
    sql_insert = get_multi_insert_sql(table_name, table_columns)
    # 这里调用的是insert_batch,
    mysql.insert_batch(sql_insert, values)


def test_delete():
    """
    测试删
    :return:
    """
    sql = 'delete from pytest_user_info where id = %d' % 1
    result = mysql.delete(sql)
    # result = mysql.execute(sql)
    print('删除条数', result)


def test_modify():
    """
    测试改
    :return:
    """
    sql = 'update pytest_user_info set age = 19 where id = 5'
    result = mysql.update(sql)
    print('修改条数', result)


def test_query():
    """
    测试查询
    :return:
    """
    sql = 'select * from pytest_user_info where id = 5'
    result = mysql.query(sql)
    print(result)
