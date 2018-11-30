# -*- coding:utf-8 -*-
# Power by godaipl 2018-11-27 11:02:35

import os

import sys

from enum import Enum

from termcolor import cprint


class ColourEnum(Enum):
    """
    前景颜色定义
    """
    RED = 'red'
    GREEN = 'green'
    YELLOW = 'yellow'
    BLUE = 'blue'


def print_red(*value):
    print_colour_str(value, colour=ColourEnum.RED)


def print_green(*value):
    print_colour_str(value, colour=ColourEnum.GREEN)


def print_yellow(*value):
    print_colour_str(value, colour=ColourEnum.YELLOW)


def print_blue(*value):
    print_colour_str(value, colour=ColourEnum.BLUE)


def print_colour_str(value, colour=ColourEnum.RED):
    """
    着色公共方法,根据打印环境，输出不同内容
    :param colour: 想要打印的颜色， 具体参看枚举类
    :param value: 可能是一个，也可能是好几个
    :return:
    """
    if value:
        value_tmp = ''
        if type(value) is tuple:
            for object_tmp in value:
                if object_tmp is str:
                    value_tmp = value_tmp + object_tmp
                else:
                    value_tmp = value_tmp + str(object_tmp)
        else:
            if value is str:
                value_tmp = value
            else:
                value_tmp = str(value)

        env = os.getenv('TERM')

        # 判断打印环境，来区分打印输出方式

        if env:
            cprint(value_tmp, colour.value)
        else:
            print(value_tmp, file=sys.stderr)
