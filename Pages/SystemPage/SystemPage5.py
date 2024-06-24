# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/3/19 15:43
# @File :SystemPage5
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
    # 全局测温设置子模块元素定位
    __test = ""

    @allure.step("点击鼠标显示温度开关")
    def click_mouse_temp_switch(self):
        self.page.locator("div").filter(has_text=re.compile(r"^鼠标点击显示温度$")).locator("span").click()

    @allure.step("点击测温档位下拉框")
    def click_temp_level_select(self):
        self.page.locator("div").filter(has_text=re.compile(r"^测温档位 ℃$|^-20~150100~550 ℃$")).get_by_placeholder("请选择").click()

    @allure.step("选择-20-150度档位")
    def select_150(self):
        self.page.get_by_text("-20~").click()

    @allure.step("选择100-550度档位")
    def select_550(self):
        self.page.get_by_text("~550").click()

    @allure.step("选择色带")
    def select_color_bar(self, value):
        self.page.get_by_label("全局设置").locator("i").nth(2).click()
        self.page.get_by_text(value).click()

    @allure.step("点击色带显示开关")
    def click_color_bar_switch(self):
        self.page.locator("div").filter(has_text=re.compile(r"^色带条显示$")).locator("span").click()

    @allure.step("点击冷热点追踪开关")
    def click_hot_cold_switch(self):
        (self.page.get_by_label("全局设置").locator("form div").
         filter(has_text="冷热点追踪设置 高温 清空 确定 低温 清空 确定").get_by_role("switch").locator("span").click())

    @allure.step("设置自定义发射率值")
    def set_emiss(self, value):
        self.page.get_by_label("全局温度参数").get_by_role("textbox").nth(1).fill(value)

    @allure.step("点击发射率下拉框")
    def click_emiss_select(self):
        self.page.get_by_label("全局温度参数").get_by_placeholder("请选择").click()

    @allure.step("选择发射率")
    def select_emiss(self, value):
        self.click_emiss_select()
        self.page.get_by_text(value).click()

    @allure.step("设置距离参数")
    def set_distance(self, value):
        (self.page.get_by_label("全局温度参数").locator("form div").
         filter(has_text="距离 M (0.1~200)").get_by_role("textbox").fill(value))

    @allure.step("设置反射温度")
    def set_reflect(self, value):
        (self.page.locator("div").filter(has_text=re.compile(r"^反射温度 ℃ \(-40~2000\)$")).
         get_by_role("textbox").fill(value))

    @allure.step("设置全局温度修正值")
    def set_isotherm(self, value):
        (self.page.get_by_label("全局温度参数").locator("form div").
         filter(has_text="全局温度修正 ℃(-1.0~1.0)").get_by_role("textbox").fill(value))

    @allure.step("点击等温线开关")
    def click_isotherm_switch(self):
        self. page.get_by_label("等温线设置").get_by_role("switch").locator("span").click()

    @allure.step("选择关闭等温线")
    def close_isotherm(self):
        self.page.get_by_label("等温线设置").locator("i").first.click()

    @allure.step("设置高等温线")
    def set_isotherm_high(self):
        self.page.get_by_label("等温线设置").locator("i").nth(1).click()

    @allure.step("设置低等温线")
    def set_isotherm_low(self):
        self.page.get_by_label("等温线设置").locator("i").nth(2).click()

    @allure.step("设置区间等温线")
    def set_isotherm_range(self):
        self.page.get_by_label("等温线设置").locator("i").nth(3).click()

    @allure.step("设置区间外等温线")
    def set_isotherm_range_out(self):
        self.page.get_by_label("等温线设置").locator("i").nth(4).click()

    @allure.step("设置等温线值高温阈值")
    def set_isotherm_high_value(self, value):
        (self.page.get_by_label("等温线设置").locator("form div").
         filter(has_text="高温 ℃").get_by_role("textbox").fill(value))

    @allure.step("设置等温线值低温阈值")
    def set_isotherm_low_value(self, value):
        (self.page.get_by_label("等温线设置").locator("form div").
         filter(has_text="低温 ℃ 清空 确定").get_by_role("textbox").fill(value))

    @allure.step("点击默认")
    def click_default(self):
        self.page.get_by_role("button", name="默认").click()

    @allure.step("点击刷新")
    def click_refresh(self):
        self.page.get_by_role("button", name="刷新").click()

    @allure.step("点击确定")
    def click_ok(self):
        self.page.get_by_role("button", name="确定").click()

























































