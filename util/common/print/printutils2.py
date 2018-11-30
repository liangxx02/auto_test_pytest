# -*- coding:utf-8 -*-
# Power by godaipl 2018-11-27 11:02:35
# 这个工具不要用，只作学习使用

import sys
from enum import Enum, unique


# 显示颜色格式：\033[显示方式;字体色;背景色m......[\033[0m]
# -------------------------------------------
# -------------------------------------------
# 字体色     |       背景色     |      颜色描述
# -------------------------------------------
# 30        |        40       |       黑色
# 31        |        41       |       红色
# 32        |        42       |       绿色
# 33        |        43       |       黃色
# 34        |        44       |       蓝色
# 35        |        45       |       紫红色
# 36        |        46       |       青蓝色
# 37        |        47       |       白色
# -------------------------------------------
# -------------------------------
# 显示方式     |      效果
# -------------------------------
# 0           |     终端默认设置
# 1           |     高亮显示
# 4           |     使用下划线
# 5           |     闪烁
# 7           |     反白显示
# 8           |     不可见
# -------------------------------


@unique
class ColourEnum(Enum):
    """
    前景颜色定义
    """
    BLACK = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    # 紫红色
    PURPLISHRED = 35
    BLUISHGREEN = 36
    WHITE = 37


@unique
class ShowEnum(Enum):
    """
    显示方式
    """
    # 终端默认设置
    DEFAULT = 0
    # 高亮显示
    HIGHLIGHT = 1
    # 使用下划线
    UNDERSCORE = 4
    # 闪烁
    TWINKLE = 5
    # 反白显示
    ANTIWHITE = 7
    # 不可见
    INVISIBLE = 8


def print_black(*value):
    print_colour_str(value, colour=ColourEnum.BLACK)


def print_red(*value):
    print_colour_str(value, colour=ColourEnum.RED)


def print_green(*value):
    print_colour_str(value, colour=ColourEnum.GREEN)


def print_yellow(*value):
    print_colour_str(value, colour=ColourEnum.YELLOW)


def print_blue(*value):
    print_colour_str(value, colour=ColourEnum.BLUE)


def test_print_cases():
    print('11111')
    print_black('测试黑色', 1, 2)
    print_red('测试红色', 1, 2)
    print_green('测试绿色', 1, 2)
    print_yellow('测试黄色', 1, 2)
    print_blue('测试蓝色', 1, 2)


def print_colour_str(value, show_type=ShowEnum.DEFAULT, colour=ColourEnum.BLACK):
    """
    着色公共方法
    :param colour: 想要打印的颜色， 具体参看枚举类
    :param show_type: 打印方式，具体参看枚举类
    :param value: 可能是一个，也可能是好几个
    :return:
    """
    if value:
        print('\033[' + str(show_type.value) + ';' + str(colour.value) + ';20m', end='')
        if type(value) is tuple:
            for object_tmp in value:
                print(object_tmp, end='')
        else:
            print(value, end='')
        print('\033[0m')

