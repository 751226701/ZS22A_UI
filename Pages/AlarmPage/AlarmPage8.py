# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/3/19 9:15
# @File :AlarmPage8.py
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

class AlarmPage(Common):
    # 报警事件子模块元素定位
    __test = ""

    @allure.step("查询报警事件")
    def query_alarm_event(self):
        self.page.locator(".icon-search").click()

    @allure.step("点击静音按钮")
    def click_mute_button(self):
        self.page.locator(".el-tooltip").click()

    @allure.step("点击报警复归")
    def click_recovery_button(self):
        self.page.get_by_role("button", name="报警复归").click()

    @allure.step("点击清空报警")
    def click_clear_alarm(self):
        self.page.get_by_role("button", name="清空报警").click()

    @allure.step("点击确定清空")
    def click_ok_clear_alarm(self):
        self.page.get_by_role("button", name="确定").click()

    @allure.step("点击取消清空")
    def click_cancel_clear_alarm(self):
        self.page.get_by_role("button", name="取消").click()

    @allure.step("报警类型选择")
    def alarm_type_select(self):
        self.page.locator(".el-select__caret").click()

    @allure.step("选择全部")
    def select_all(self):
        self.page.get_by_text("全部").click()

    @allure.step("取消全选")
    def cancel_all(self):
        self.page.locator("li").filter(has_text="全部").locator("span").click()

    @allure.step("选择全局温度")
    def select_global_temp(self):
        self.page.locator("span").filter(has_text="全局温度").click()

    @allure.step("取消全局温度")
    def cancel_global_temp(self):
        self.page.get_by_text("全局温度").nth(2).click()

    @allure.step("选择对象温度")
    def select_object_temp(self):
        self.page.get_by_text("对象温度").click()

    @allure.step("取消对象温度")
    def cancel_object_temp(self):
        self.page.locator("li").filter(has_text="对象温度").locator("span").click()

    @allure.step("选择对象温差")
    def select_object_temp_diff(self):
        self.page.locator("span").filter(has_text="对象温差").click()

    @allure.step("取消对象温差")
    def cancel_object_temp_diff(self):
        self.page.get_by_text("对象温差").nth(2).click()

    @allure.step("选择存储异常")
    def select_storage_abnormal(self):
        self.page.locator("li").filter(has_text="存储异常").nth(2).click()

    @allure.step("取消存储异常")
    def cancel_storage_abnormal(self):
        self.page.get_by_text("存储异常").nth(2).click()

    @allure.step("选择网络异常")
    def select_network_abnormal(self):
        self.page.locator("span").filter(has_text="网络异常").click()

    @allure.step("取消网络异常")
    def cancel_network_abnormal(self):
        self.page.get_by_text("网络异常").nth(2).click()

    @allure.step("选择非法访问")
    def select_illegal_access(self):
        self.page.locator("span").filter(has_text="非法访问").click()

    @allure.step("取消非法访问")
    def cancel_illegal_access(self):
        self.page.get_by_text("非法访问").nth(2).click()

    @allure.step("选择报警输入")
    def select_alarm_input(self):
        self.page.locator("span").filter(has_text="报警输入").click()

    @allure.step("取消报警输入")
    def cancel_alarm_input(self):
        self.page.get_by_text("报警输入").nth(2).click()
























































