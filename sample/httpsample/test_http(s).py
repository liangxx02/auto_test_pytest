# -*- coding:utf-8 -*-
# Power by godaipl 2018-11-26 17:28:15

import requests


def test_http_get():
    """
    测试http get请求
    """
    headers = {}
    headers['Auth'] = 'aaaaaaaaa'  # 测试用

    params = {}
    params['name'] = 'godaipl'  # 测试用参数

    # params就是普通的url后加参数的方式
    r = requests.get(
        url='http://www.baidu.com', params=params, headers=headers)
    print('r\'s status code is ', r.status_code)
    print('r\'s text is ', r.text)
    print('r\'s json is ', r.json)


def test_http_post():
    """
    测试http post请求
    """
    headers = {}
    headers['Auth'] = 'aaaaaaaaa'  # 测试用

    params = {}
    params['name'] = 'godaipl'  # 测试用参数

    # params就是普通的url后加参数的方式
    # r = requests.post(
    # url='http://www.baidu.com', params=params, headers=headers)

    r = requests.post(
        url='http://www.baidu.com', json=params, headers=headers)
    print('r\'s status code is ', r.status_code)
    print('r\'s text is ', r.text)
    print('r\'s json is ', r.json)

# https的省略


if __name__ == "__main__":
    pass
