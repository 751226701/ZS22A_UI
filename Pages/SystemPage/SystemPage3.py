# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/3/19 14:14
# @File :SystemPage3
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
    # OSD设置子模块元素定位
    __test = ""

    @allure.step("点击全局温度显示复选框")
    def click_global_temp_box(self):
        self.page.locator(".el-checkbox__inner").first.click()

    @allure.step("选择温度显示类型")
    def select_temp_type(self):
        self.page.get_by_placeholder("请选择").click()

    @allure.step("最高温")
    def max_temp(self):
        self.page.get_by_text("最高温", exact=True).click()

    @allure.step("最低温")
    def min_temp(self):
        self.page.get_by_text("最低温", exact=True).click()

    @allure.step("平均温")
    def avg_temp(self):
        self.page.get_by_text("平均温", exact=True).click()

    @allure.step("最高温+最低温")
    def max_min_temp(self):
        self.page.get_by_text("最高温+最低温", exact=True).click()

    @allure.step("最高温+平均温")
    def max_avg_temp(self):
        self.page.get_by_text("最高温+平均温", exact=True).click()

    @allure.step("平均温+最低温")
    def min_avg_temp(self):
        self.page.get_by_text("平均温+最低温", exact=True).click()

    @allure.step("最高温+最低温+平均温")
    def max_min_avg_temp(self):
        self.page.get_by_text("最高温+最低温+平均温", exact=True).click()

    @allure.step("点击日期显示复选框")
    def click_date_box(self):
        self.page.locator("div").filter(has_text=re.compile(r"^显示$")).locator("span").nth(1).click()

    @allure.step("点击字符串复选框")
    def click_string_box(self):
        (self.page.get_by_label("红外字符串叠加").locator("form div").
         filter(has_text="字符串显示").locator("span").nth(1).click())

    @allure.step("设置字符串内容")
    def set_string_content(self, value):
        (self.page.get_by_label("红外字符串叠加").locator("form div").
         filter(has_text="字符串显示").get_by_role("textbox").fill(value))

    @allure.step("点击通道名称复选框")
    def click_channel_name_box(self):
        (self.page.get_by_label("红外字符串叠加").locator("form div").
         filter(has_text="通道名称显示").locator("span").nth(1).click())

    @allure.step("设置通道名称")
    def set_channel_name(self, value):
        (self.page.get_by_label("红外字符串叠加").locator("form div").
         filter(has_text="通道名称显示").get_by_role("textbox").fill(value))

    @allure.step("点击可见光日期显示复选框")
    def click_vl_date_box(self):
        (self.page.locator("div").filter(has_text=re.compile(r"^显示 （该设备可见光日期显示无法移动！）$")).
         locator("span").first.click())

    @allure.step("点击可见光字符串复选框")
    def click_vl_string_box(self):
        (self.page.get_by_label("可见光字符串叠加").locator("form div").
         filter(has_text="字符串显示").locator("span").nth(1).click())

    @allure.step("设置可见光字符串内容")
    def set_vl_string_content(self, value):
        (self.page.get_by_label("可见光字符串叠加").locator("form div").
         filter(has_text="字符串显示").get_by_role("textbox").fill(value))

    @allure.step("点击可见光通道名称复选框")
    def click_vl_channel_name_box(self):
        (self.page.get_by_label("可见光字符串叠加").locator("form div").
         filter(has_text="通道名称显示").locator("span").nth(1).click())

    @allure.step("设置可见光通道名称")
    def set_vl_channel_name(self, value):
        (self.page.get_by_label("可见光字符串叠加").locator("form div").
         filter(has_text="通道名称显示").get_by_role("textbox").fill(value))

    @allure.step("点击默认")
    def click_default(self):
        self.page.get_by_role("button", name="默认").click()

    @allure.step("点击刷新")
    def click_refresh(self):
        self.page.get_by_role("button", name="刷新").click()

    @allure.step("点击确定")
    def click_ok(self):
        self.page.get_by_role("button", name="确定").click()


