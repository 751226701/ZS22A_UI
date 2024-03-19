# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/3/18 17:19
# @File :AlarmPage7
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
    # 报警输入子模块元素定位
    __sensor_type = r"^传感器类型$|^传感器类型常开型 常闭型$"
    __alarm_interval_time_select = r"^报警间隔时间30s 60s 5min 10min 15min 30min 60min$|^报警间隔时间$"
    __record_time = "录像可见光录像 红外录像 录像时间 s(10~300"
    __audio_switch = "div:nth-child(4) > .el-form-item__content > .el-switch > .el-switch__core"
    __light_switch = "div:nth-child(5) > .el-form-item__content > .el-switch > .el-switch__core"
    __output_switch = "div:nth-child(6) > .el-form-item__content > .el-switch > .el-switch__core"
    __set_time = "录像可见光录像 红外录像 录像时间 s(10~300"

    @allure.step("报警启用状态开关")
    def alarm_switch(self):
        self.page.locator("div").filter(has_text=re.compile(r"^启用状态$")).locator("span").click()

    @allure.step("传感器类型选择")
    def sensor_type(self):
        self.page.locator("div").filter(has_text=re.compile(self.__sensor_type)).get_by_placeholder("请选择").click()

    @allure.step("常开型")
    def sensor_type_normal(self):
        self.page.get_by_text("常开型").click()

    @allure.step("常闭型")
    def sensor_type_close(self):
        self.page.get_by_text("常闭型").click()

    @allure.step("设置去抖动时间")
    def set_debounce_time(self, value):
        self.page.locator("div").filter(has_text=re.compile(r"^去抖动 s\(1-10\)$")).get_by_role("textbox").fill(value)

    @allure.step("设置报警间隔时间")
    def set_alarm_interval_time(self):
        self.page.locator("div").filter(has_text=re.compile(self.__alarm_interval_time_select)).get_by_placeholder("请选择").click()

    @allure.step("30S")
    def alarm_interval_30s(self):
        self.page.get_by_text("30s").click()

    @allure.step("60S")
    def alarm_interval_60s(self):
        self.page.get_by_text("60s").click()

    @allure.step("5min")
    def alarm_interval_5min(self):
        self.page.get_by_text("5min", exact=True).click()

    @allure.step("10min")
    def alarm_interval_10min(self):
        self.page.get_by_text("10min", exact=True).click()

    @allure.step("15min")
    def alarm_interval_15min(self):
        self.page.get_by_text("15min", exact=True).click()

    @allure.step("30min")
    def alarm_interval_30min(self):
        self.page.get_by_text("30min", exact=True).click()

    @allure.step("60min")
    def alarm_interval_60min(self):
        self.page.get_by_text("60min", exact=True).click()

    @allure.step("点击可见光录像复选框")
    def click_vl_record_box(self):
        self. page.locator("label").filter(has_text="可见光录像").locator("span").nth(1).click()

    @allure.step("点击红外录像复选框")
    def click_ir_record_box(self):
        self.page.locator("label").filter(has_text="红外录像").locator("span").nth(1).click()

    @allure.step("设置录像时间")
    def set_record_time(self, value):
        self.page.locator("form").filter(has_text=self.__record_time).get_by_role("textbox").first.fill(value)

    @allure.step("点击可见光抓图复选框")
    def click_vl_capture_box(self):
        self.page.locator("label").filter(has_text="可见光抓图").locator("span").nth(1).click()

    @allure.step("点击红外抓图复选框")
    def click_ir_capture_box(self):
        self.page.locator("label").filter(has_text="红外抓图").locator("span").nth(1).click()

    @allure.step("点击邮件通知开关")
    def click_email_switch(self):
        self.page.locator("div").filter(has_text=re.compile(r"^邮件通知$")).locator("span").click()

    @allure.step("点击音频播放开关")
    def click_audio_switch(self):
        self.page.locator(self.__audio_switch).click()

    @allure.step("设置音频播放时间")
    def set_audio_time(self, value):
        self.page.locator("form").filter(has_text=self.__set_time).get_by_role("textbox").nth(1).fill(value)

    @allure.step("点击灯光开关")
    def click_light_switch(self):
        self.page.locator(self.__light_switch).click()

    @allure.step("设置灯光时间")
    def set_light_time(self, value):
        self.page.locator("form").filter(has_text=self.__set_time).get_by_role("textbox").nth(2).fill(value)

    @allure.step("点击报警输出开关")
    def click_alarm_output_switch(self):
        self.page.locator(self.__output_switch).click()

    @allure.step("设置报警输出时间")
    def set_alarm_output_time(self, value):
        self.page.locator("form").filter(has_text=self.__set_time).get_by_role("textbox").nth(3).fill(value)

    @allure.step("点击默认")
    def click_default(self):
        self.page.get_by_role("button", name="默认").click()

    @allure.step("点击刷新")
    def click_refresh(self):
        self.page.get_by_role("button", name="刷新").click()

    @allure.step("点击确定")
    def click_ok(self):
        self.page.get_by_role("button", name="确定").click()
























