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
    for excel_data in re:
        # print(excel_data)
        #如果步骤为打开浏览器，则调用打开浏览器
        if excel_data['operation'] == 'open_browser':
            key = Keys(**excel_data['param'])
        # #如果参数为空
        # elif not excel_data['param']:
        #     getattr(key, excel_data['operation'])()
        elif 'assert' in excel_data['operation']:
            result = getattr(key, excel_data['operation'])(**excel_data['param'])
            if result:
                re.send('Pass')
            else:
                re.send('Failed')
        else:
            getattr(key, excel_data['operation'])(**excel_data['param'])
