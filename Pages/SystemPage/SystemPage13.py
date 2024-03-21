# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/3/21 14:26
# @File :SystemPage13
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
    # 操作日志子模块元素定位
    __test = ""

    @allure.step("选择用户")
    def select_user(self):
        self.page.get_by_placeholder("请选择").click()

    @allure.step("全部")
    def all(self):
        self.page.get_by_text("全部").click()

    @allure.step("root")
    def root(self):
        self.page.locator("li").filter(has_text="root").locator("span").click()

    @allure.step("admin")
    def admin(self):
        self.page.locator("span").filter(has_text="admin").click()

    @allure.step("user")
    def user(self):
        self.page.get_by_text("user").click()

    @allure.step("设置操作内容")
    def set_operation(self, value):
        self. page.get_by_role("textbox").nth(3).fill(value)

    @allure.step("查询")
    def search(self):
        self.page.locator("form i").nth(3).click()

    @allure.step("刷新")
    def refresh(self):
        self.page.locator("form i").nth(4).click()
