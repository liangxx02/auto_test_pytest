host = '183.129.150.2'

port = '8777'


class BitanUris:
    URL_PREFIX = 'http://' + host + ':' + port

    # 少一个斜杠，我加过了
    # 用户
    API_USER_LOGOUT = URL_PREFIX + '/oauth/oauth-rest/logout'
    # 帖子
    API_POST_ADD = URL_PREFIX + '/knowledge/posts/add'
