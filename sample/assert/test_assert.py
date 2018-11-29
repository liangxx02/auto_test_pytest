# -*- coding:utf-8 -*-
# Power by godaipl 2018-11-21 11:30:45
import pytest


def test_template_assert():  # 定义一个断言测试方法
    print('template_assert_test called')
    x = 1
    y = 2

    z = x + y

    assert 3 == z
    assert x == z


def test_template_assert1():  # 定义一个断言测试方法
    print('template_assert1_test called')


def test_zero_division():
    with pytest.raises(ZeroDivisionError) as excinfo:
        1 / 0

    assert excinfo.type == 'RuntimeError'


if __name__ == "__main__":
    pass
