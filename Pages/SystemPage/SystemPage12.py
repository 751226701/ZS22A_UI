# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/3/21 14:00
# @File :SystemPage
# @Project : ZS22A_UI

from PIL import Image
import io
import re
import base64
import os.path
import allure
from time import sleep
from Common.Common import Common
from Config.Config import Config
from Common.CompareImage import download_image
from playwright.sync_api import expect

class SystemPage(Common):
    # 定时重启子模块元素定位
    __test = ""

    @allure.step("启用开关")
    def enable_switch(self):
        self.page.get_by_role("switch").locator("span").click()

    @allure.step("设置定时重启时间")
    def set_time(self, time):
        """
        :param time: 每天、每周一、每周二、每周三、每周四、每周五、每周六、每周日
        :return: 无
        """
        self.page.get_by_placeholder("请选择").click()
        self.page.get_by_text(time).click()

    @allure.step("重启")
    def restart(self):
        self.page.get_by_role("button", name="重启").click()

    @allure.step("确定")
    def click_confirm(self):
        self.page.get_by_role("button", name="确定").click()

    @allure.step("取消")
    def click_cancel(self):
        self.page.get_by_role("button", name="取消").click()




















