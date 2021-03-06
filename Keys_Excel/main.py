#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xiayun
# @Time     : 2022/5/1 15:45
# @Description     : 这是一个**功能的Python文件
# @Software : PyCharm
import os


from Keys_Excel.RunTest.RunTestCases import RunTestCases

def run():
    # 自动搜索含testcases的用例

    rtc = RunTestCases()
    for r, d, fs in os.walk('./testcases'):
        for f in fs:
            if 'testcases' in f:
                print(os.path.join(r, f))
                rtc.run_testcases(os.path.join(r, f),reRunNum=1)
    print('共执行{}条用例，成功用例数:{},失败用例数:{},成功率:{}%'.format(rtc.passCases_num + rtc.failedCases_num,
                                                      rtc.passCases_num,
                                                      rtc.failedCases_num,
                                                      rtc.passCases_num*100 / (rtc.passCases_num + rtc.failedCases_num)))
    # run_testcases(r'./testcases/testcases.xlsx')


if __name__ == '__main__':
    run()
