#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xiayun
# @Time     : 2022/5/1 15:49
# @Description     : 这是一个**功能的Python文件
# @Software : PyCharm
from Keys_Excel.FileRead.ReadFile import read_excel
from Keys_Excel.Keys.keys import Keys


class RunTestCases():
    def __init__(self):
        self.passCases_num = 0
        self.failedCases_num = 0

    def run_testcases(self,file_path=None, _sheet_index=None, _have_title=True, reRunNum=0):
        """
        :param file_path:
        :param _sheet_index:
        :param _have_title:
        :param reRunNum:重跑次数，如果不为0，则失败重跑
        :return:
        """
        re = read_excel(file_path, _sheet_index, _have_title)
        key = None
        re_data = next(re)
        while True:
            try:
                # result = None
                for excel_data in re_data:
                    # 如果步骤为打开浏览器，则调用打开浏览器
                    if excel_data['operation'] == 'open_browser':
                        key = Keys(**excel_data['param'])
                    # 如果参数为空
                    elif 'assert' in excel_data['operation'] and key is not None:
                        result = getattr(key, excel_data['operation'])(**excel_data['param'])
                    elif key is not None:
                        getattr(key, excel_data['operation'])(**excel_data['param'])
                # 返回用例执行结果
                if result is True:
                    self.passCases_num += 1
                    re_data = re.send('Pass')
                elif result is False:
                    # 如果要求失败重跑
                    if reRunNum > 0:
                        reRunNum -= 1
                        continue    # 直接原有数据再次跑一遍，不执行获取新数据
                    self.failedCases_num += 1
                    re_data = re.send('Failed')
            # 如果遇到了StopIteration 说明没有用例了
            except StopIteration:
                break
            # 如果遇到其他异常，判定用例失败
            except Exception as e:
                # 判断是否重跑
                if reRunNum > 0:
                    reRunNum -= 1
                    continue
                self.failedCases_num += 1
                re_data = re.send('Failed')
