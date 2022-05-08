#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xiayun
# @Time     : 2022/5/1 15:49
# @Description     : 这是一个**功能的Python文件
# @Software : PyCharm
from Keys_Excel.FileRead.ReadFile import read_excel
from Keys_Excel.Keys.keys import Keys


def run_testcases(file_path=None, _sheet_index=None, _have_title=True):
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
                re_data = re.send('Pass')
            elif result is False:
                re_data = re.send('Failed')
        except StopIteration:
            break
