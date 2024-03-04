# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/3/4 13:25
# @File :AlarmPage.py
# @Project : ZS22A_UI

from PIL import Image
import io
import base64
import os.path
import allure
from time import sleep
from Common.Common import Common
from Config.Config import Config
from Common.CompareImage import are_images_equal, download_image
from playwright.sync_api import expect

class AlarmPage(Common):
    # 元素定位器
    __alarm_event = "报警事件"
    __temp_monitoring = "温度监测"
    __global = ("menuitem", "全局温度")
    __analysis = ("menuitem", "分析对象")
    __difference = ("menuitem", "对象温差")
    __device = "设备异常"
    __storage = ("menuitem", "存储异常")
    __network = ("menuitem", "网络异常")
    __other = "其他事件"
    __unauthorized = ("menuitem", "非法访问")

    @allure.step("选择报警事件")
    def select_alarm(self):
        self.page.get_by_text(self.__alarm_event).click()

    @allure.step("选择温度监测")
    def select_temp_monitoring(self):
        self.page.get_by_text(self.__temp_monitoring).click()

    @allure.step("选择全局温度")
    def select_global(self):
        self.page.get_by_role("menuitem", name=self.__global[1]).click()

    @allure.step("选择分析对象")
    def select_analysis(self):
        self.page.get_by_role("menuitem", name=self.__analysis[1]).click()

    @allure.step("选择对象温差")
    def select_difference(self):
        self.page.get_by_role("menuitem", name=self.__difference[1]).click()

    @allure.step("选择设备异常")
    def select_device(self):
        self.page.get_by_text(self.__device).click()

    @allure.step("选择存储异常")
    def select_storage(self):
        self.page.get_by_role("menuitem", name=self.__storage[1]).click()

    @allure.step("选择网络异常")
    def select_network(self):
        self.page.get_by_role("menuitem", name=self.__network[1]).click()

    @allure.step("选择其他事件")
    def select_other(self):
        self.page.get_by_text(self.__other).click()

    @allure.step("选择非法访问")
    def select_unauthorized(self):
        self.page.get_by_role("menuitem", name=self.__unauthorized[1]).click()


















































































