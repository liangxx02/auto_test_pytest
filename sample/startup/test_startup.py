# -*- coding:utf-8 -*-
# Power by godaipl 2018-11-21 11:54:45
import pytest

from util.common.print import printutils2


def test_case1():
    printutils2.print_yellow('test_case1 called')


@pytest.mark.P0
def test_case2():
    printutils2.print_yellow('test_case2 called')


@pytest.mark.P1
def test_case3():
    printutils2.print_yellow('test_case3 called')


class TestClass:
    def test_case4(self):
        printutils2.print_yellow('test_case4 called')

    def test_case5(self):
        printutils2.print_yellow('test_case5 called')

