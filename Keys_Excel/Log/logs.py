#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xiayun
# @Time     : 2022/3/16 21:15
# @Description     : 日志模块
# @Software : PyCharm
"""
    logger:
    handlers:处理器，文件、流
    formatter:格式器，显示格式

"""
import logging
import logging.config


def logger():
    #直接在代码中完成日志配置
    log_format = '[%(asctime)s]%(filename)s-%(levelname)s-lineNo:%(lineno)d %(message)s'
    # logging.basicConfig('./log.txt', 'r', format=log_format)
    logger_ = logging.getLogger('requests')
    file_handler = logging.FileHandler('./Log/logs.log', encoding='utf-8')
    logger_.addHandler(file_handler)
    formatter = logging.Formatter(fmt=log_format)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)
    logger_.setLevel(logging.DEBUG)

    #使用日志文件形成配置
    # log_file_path = path.join(path.dirname(path.abspath(__file__)), r'./log.ini')
    # logging.config.fileConfig(log_file_path)
    # logger_ = logging.getLogger('root')
    return logger_


