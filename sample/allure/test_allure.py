# -*- coding:utf-8 -*-

import allure

# Allure中对严重级别的定义：
# 1、 Blocker级别：中断缺陷（客户端程序无响应，无法执行下一步操作）
# 2、 Critical级别：临界缺陷（ 功能点缺失）
# 3、 Normal级别：普通缺陷（数值计算错误）
# 4、 Minor级别：次要缺陷（界面错误与UI需求不符）
# 5、 Trivial级别：轻微缺陷（必输项无提示，或者提示不规范）


@allure.feature('test_module_01')
@allure.story('test_abcd_story_1')
@allure.title('test_abcd_title_1')
@allure.severity('blocker')
def test_abcd_story_1():
    """
    这是模块01的story1
    """
    print('test_abcd_story_1')


@allure.feature('test_module_01')
@allure.story('test_abcd_story_2')
@allure.title('test_abcd_title_2')
@allure.severity('critical')
def test_abcd_story_2():
    """
    这是模块01的story2
    """
    print('test_abcd_story_2')


@allure.feature('test_module_02')
@allure.severity('normal')
def test_abcd2():
    """
    这是第二个测试方法
    """
    print('test_abcd2')


@allure.feature('test_module_03')
@allure.severity('minor')
def test_abcd3():
    """
    这是第三个测试方法
    """
    assert 1 == 2


@allure.feature('test_module_03')
@allure.severity('trivial')
def test_abcd4():
    """
    这是第四个测试方法
    """
    assert 1 == 3


@allure.step("字符串相加：{0}，{1}")  # 测试步骤，可通过format机制自动获取函数参数
def str_add(str1, str2):
    print('hello')
    if not isinstance(str1, str):
        return "%s is not a string" % str1
    if not isinstance(str2, str):
        return "%s is not a string" % str2
    return str1 + ' ' + str2


@allure.feature('test_module_04')
@allure.story('test_story_01')
@allure.severity('blocker')
@allure.issue('http://jira.treefinance.com.cn/browse/AUTOTEST-41')
@allure.testcase('http://confluence.treefinance.com.cn')
def test_case():
    str1 = 'hello'
    str2 = 'world'
    assert str_add(str1, str2) == 'helloworld'
