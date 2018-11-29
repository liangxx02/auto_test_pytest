#!/usr/bin/env python
# -*- coding: utf-8 -*-

from util.common.dubbo.dubboclient import dubbo

import json

global authority_dubbo_service_conn


# 这里用到了fixture的知识，不懂？去看一下那部分的说明
def setup_module(module):
    """
    模块初始化，初始化dubbo客户端
    :param module:
    :return:
    """
    authority_dubbo_service_ip = '192.168.5.109'
    authority_dubbo_service_port = '20880'
    # 全局变量，用于后面测试用例使用
    global authority_dubbo_service_conn
    authority_dubbo_service_conn = \
        dubbo(authority_dubbo_service_ip, authority_dubbo_service_port)
    # 设定连接超时时间
    # authority_dubbo_service_conn.set_connect_timeout(10)  # 单位秒
    # 设定响应的编码
    # authority_dubbo_service_conn.set_encoding('gbk')


def test_invoke_ls():
    """
    测试invoke方法 参数是普通的类型
    """
    res_data = authority_dubbo_service_conn.do(
        'ls com.treefinance.loan.authority.facade.service.ResourceService')
    print('res_data is ', res_data)

    res_data_ls = authority_dubbo_service_conn.do('ls')
    print('res_data_ls is ', res_data_ls)


def test_invoke_with_param():
    """
    测试invoke方法
    """
    # 定义dubbo接口叫什么
    interface = 'com.treefinance.loan.authority.facade.service.ResourceService'
    # 定义接口里的方法叫什么
    method = 'getResourceIds'
    # 如果有1个参数这样写
    param = '1111111111111'
    res_data = authority_dubbo_service_conn.invoke(interface, method, param)
    print('res_data is ', res_data)


def test_invoke_with_params():
    """
    测试invoke方法， 参数是普通的类型
    """
    # 定义dubbo接口叫什么
    interface = 'com.treefinance.loan.authority.facade.service.ResourceService'
    # 定义接口里的方法叫什么
    method = 'getResourceNonPermissionList'
    # 如果有多个参数这样写
    # Map < String, List < PermissionVO >>
    # getResourceNonPermissionList(Long userId, Long companyId);
    param = '1111111111111, 2'

    res_data = authority_dubbo_service_conn.invoke(interface, method, param)
    print('res_data is ', res_data)


def test_invoke_with_object():
    """
    测试invoke方法 参数是对象
    """
    # 定义dubbo接口叫什么
    interface = 'com.treefinance.loan.authority.busniess.'
    + 'facade.b2bservice.CreateOperatorService'
    # 定义接口里的方法叫什么
    method = 'createOperator'
    # 如果有多个参数这样写
    # OperatorDTO createOperator(OperatorDTO operatorDTO);
    operatorDTO = {}
    operatorDTO['userName'] = 'yandongjun'
    operatorDTO['email'] = 'yandongjun@treefinance.com.cn'
    operatorDTO['authCode'] = 'SECRETCODE1231231231231'
    operatorDTO['companyName'] = '波波company'
    operatorDTO['companyId'] = '2'
    operatorDTO['employeeNo'] = 'NO1231312312'

    # 转成字符串，如果有多个对象，就像普通对象一样，添加多个，比如
    # json.dumps(operatorDTO) + ',' +
    # json.dumps(operatorDTO2) + ',12121212121212'
    param = json.dumps(operatorDTO)

    res_data = authority_dubbo_service_conn.invoke(interface, method, param)
    print('res_data is ', res_data)


def teardown_module(module):
    """
    这个模块的测试用例跑完之后，用这个方法把连接关掉
    """


if __name__ == "__main__":
    pass
