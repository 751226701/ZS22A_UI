# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/3/18 10:17
# @File :AlarmPage4.py
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
    # 存储异常子模块元素定位
    __audio_switch = "div:nth-child(2) > .el-form-item__content > .el-switch > .el-switch__core"
    __light_switch = "div:nth-child(3) > .el-form-item__content > .el-switch > .el-switch__core"
    __output_switch = "div:nth-child(4) > .el-form-item__content > .el-switch > .el-switch__core"

    @allure.step("报警启用状态开关")
    def alarm_switch(self):
        self.page.locator("div").filter(has_text=re.compile(r"^启用状态$")).locator("span").click()

    @allure.step("报警间隔时间选择")
    def alarm_interval(self):
        self.page.get_by_placeholder("请选择").click()

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

    @allure.step("点击邮件通知开关")
    def click_email_switch(self):
        self.page.locator("div").filter(has_text=re.compile(r"^邮件通知$")).locator("span").click()

    @allure.step("点击音频播放开关")
    def click_audio_switch(self):
        self.page.locator(self.__audio_switch).click()

    @allure.step("设置音频播放时间")
    def set_audio_time(self, value):
        self. page.get_by_role("textbox").nth(2).fill(value)

    @allure.step("点击灯光开关")
    def click_light_switch(self):
        self.page.locator(self.__light_switch).click()

    @allure.step("设置灯光时间")
    def set_light_time(self, value):
        self.page.get_by_role("textbox").nth(3).fill(value)

    @allure.step("点击报警输出开关")
    def click_alarm_output_switch(self):
        self.page.locator(self.__output_switch).click()

    @allure.step("设置报警输出时间")
    def set_alarm_output_time(self, value):
        self.page.get_by_role("textbox").nth(4).fill(value)

    @allure.step("切换至FTP异常页面")
    def switch_ftp_page(self):
        self.page.get_by_role("tab", name="FTP异常").click()

    @allure.step("切换至SD卡异常页面")
    def switch_sd_page(self):
        self.page.get_by_role("tab", name="SD卡异").click()

    """
    set_audio_time
    set_light_time
    set_alarm_output_time
    上面的这三个方法不能在FTP异常页面和SD卡异常页面使用
    FTP异常页面和SD卡异常页面在下面重新封装设置时间的方法
    """

    @allure.step("设置音频播放时间")
    def set_audio_time1(self, value):
        self.page.get_by_role("textbox").nth(1).fill(value)

    @allure.step("设置灯光时间")
    def set_light_time1(self, value):
        self.page.get_by_role("textbox").nth(2).fill(value)

    @allure.step("设置报警输出时间")
    def set_alarm_output_time1(self, value):
        self.page.get_by_role("textbox").nth(3).fill(value)

    @allure.step("点击默认")
    def click_default(self):
        self.page.get_by_role("button", name="默认").click()

    @allure.step("点击刷新")
    def click_refresh(self):
        self.page.get_by_role("button", name="刷新").click()

    @allure.step("点击确定")
    def click_ok(self):
        self.page.get_by_role("button", name="确定").click()














































































