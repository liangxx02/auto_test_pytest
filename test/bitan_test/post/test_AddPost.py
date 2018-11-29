# -*- coding:utf-8 -*-


import requests
# import test.utils

# from test.constants import constants


# 定义初始化方法，获取token
# from constants import constants
# from utils import TokenUtils
from test.bitan_test.constants import constants
from test.bitan_test.utils import TokenUtils


def setup_module():
    """
    这个文件的初始化方法
    :return:
    """
    global token
    params = TokenUtils.init_params()
    token = params['token']

    if token:
        print('init ok')
    else:
        raise Exception('init error')


def teardown_module():
    """
    所有方法跑完了会跑这个方法
    :return:
    """
    # 在这里可以写一些退出操作
    headers = TokenUtils.headers
    # 定义头信息
    headers['lang'] = 'cn'
    headers['buildVersion'] = '60'
    headers['token'] = token
    result = requests.get(constants.BitanUris.API_USER_LOGOUT, headers=headers)
    print(result)


def test_add_post():
    """
    发没有图片的帖子
    :return:
    """
    headers = TokenUtils.headers
    # 定义头信息
    headers['lang'] = 'cn'
    headers['buildVersion'] = '60'
    headers['token'] = token
    # 定义参数
    params = {'content': '12',
              'lang': 'cn',
              'status': '2',
              'type': '1',
              'userId': '62',
              }

    result = requests.post(constants.BitanUris.API_POST_ADD, headers=headers, json=params)
    print(headers)
    print(params)
    print(result)
    if result.status_code == 200:
        res_json = result.json()
        print('res_json is', res_json)
        code = res_json['code']
        print('code is', code)
        if code == 0:
            print("发帖成功")
        else:
            raise Exception('发帖失败', res_json['code'], 'resultMsg is ',
                            res_json['resultMsg'])
    else:
        raise Exception('返回异常')


def test_add_image_post():
    """
    发有图片的帖子
    :return:
    """
    headers = TokenUtils.headers
    # 定义头信息
    headers['lang'] = 'cn'
    headers['buildVersion'] = '60'
    headers['token'] = token
    # 定义参数
    params = {'content': '12',
              'lang': 'cn',
              'images': '',
              'status': '2',
              'type': '1',
              'userId': '62',
              }

    result = requests.post(constants.BitanUris.API_POST_ADD, headers=headers, json=params)
    print(headers)
    print(params)
    print(result)
    if result.status_code == 200:
        res_json = result.json()
        print('res_json is', res_json)
        code = res_json['code']
        print('code is', code)
        if code == 0:
            print("发帖成功")
        else:
            raise Exception('发帖失败', res_json['code'], 'resultMsg is ',
                            res_json['resultMsg'])
    else:
        raise Exception('返回异常')


def test_add_post5():
    """
    每日发帖超5次
    :return:
    """
    headers = TokenUtils.headers
    # 定义头信息
    headers = TokenUtils.headers
    headers['lang'] = 'cn'
    headers['buildVersion'] = '60'
    headers['token'] = token
    # 定义参数
    params = {'content': '12',
              'lang': 'cn',
              'status': '2',
              'type': '1',
              'userId': '62',
              }

    result = requests.post(constants.BitanUris.API_POST_ADD, headers=headers, json=params)
    print(headers)
    print(params)
    print(result)
    if result.status_code == 200:
        res_json = result.json()
        print('res_json is', res_json)
        code = res_json['code']
        print('code is', code)
        if code == 0:
            print("每天最多可以发帖5篇")
        else:
            raise Exception('发帖失败', res_json['code'], 'resultMsg is ',
                            res_json['resultMsg'])
    else:
        raise Exception('返回异常')

