#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xiayun
# @Time     : 2022/5/1 15:45
# @Description     : 这是一个**功能的Python文件
# @Software : PyCharm
from Keys_Excel.RunTest.RunTestCases import run_testcases


def run():
    run_testcases(r'./testcases/testcases.xlsx')


if __name__ == '__main__':
    run()