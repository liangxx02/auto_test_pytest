# -*- coding:utf-8 -*-
# Power by godaipl 2018-11-21 13:22:11


# 功能函数
def multiply(a, b):
    return a * b


# ===============fixfures================
def setup_module(module):
    print('setup_module called')


def teardown_module(module):
    print('teardown_module called')


def setup_function(function):
    print('setup_function called')


def teardown_function(function):
    print('teardown_function called')


# ===============测试用例================
def test_numbers_3_4():
    print('test_numbers_3_4 called')
    assert multiply(3, 4) == 12


def test_string_3():
    print('test_string_3 called')
    assert multiply('a', 3) == 'aaa'


class TestClass:
    @classmethod
    def setup_class(cls):
        print('setup_class')

    @classmethod
    def teardown_class(cls):
        print('teardown_class')

    @classmethod
    def setup_function(function):
        print('setup_function')

    @classmethod
    def teardown_function(function):
        print('teardown_function')

    def test_class_function(self):
        print('test_class_function')

    def test_class_function2(self):
        print('test_class_function2')


if __name__ == "__main__":
    pass
