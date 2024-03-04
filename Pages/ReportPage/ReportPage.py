# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/2/29 16:50
# @File :ReportPage.py
# @Project : ZS22A_UI

import os.path
import re

import allure
from time import sleep
from Common.Common import Common
from Config.Config import Config
from Common.CompareImage import are_images_equal, download_image
from playwright.sync_api import expect

class ReportPage(Common):
    __object_temp = ".el-select__caret"
    __object_temp_high = ("li", "最高温")
    __object_temp_low = ("li", "最低温")
    __object_temp_avg = ("li", "平均温")
    __search = ".icon-search"
    __point = ".el-checkbox__inner"
    __line = "label:nth-child(2) > .el-checkbox__input > .el-checkbox__inner"
    __round = "label:nth-child(3) > .el-checkbox__input > .el-checkbox__inner"
    __rectangle = "label:nth-child(4) > .el-checkbox__input > .el-checkbox__inner"
    __polygon = "label:nth-child(5) > .el-checkbox__input > .el-checkbox__inner"
    __select_all = ("label", "全选", "span", 1)
    __download_curve_image = ".downloadBtn"
    __period = ("form", "按时间间隔", "请选择")
    __period_1min = ("li", "1min")
    __period_5min = ("li", r"^5min$")
    __period_10min = ("li", "10min")
    __period_15min = ("li", "15min")
    __period_60min = ("li", "60min")
    __export_report = "导出报表"

    @allure.step("对象温度类型选择")
    def select_object_temp(self):
        self.page.locator(self.__object_temp).first.click()

    @allure.step("对象温度最高温")
    def select_object_temp_high(self):
        self.page.locator(self.__object_temp_high[0]).filter(has_text=self.__object_temp_high[1]).click()

    @allure.step("对象温度最低温")
    def select_object_temp_low(self):
        self.page.locator(self.__object_temp_low[0]).filter(has_text=self.__object_temp_low[1]).click()

    @allure.step("对象温度平均温")
    def select_object_temp_avg(self):
        self.page.locator(self.__object_temp_avg[0]).filter(has_text=self.__object_temp_avg[1]).click()

    @allure.step("查询温度曲线")
    def search_temperature_curve(self):
        self._click(self.__search)

    @allure.step("点击全选")
    def select_all(self):
        (self.page.locator(self.__select_all[0]).filter(has_text=self.__select_all[1]).
         locator(self.__select_all[2]).nth(self.__select_all[3]).click())

    @allure.step("下载温度曲线截图")
    def download_temperature_curve_image(self):
        self._click(self.__download_curve_image)

    @allure.step("选择时间间隔")
    def select_period(self):
        (self.page.locator(self.__period[0]).filter(has_text=self.__period[1]).
         locator(self.__period[2]).click())

    @allure.step("选择1min")
    def select_period_1min(self):
        self.page.locator(self.__period_1min[0]).filter(has_text=self.__period_1min[1]).click()

    @allure.step("选择5min")
    def select_period_5min(self):
        (self.page.locator(self.__period_5min[0]).
         filter(has_text=re.compile(self.__period_5min[1])).click())

    @allure.step("选择10min")
    def select_period_10min(self):
        self.page.locator(self.__period_10min[0]).filter(has_text=self.__period_10min[1]).click()

    @allure.step("选择15min")
    def select_period_15min(self):
        self.page.locator(self.__period_15min[0]).filter(has_text=self.__period_15min[1]).click()


    @allure.step("选择60min")
    def select_period_60min(self):
        self.page.locator(self.__period_60min[0]).filter(has_text=self.__period_60min[1]).click()

    @allure.step("导出报表")
    def export_report(self):
        self.page.get_by_role("button", name=self.__export_report).click()








