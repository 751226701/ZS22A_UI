# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/3/4 13:25
# @File :AlarmPage1.py
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

class AlarmPage(Common):

    # 全局温度子模块元素定位
    __global_high_temp_box = ".el-checkbox__inner"
    __global_high_temp_value = "div:nth-child(4) > .el-input__inner"
    __global_high_temp_select = "请选择"
    __global_low_temp_box = "div:nth-child(6) > .el-checkbox > .el-checkbox__input > .el-checkbox__inner"
    __global_low_temp_value = "div:nth-child(6) > div:nth-child(4) > .el-input__inner"
    __global_low_temp_select = "请选择"
    __select_great = ("list", ">")
    __select_less = ("list", "<")
    __debounce = ("div", r"^去抖动 s \(1~10\)$", "textbox")
    __alarm_interval_time_select = ("div", r"^报警间隔时间30s 60s 5min 10min 15min 30min 60min$|^报警间隔时间$", "请选择")
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
    __audio_switch = "div:nth-child(4) > .el-form-item__content > .el-switch > .el-switch__core"
    __audio_time = "录像可见光录像 红外录像 录像时间 s(10~300"
    __light_switch = "div:nth-child(4) > .el-form-item__content > .el-switch > .el-switch__core"
    __alarm_output = "div:nth-child(6) > .el-form-item__content > .el-switch > .el-switch__core"
    __output_time = "录像可见光录像 红外录像 录像时间 s(10~300"
    __duration = ("form", "录像可见光录像 红外录像 录像时间 s(10~300", "textbox")
    __default = "默认"
    __refresh = "刷新"
    __ok = "确定"

    # 全局温度子模块方法
    @allure.step("点击全局最高温复选框")
    def click_global_high_temp_box(self):
        self.page.locator(self.__global_high_temp_box).first.click()

    @allure.step("断言全局高温复选框是否选中")
    def assert_global_high_temp_box(self, value):
        """
        断言全局高温复选框是否选中
        :param value: 1 选中 2 未选中
        """
        sleep(1)
        if value == 1:
            expect(self.page.locator(self.__global_high_temp_box).first).to_be_checked()
        elif value == 2:
            expect(self.page.locator(self.__global_high_temp_box).first).not_to_be_checked()

    @allure.step("点击全局最低温复选框")
    def click_global_low_temp_box(self):
        self.page.locator(self.__global_low_temp_box).click()

    @allure.step("断言全局低温复选框是否选中")
    def assert_global_low_temp_box(self, value):
        """
        断言全局高温复选框是否选中
        :param value: 1 选中 2 未选中
        """
        sleep(1)
        if value == 1:
            expect(self.page.locator(self.__global_low_temp_box).first).to_be_checked()
        elif value == 2:
            expect(self.page.locator(self.__global_low_temp_box).first).not_to_be_checked()

    @allure.step("全局最高温报警条件选择")
    def global_high_temp_select(self):
        self.page.get_by_placeholder(self.__global_high_temp_select).first.click()

    @allure.step("全局最低温报警条件选择")
    def global_low_temp_select(self):
        self.page.get_by_placeholder(self.__global_low_temp_select).nth(1).click()

    @allure.step("设置高温报警阈值")
    def set_global_high_temp_value(self, value):
        self.page.locator(self.__global_high_temp_value).first.fill(value)

    @allure.step("断言高温报警阈值")
    def assert_global_high_temp_value(self, value):
        expect(self.page.locator(self.__global_high_temp_value).first).to_have_value(value)

    @allure.step("设置低温报警阈值")
    def set_global_low_temp_value(self, value):
        self.page.locator(self.__global_low_temp_value).fill(value)

    @allure.step("断言低温报警阈值")
    def assert_global_low_temp_value(self, value):
        expect(self.page.locator(self.__global_low_temp_value)).to_have_value(value)

    @allure.step("选择大于")
    def select_great(self):
        self.page.get_by_role("list").get_by_text(self.__select_great[1]).click()

    @allure.step("选择小于")
    def select_less(self):
        self.page.get_by_role("list").get_by_text(self.__select_less[1]).click()

    @allure.step("断言高温报警条件")
    def assert_high_alarm_condition(self, value):
        expect(self.page.get_by_placeholder("请选择").first).to_have_value(value)

    @allure.step("断言低温报警条件")
    def assert_low_alarm_condition(self, value):
        expect(self.page.get_by_placeholder("请选择").nth(1)).to_have_value(value)

    @allure.step("设置去抖动")
    def set_debounce_value(self, value):
        (self.page.locator("div").filter(has_text=re.compile(r"^去抖动 s \(0~10\)$")).
         get_by_role("textbox").fill(value))

    @allure.step("断言去抖动值")
    def assert_debounce_value(self, value):
        expect(self.page.locator("div").filter(has_text=re.compile(r"^去抖动 s \(0~10\)$")).
               get_by_role("textbox")).to_have_value(value)

    @allure.step("设置报警间隔时间")
    def set_alarm_interval_time(self):
        (self.page.locator(self.__alarm_interval_time_select[0]).
         filter(has_text=re.compile(self.__alarm_interval_time_select[1])).
         get_by_placeholder(self.__alarm_interval_time_select[2]).click())

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

    @allure.step("断言报警间隔时间")
    def assert_alarm_interval_time(self, value):
        has_text = re.compile(r"^报警间隔时间*")
        expect(self.page.locator("div").filter(has_text=re.compile(has_text)).
               get_by_placeholder("请选择")).to_have_value(value)

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

    @allure.step("点击邮件通知开关")
    def click_email_switch(self):
        (self.page.locator(self.__email_switch[0]).filter(has_text=re.compile(self.__email_switch[1])).
         locator(self.__email_switch[2]).click())

    @allure.step("点击音频播放开关")
    def click_audio_switch(self):
        self.page.locator(self.__audio_switch).click()

    @allure.step("设置音频播放时间")
    def set_audio_time(self, value):
        self.page.locator("form").filter(has_text=self.__audio_time).get_by_role("textbox").nth(1).fill("25")

    @allure.step("点击灯光开关")
    def click_light_switch(self):
        self._click(self.__light_switch)

    @allure.step("设置灯光持续时间")
    def set_duration(self, value):
        (self.page.locator(self.__duration[0]).filter(has_text=self.__duration[1]).
         get_by_role("textbox").nth(1).fill(value))

    @allure.step("点击报警输出开关")
    def click_alarm_output_switch(self):
        self.page.locator(self.__alarm_output).click()

    @allure.step("设置报警输出时间")
    def set_alarm_output_time(self, value):
        self.page.locator("form").filter(has_text=self.__output_time).get_by_role("textbox").nth(3).fill("25")

    @allure.step("点击默认")
    def click_default(self):
        self.page.get_by_role("button", name=self.__default).click()

    @allure.step("点击刷新")
    def click_refresh(self):
        self.page.get_by_role("button", name=self.__refresh).click()

    @allure.step("点击确定")
    def click_ok(self):
        self.page.get_by_role("button", name=self.__ok).click()

    @allure.step("断言是否产生报警")
    def assert_alarm(self, value):
        expect(self.page.locator(value)).to_be_visible()


















































































