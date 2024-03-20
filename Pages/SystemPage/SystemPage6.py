# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/3/19 17:17
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
from Common.CompareImage import are_images_equal, download_image
from playwright.sync_api import expect


class SystemPage(Common):
    # 屏蔽区域子模块元素定位
    __test = ""

    @allure.step("添加分析对象")
    def add_obj(self, x, y, x1, y1):
        """
        :param x: 起始横坐标
        :param y: 起始纵坐标
        :param x1: 末端横坐标
        :param y1: 末端纵坐标
        :return: 无
        """
        self.page.locator("form i").first.click()
        mouse = self.page.mouse
        mouse.move(x, y)
        mouse.down()
        mouse.move(x1, y1, steps=50)
        mouse.up()

    @allure.step("点击默认")
    def click_default(self):
        self.page.get_by_role("button", name="默认").click()

    @allure.step("点击刷新")
    def click_refresh(self):
        self.page.get_by_role("button", name="刷新").click()

    @allure.step("点击确定")
    def click_ok(self):
        self.page.get_by_role("button", name="确定").click()