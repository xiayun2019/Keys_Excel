#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xiayun
# @Time     : 2022/5/1 15:45
# @Description     : 这是一个**功能的Python文件
# @Software : PyCharm
import os

from Keys_Excel.RunTest.RunTestCases import run_testcases


def run():
    # 自动搜索含testcases的用例
    for r, d, fs in os.walk('./testcases'):
        for f in fs:
            if 'testcases' in f:
                print(os.path.join(r, f))
                run_testcases(os.path.join(r, f))
    # run_testcases(r'./testcases/testcases.xlsx')


if __name__ == '__main__':
    run()
