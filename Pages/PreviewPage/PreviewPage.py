#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: 刘涛
# @time: 2024/1/17 9:57
# @file: PreviewPage.py
# @project: ZS22A_UI

import os.path
import allure
from time import sleep
from Common.Common import Common
from Config.Config import Config
from Common.CompareImage import are_images_equal, download_image
from playwright.sync_api import expect


class PreviewPage(Common):
    __video_start = ".el-tooltip"
    __video_stop = ".el-tooltip"
    __screenshot = "i:nth-child(2)"
    __screenshot_close = ".el-icon-circle-close"
    __start_record = ".btn-opr > i:nth-child(3)"
    __stop_record = ".btn-opr > i:nth-child(3)"
    __continuous_snapshot = "i:nth-child(4)"
    __auto_focus = "li > .el-tooltip"
    __electronic_amplification = ("li", "1X 4X 16X", "i", 2)
    __select_1X = ("li", "1X", 2)
    __select_2X = "2X"
    __select_3X = ("li", "3X")
    __real_time_temp_curve = "li:nth-child(3) > .el-tooltip"
    __object_temp_select = ("请选择", 1)
    __object_temp_max = "最高温"
    __object_temp_min = "最低温"
    __object_temp_avg = "平均温"
    __time_range_select = "请选择"
    __time_range_24H = "近24小时"
    __time_range_72H = "近72小时"
    __time_range_4H = "近4小时"
    __fill_or_adapt = "li:nth-child(4) > .el-tooltip"
    __full_screen = "li:nth-child(5) > .el-tooltip"
    __full_screen_exit = ".video-wrap > canvas"

    @allure.step("点击暂停播放")
    def click_video_stop(self):
        sleep(1)
        self._click(self.__video_stop)

    @allure.step("断言暂停播放")
    def assert_video_stop(self, value):
        expect(self.page.locator(value[0])).to_contain_text(value[1])

    @allure.step("点击开始播放")
    def click_video_start(self):
        self._click(self.__video_stop)

    @allure.step("断言开始播放")
    def assert_video_start(self, value):
        expect(self.page.locator(value[0])).to_contain_text(value[1])

    @allure.step("点击抓图")
    def click_screenshot(self):
        self._click(self.__screenshot)

    @allure.step("断言抓图成功")
    def assert_click_screenshot(self, value):
        expect(self.page.locator(value)).to_be_visible()

    @allure.step("点击关闭抓图框")
    def click_screenshot_close(self):
        self._click(self.__screenshot_close)

    @allure.step("断言关闭抓图框成功")
    def assert_click_screenshot_close(self, value):
        expect(self.page.locator(value)).to_be_hidden()

    @allure.step("点击开始录制")
    def click_start_record(self):
        self._click(self.__start_record)

    @allure.step("断言开始录制成功")
    def assert_start_record(self, value):
        expect(self.page.locator(value)).to_be_visible()

    @allure.step("点击停止录制")
    def click_stop_record(self):
        self._click(self.__stop_record)

    @allure.step("断言停止录制成功")
    def assert_stop_record(self, value):
        expect(self.page.get_by_text(value)).to_be_visible()

    @allure.step("点击连续抓图")
    def click_continuous_snapshot(self):
        self._click(self.__continuous_snapshot)

    @allure.step("断言连续抓图成功")
    def assert_continuous_snapshot(self, value):
        expect(self.page.get_by_text(value)).to_be_visible()

    @allure.step("点击自动聚焦")
    def click_auto_focus(self):
        self._click(self.__auto_focus)

    @allure.step("断言自动聚焦成功")
    def assert_auto_focus(self, value):
        expect(self.page.get_by_text(value)).to_be_visible()

    @allure.step("点击电子变倍")
    def click_electronic_amplification(self):
        (self.page.locator(self.__electronic_amplification[0]).
         filter(has_text=self.__electronic_amplification[1]).
         locator(self.__electronic_amplification[2]).
         nth(self.__electronic_amplification[3]).click())

    @allure.step("选择电子变倍1X")
    def select_electronic_amplification_1X(self):
        (self.page.locator(self.__select_1X[0]).
         filter(has_text=self.__select_1X[1]).
         nth(self.__select_1X[2]).click())

    @allure.step("选择电子变倍2X")
    def select_electronic_amplification_2X(self):
        self.page.get_by_text(self.__select_2X).click()

    @allure.step("选择电子变倍3X")
    def select_electronic_amplification_3X(self):
        (self.page.locator(self.__select_3X[0]).
         filter(has_text=self.__select_3X[1]).click())

    @allure.step("断言电子变倍成功")
    def assert_electronic_amplification(self, value):
        expect(self.page.get_by_role("textbox", name="请选择")).to_have_value(value)

    @allure.step("点击实时温度曲线")
    def click_real_time_temp_curve(self):
        self._click(self.__real_time_temp_curve)

    @allure.step("断言打开实时温度曲线成功")
    def assert_real_time_temp_curve_start(self, value):
        expect(self.page.locator(value)).to_be_visible()

    @allure.step("点击选择对象温度")
    def click_object_temp_select(self):
        self.page.get_by_placeholder(self.__object_temp_select[0]).nth(self.__object_temp_select[1]).click()

    @allure.step("选择对象温度最高温")
    def select_object_temp_max(self):
        self.page.get_by_text(self.__object_temp_max).click()

    @allure.step("选择对象温度最低温")
    def select_object_temp_mix(self):
        self.page.get_by_text(self.__object_temp_min).click()

    @allure.step("选择对象温度平均温")
    def select_object_temp_avg(self):
        self.page.get_by_text(self.__object_temp_avg).click()

    @allure.step("断言选择对象温度成功")
    def assert_select_object_temp_success(self, value):
        expect(self.page.get_by_placeholder("请选择").nth(1)).to_have_value(value)

    @allure.step("点击选择时间范围")
    def click_time_range_select(self):
        self.page.get_by_placeholder(self.__time_range_select).first.click()

    @allure.step("选择时间范围4小时")
    def select_time_range_4H(self):
        self.page.get_by_text(self.__time_range_4H).click()

    @allure.step("选择时间范围24小时")
    def select_time_range_24H(self):
        self.page.get_by_text(self.__time_range_24H).click()

    @allure.step("选择时间范围72小时")
    def select_time_range_72H(self):
        self.page.get_by_text(self.__time_range_72H).click()

    @allure.step("断言选择时间范围切换成功")
    def assert_select_time_range_success(self, value):
        expect(self.page.get_by_placeholder("请选择").first).to_have_value(value)

    @allure.step("断言关闭实时温度曲线成功")
    def assert_real_time_temp_curve_stop(self, value):
        expect(self.page.locator(value)).to_be_hidden()

    @allure.step("点击填充或适应")
    def click_fill_or_adapt(self):
        self._click(self.__fill_or_adapt)

    @allure.step("断言填充或适应成功")
    def assert_fill_or_adapt(self, value):
        expect(self.page.get_by_text(value)).to_be_visible()

    @allure.step("全屏显示")
    def click_full_screen(self):
        self._click(self.__full_screen)

    @allure.step("退出全屏显示")
    def click_full_screen_exit(self):
        self.page.locator(self.__full_screen_exit).dblclick()























































