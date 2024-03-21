# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/3/21 13:43
# @File :SystemPage11
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
    # 系统升级子模块元素定位
    __test = ""

    @allure.step("备份配置文件")
    def backup_config(self):
        self.page.get_by_role("button", name="备份配置文件").click()

    @allure.step("恢复出厂设置")
    def restore_factory(self):
        self.page.get_by_role("button", name="恢复出厂设置").click()

    @allure.step("重启")
    def restart(self):
        self.page.get_by_role("button", name="重启").click()

    @allure.step("确定")
    def click_confirm(self):
        self.page.get_by_role("button", name="确定").click()

    @allure.step("取消")
    def click_cancel(self):
        self.page.get_by_role("button", name="取消").click()
















