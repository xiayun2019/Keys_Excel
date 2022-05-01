#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xiayun
# @Time     : 2022/3/13 20:29
# @Description     : selenium 关键字驱动类:常用操作行为封装为关键字
# @Software : PyCharm
"""
1、创建driver
2、访问url
3、定位元素
4、click
5、send_keys
6、webDriverWait
7、quit
8、相对定位器(作业)

"""
import time

from selenium import webdriver

# 自定义关键字类
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with, RelativeBy
from selenium.webdriver.support.wait import WebDriverWait

from Selenium_POM.Utils.chromeOptions import chromeOptions
import threading


def open_browser(type_):
    if type_ == 'Chrome':
        driver = webdriver.Chrome(options=chromeOptions())
        return driver
    else:
        try:
            driver = getattr(webdriver, type_)()
        except Exception:
            driver = webdriver.Chrome()
        return driver


"""
python反射机制
    四大内置函数：getattr,获取指定类的属性
    getattr(类，属性)  = 类.属性  ，获取函数需要加上()
"""


class Keys:

    def __init__(self, _type):
        self.driver = open_browser(_type)
        self.driver.implicitly_wait(10)
        self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",  {
                                    "source":
                                    """
                                    Object.defineProperty(navigator, 'webdriver', 
                                    {get: () => undefined})
                                    """
                                    })

    # 访问url
    def open(self, url):
        self.driver.get(url)

    def locate(self, name=None, value=None, relative: RelativeBy = None):
        if relative is None:
            return self.driver.find_element(name, value)
        else:
            return self.driver.find_element(relative)

    def click(self, name, value):
        self.locate(name, value).click()

    def input(self, name, value, txt):
        try:
            self.locate(name, value).send_keys(txt)
        except Exception:
            raise Exception


    # 显示等待
    def web_el_wait(self, name, value):
        WebDriverWait(self.driver, 10).until(
            lambda el: self.locate(name, value),
            message="元素查找失败"
        )

    # 强制等待
    def wait(self, time_=3):
        time.sleep(int(time_))

    # 切换句柄
    def switch_handle(self, isclose_=False, index=1):
        handle = self.driver.window_handles
        if isclose_:
            self.driver.close()
        self.driver.switch_to.window(handle[index])

    def switch_frame(self, value, name=None):
        # 第一种方法
        # if name == 'id' or name == 'name':
        #     self.driver.switch_to.frame(value)
        # self.driver.switch_to.frame(self.locate(name,value))
        # 第二种方法
        # try:
        #     self.driver.switch_to.frame(self.locate('id',value))
        # except NoSuchElementException:
        #     try:
        #         self.driver.switch_to.frame(self.locate('name',value))
        #     except NoSuchElementException:
        #         self.driver.switch_to.frame(self.locate(name,value))
        # 第三种方法
        if name is None:
            self.driver.switch_to.frame(value)
        else:
            self.driver.switch_to.frame(self.locate(name, value))

    # 相对定位
    def relative_locate(self, relative_name: By, relative_vlaue: str, location: str, name, value):
        relative = locate_with(relative_name, relative_vlaue)  # 返回RelativeBy对象
        # if location in (locator:=['above','below','to_left_of','to_right_of']):
        #     relative_ = getattr(relative,location)(self.locate(name,value))
        #     return self.locate(relative=relative_)
        # else:
        #     raise Exception('定位方式错误，正确方式包括{}'.format(locator))
        relative_ = getattr(relative, location)(self.locate(name, value))
        return self.locate(relative=relative_)

    def assert_txt(self, name, value, txt):
        #解决特殊不可见字符的比较问题
        actual_txt = ''.join(x for x in self.locate(name, value).text if x.isprintable())
        expected_txt = txt
        if expected_txt == actual_txt:
            return True
        else:
            print('预期结果为:{}，实际结果为:{},不一致'.format(repr(expected_txt), repr(actual_txt)))
            return False

    def close(self):
        self.driver.quit()


if __name__ == "__main__":
    pass
