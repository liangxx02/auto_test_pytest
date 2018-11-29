# -*- coding:utf-8 -*-
# Power by godaipl 2018-11-21 11:54:45
import pytest


def test_case1():
    print('test_case1 called')


@pytest.mark.P0
def test_case2():
    print('test_case2 called')


@pytest.mark.P1
def test_case3():
    print('test_case3 called')


class TestClass:
    def test_case4(self):
        print('test_case4 called')

    def test_case5(self):
        print('test_case5 called')


if __name__ == "__main__":
    pass
