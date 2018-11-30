# -*- coding:utf-8 -*-
# Power by godaipl 2018-11-29 19:08:41

from util.common.print import printutils

from termcolor import cprint


def test_print_yellow():
    print("\033[31m你好波波\033[0m")
    cprint('我要打印的东西', color='red')
    printutils.print_red('我要打印的东西')


