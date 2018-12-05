import requests

# 定义头信息
headers = {'Accept': 'application/json',
           'Content-Type': 'application/json',
           'applicationId': '2',
           'applicationClientType': '2',
           'deviceUUID': '2',
           'userFrom': 'pc',
           }


def init():
    # 定义参数
    params = {'': '',
              '': '+86',
              'sendType': '1',
              'messageType': '2',
              }

    url = "http://183.129.150.2:8777/oauth/oauth-rest/send-captcha"
    r = requests.get(url, params, headers=headers)
    print(headers)
    print(r)
    if r.status_code == 200:
        res_json = r.json()
        code = res_json['code']
        if code == 0:
            print('init code success')
        else:
            raise Exception('auth code retcode error')
    else:
        raise Exception('get auth code error')
