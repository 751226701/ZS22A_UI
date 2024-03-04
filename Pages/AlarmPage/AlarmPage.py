# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/3/4 13:25
# @File :AlarmPage.py
# @Project : ZS22A_UI
import re

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
    # 子模块元素定位
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

    # 报警事件子模块元素定位
    __global_high_temp = ".el-checkbox__inner"
    __global_high_temp_box = "div:nth-child(6) > .el-checkbox > .el-checkbox__input > .el-checkbox__inner"
    __global_high_temp_select = "请选择"
    __global_low_temp_value = "div:nth-child(4) > .el-input__inner"
    __global_low_temp_box = "div:nth-child(6) > .el-checkbox > .el-checkbox__input > .el-checkbox__inner"
    __global_low_temp_select = "请选择"
    __select_greater = ("list", ">")
    __select_lower = ("list", "<")
    __debounce = ("div", r"^去抖动 s \(1~10\)$", "textbox")
    __alarm_interval_time_select = ("div", r"^报警间隔时间$", "请选择")
    __alarm_interval_time_30S = "30s"
    __alarm_interval_time_60S = "60s"
    __alarm_interval_time_5min = "5min"
    __alarm_interval_time_10min = "10min"
    __alarm_interval_time_15min = "15min"
    __alarm_interval_time_30min = "30min"
    __alarm_interval_time_60min = "60min"
    __vl_record_box = ("label", "可见光录像", "span", 1)
    __ir_record_box = ("label", "红外录像", "span", 1)
    __record_time = ("form", "录像可见光录像 红外录像 录像时间 s(10~300", "textbox")
    __vl_capture_box = ("label", "可见光抓图", "span", 1)
    __ir_capture_box = ("label", "红外抓图", "span", 1)
    __email_switch = ("div", r"^邮件通知$", "span")
    __light_switch = "div:nth-child(4) > .el-form-item__content > .el-switch > .el-switch__core"
    __duration = ("form", "录像可见光录像 红外录像 录像时间 s(10~300", "textbox")

    # 全局温度子模块元素定位


    # 分析对象子模块元素定位

    # 对象温差子模块元素定位

    # 存储异常子模块元素定位

    # 网络异常子模块元素定位

    # 非法访问子模块元素定位


    # 子模块方法
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


    # 全局温度子模块方法
    @allure.step("点击全局最高温复选框")
    def click_global_high_temp_box(self):
        self.page.locator(self.__global_high_temp_box).first.click()

    @allure.step("点击全局最低温复选框")
    def click_global_low_temp_box(self):
        self.page.locator(self.__global_low_temp_box).click()

    @allure.step("全局最高温报警条件选择")
    def global_high_temp_select(self):
        self.page.get_by_placeholder(self.__global_high_temp_select).first.click()

    @allure.step("全局最低温报警条件选择")
    def global_low_temp_select(self):
        self.page.get_by_placeholder(self.__global_low_temp_select).nth(1).click()

    @allure.step("设置高温报警阈值")
    def set_global_high_temp_value(self, value):
        self.page.locator(self.__global_low_temp_value).fill(value)

    @allure.step("设置低温报警阈值")
    def set_global_low_temp_value(self, value):
        self.page.locator(self.__global_low_temp_value).fill(value)

    @allure.step("选择大于")
    def select_greater(self):
        self.page.get_by_role("list").get_by_text(self.__select_greater[1]).click()

    @allure.step("选择小于")
    def select_lower(self):
        self.page.get_by_role("list").get_by_text(self.__select_lower[1]).click()

    @allure.step("设置去抖动")
    def set_debounce(self, value):
        (self.page.locator(self.__debounce[0]).filter(has_text=re.compile(self.__debounce[1])).
         get_by_role("textbox").fill(value))

    @allure.step("设置报警间隔时间")
    def set_alarm_interval_time(self):
        self.page.locator("div").filter(has_text=re.compile(r"^报警间隔时间$")).get_by_placeholder("请选择").click()

    @allure.step("选择30s")
    def select_30s(self):
        self.page.get_by_text(self.__alarm_interval_time_30S).click()

    @allure.step("选择60s")
    def select_60s(self):
        self.page.get_by_text(self.__alarm_interval_time_60S).click()

    @allure.step("选择5min")
    def select_5min(self):
        self.page.get_by_text("5min", exact=True).click()

    @allure.step("选择10min")
    def select_10min(self):
        self.page.get_by_text(self.__alarm_interval_time_10min).click()

    @allure.step("选择15min")
    def select_15min(self):
        self.page.get_by_text(self.__alarm_interval_time_15min).click()

    @allure.step("选择30min")
    def select_30min(self):
        self.page.get_by_text(self.__alarm_interval_time_30min).click()

    @allure.step("选择60min")
    def select_60min(self):
        self.page.get_by_text(self.__alarm_interval_time_60min).click()

    @allure.step("点击可见光录像复选框")
    def click_vl_record_box(self):
        (self.page.locator(self.__vl_record_box[0]).filter(has_text=self.__vl_record_box[1]).
         locator(self.__vl_record_box[2]).nth(1).click())

    @allure.step("点击红外录像复选框")
    def click_ir_record_box(self):
        (self.page.locator(self.__ir_record_box[0]).filter(has_text=self.__ir_record_box[1]).
         locator(self.__ir_record_box[2]).nth(1).click())

    @allure.step("设置录像时间")
    def set_record_time(self, value):
        (self.page.locator(self.__record_time[0]).filter(has_text=self.__record_time[1]).
         get_by_role("textbox").first.fill(value))

    @allure.step("点击可见光抓图复选框")
    def click_vl_capture_box(self):
        (self.page.locator(self.__vl_capture_box[0]).filter(has_text=self.__vl_capture_box[1]).
         locator(self.__vl_capture_box[2]).nth(1).click())

    @allure.step("点击红外抓图复选框")
    def click_ir_capture_box(self):
        (self.page.locator(self.__ir_capture_box[0]).filter(has_text=self.__ir_capture_box[1]).
         locator(self.__ir_capture_box[2]).nth(1).click())

    @allure.step("点击邮件通知选择框")
    def click_email_switch(self):
        (self.page.locator(self.__email_switch[0]).filter(has_text=re.compile(self.__email_switch[1])).
         locator(self.__email_switch[2]).click())

    @allure.step("点击灯光开关")
    def click_light_switch(self):
        self._click(self.__light_switch)

    @allure.step("设置灯光持续时间")
    def set_duration(self, value):
        (self.page.locator(self.__duration[0]).filter(has_text=self.__duration[1]).
         get_by_role("textbox").nth(1).fill(value))
















    # 分析对象子模块方法

    # 对象温差子模块方法

    # 存储异常子模块方法

    # 网络异常子模块方法

    # 非法访问子模块方法















































































