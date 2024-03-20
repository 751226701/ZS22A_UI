# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/3/20 8:50
# @File :SystemPage7
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

    @allure.step("补光灯模式选择")
    def select_light_mode(self):
        self.page.get_by_placeholder("请选择").click()

    @allure.step("手动")
    def select_manual(self):
        self.page.get_by_text("手动").click()

    @allure.step("时间自动")
    def select_time_auto(self):
        self.page.get_by_text("时间自动").click()

    @allure.step("补光灯开关")
    def select_light_switch(self):
        self.page.get_by_role("switch").locator("span").click()

    @allure.step("补光灯亮度设置")
    def select_light_brightness(self, value):
        self.page.locator("form div").filter(has_text="补光灯亮度").get_by_role("textbox").fill(value)

    @allure.step("点击默认")
    def click_default(self):
        self.page.get_by_role("button", name="默认").click()

    @allure.step("点击刷新")
    def click_refresh(self):
        self.page.get_by_role("button", name="刷新").click()

    @allure.step("点击确定")
    def click_ok(self):
        self.page.get_by_role("button", name="确定").click()

































