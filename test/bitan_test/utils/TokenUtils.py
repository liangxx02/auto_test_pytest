# -*- coding:utf-8 -*-

import requests

# 定义头信息
headers = {'Accept': 'application/json',
           'Content-Type': 'application/json',
           'applicationId': '2',
           'applicationClientType': '2',
           'deviceUUID': '2',
           'userFrom': 'pc',
           }


def init_captcha():
    # 定义参数
    params = {'account': '18268040361',
              'countryCode': '+86',
              'sendType': '1',
              'messageType': '2',
              }

    url = "http://183.129.150.2:8777/oauth/oauth-rest/send-captcha"
    r = requests.get(url, params, headers=headers)
    if r.status_code == 200:
        res_json = r.json()
        code = res_json['code']

        if code == 0:
            print('init code success')
        else:
            raise Exception('auth code retcode error')
    else:
        raise Exception('get auth code error')


def init_token():
    """
    init token
    :return:
    """
    # 定义参数
    params = {'mobile': '18268040361',
              'captcha': '123456',
              'countryCode': '+86',
              'inviterCode': '',
              }

    url = "http://183.129.150.2:8777/oauth/oauth-rest/login-no-password"
    result = requests.post(url, headers=headers, json=params)
    print(headers)
    print(params)
    print(result)
    if result.status_code == 200:
        res_json = result.json()
        print('res_json is', res_json)
        code = res_json['code']
        print('code is', code)
        if code == 0:
            token = res_json['data']['token']
            print('token is', token)
            return token
        else:
            raise Exception('get token code error')
    else:
        raise Exception('get token status code error')



def init_params():
    """
    init params
    :return:
    """
    params = {}

    # init auth code
    init_captcha()

    # init token
    token = init_token()

    params['token'] = token

    return params
