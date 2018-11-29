#!/usr/bin/env python
# -*- coding: utf-8 -*-

from util.common.dubbo.dubboclient import dubbo


global uid_dubbo_service_conn


# 这里用到了fixture的知识，不懂？去看一下那部分的说明
def setup_module(module):
    """
    模块初始化，初始化dubbo客户端
    :param module:
    :return:
    """
    uid_dubbo_service_ip = '192.168.5.104'
    uid_dubbo_service_port = '20100'
    # 全局变量，用于后面测试用例使用
    global uid_dubbo_service_conn
    uid_dubbo_service_conn = \
        dubbo(uid_dubbo_service_ip, uid_dubbo_service_port)
    # 设定连接超时时间
    uid_dubbo_service_conn.set_connect_timeout(10)  # 单位秒
    # 设定响应的编码
    uid_dubbo_service_conn.set_encoding('gbk')


def test_do_get_uid():
    # 定义dubbo接口叫什么
    interface = 'com.treefinance.commonservice.uid.UidService'
    # 定义接口里的方法叫什么
    method = 'getId'
    # 如果没有参数就写空字符串
    param = ''

    cmd = "%s %s.%s(%s)" % ('invoke', interface, method, param)
    print('result', uid_dubbo_service_conn.do(cmd))


def test_invoke_get_uid():
    """
    测试invoke方法
    """
    # 定义dubbo接口叫什么
    interface = 'com.treefinance.commonservice.uid.UidService'
    # 定义接口里的方法叫什么
    method = 'getId'
    # 如果没有参数就写空字符串
    param = ''
    print('result', uid_dubbo_service_conn.invoke(interface, method, param))


def teardown_module(module):
    """
    这个模块的测试用例跑完之后，用这个方法把连接关掉
    """


if __name__ == "__main__":
    pass
