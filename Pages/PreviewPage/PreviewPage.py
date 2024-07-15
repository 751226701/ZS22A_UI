#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: 刘涛
# @time: 2024/1/17 9:57
# @file: PreviewPage.py
# @project: ZS22A_UI

import os.path
import re
import allure
from time import sleep
from Common.Common import Common
from Config.Config import Config
from Common.CompareImage import download_image
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
    __electronic_amplification = ("list", "i")
    __real_time_temp_curve = ".el-tooltip.icon-report"
    __object_temp_select = ("请选择", 1)
    __object_temp_max = "最高温"
    __object_temp_min = "最低温"
    __object_temp_avg = "平均温"
    __time_range_select = "请选择"
    __time_range_24H = "近24小时"
    __time_range_72H = "近72小时"
    __time_range_4H = "近4小时"
    __fill_or_adapt = ".el-tooltip.icon-videomode"
    __full_screen = ".el-tooltip.icon-full"
    __vl_full_screen = ".video-wrap > canvas"
    __ir_full_screen = ".show_window_ir > .video-wrap > canvas"
    __full_screen_exit = ".video-wrap > canvas"
    __full_screen_exit_ir = ".show_window_ir > .video-wrap > canvas"
    __root = ("button", "root")
    __logout = "退出登录"
    __confirm_exit = ("button", "确认退出")

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

    @allure.step("断言红外通道开始录制成功")
    def assert_start_ir_record(self, value):
        expect(self.page.locator(value[0]).first).to_be_visible()

    @allure.step("断言可见光通道开始录制成功")
    def assert_start_vl_record(self, value):
        expect(self.page.locator(value[1]).first).to_be_visible()

    @allure.step("点击停止录制")
    def click_stop_record(self):
        self._click(self.__stop_record)

    @allure.step("断言红外通道已停止录制")
    def assert_stop_ir_record(self, value):
        expect(self.page.locator(value[0]).first).to_be_hidden()

    @allure.step("断言可见光通道已停止录制")
    def assert_stop_vl_record(self, value):
        expect(self.page.locator(value[1]).first).to_be_hidden()

    @allure.step("点击连续抓图")
    def click_continuous_snapshot(self):
        self._click(self.__continuous_snapshot)

    @allure.step("断言连续抓图成功")
    def assert_continuous_snapshot(self, value):
        expect(self.page.get_by_text(value)).to_be_visible(timeout=300000)

    @allure.step("点击自动聚焦")
    def click_auto_focus(self):
        self._click(self.__auto_focus)

    @allure.step("断言自动聚焦成功")
    def assert_auto_focus(self, value):
        expect(self.page.get_by_text(value)).to_be_visible()

    @allure.step("点击电子变倍")
    def click_electronic_amplification(self):
        self.page.get_by_role("list").locator("i").first.click()

    @allure.step("断言电子变倍成功")
    def assert_electronic_amplification(self, elem, types, value,):
        """
        :param elem: 定位元素
        :param types: 比较类型：1大于 2小于 3等于
        :param value: 比较阈值
        :return:
        """
        global a
        video_wrap = self.page.query_selector(elem)
        transform = video_wrap.evaluate("element => window.getComputedStyle(element).transform")
        matrix_pattern = r'matrix\(([^)]+)\)'
        match = re.search(matrix_pattern, transform)
        if match:
            matrix_values = match.group(1).split(',')
            if len(matrix_values) == 6:
                a = float(matrix_values[0].strip())
                b = float(matrix_values[1].strip())
                c = float(matrix_values[2].strip())
                d = float(matrix_values[3].strip())
                tx = float(matrix_values[4].strip())
                ty = float(matrix_values[5].strip())
        print(a)
        print(types)
        if types == 1:
            assert a > value
        if types == 2:
            assert a < value
        elif types == 3:
            assert a == value

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

    @allure.step("断言已全屏显示")
    def assert_full_screen(self, value, types):
        """
        :param value: 视频窗口元素定位
        :param types: 比例类型 1大于 2等于
        :return:
        """
        height = self.page.query_selector(value).evaluate("element => element.getBoundingClientRect().height")
        print(height)
        if types == 1:
            assert height > 721
        if types == 2:
            assert height == 721

    @allure.step("可见光全屏显示")
    def click_vl_full_screen(self):
        self.page.locator(self.__vl_full_screen).first.dblclick(position={"x": 345, "y": 156})

    @allure.step("红外全屏显示")
    def click_ir_full_screen(self):
        self.page.locator(self.__ir_full_screen).dblclick(position={"x": 293, "y": 236})

    @allure.step("退出全屏显示")
    def click_full_screen_exit(self):
        self.page.locator(self.__full_screen_exit).first.dblclick()

    @allure.step("退出单可见光全屏显示")
    def click_vl_full_screen_exit(self):
        self.page.locator(self.__full_screen_exit).first.dblclick()

    @allure.step("退出单红外全屏显示")
    def click_ir_full_screen_exit(self):
        self.page.locator(self.__full_screen_exit_ir).first.dblclick()

    @allure.step("点击admin用户")
    def click_admin(self):
        self.page.get_by_role("button", name="admin").click()

    @allure.step("退出登录")
    def click_logout(self):
        self.page.get_by_text(self.__logout).click()

    @allure.step("确认退出")
    def click_confirm_exit(self):
        self.page.get_by_role("button", name="确认退出").click()

    @allure.step("断言退出登录成功")
    def assert_logout_success(self, value):
        expect(self.page.get_by_placeholder(value)).to_be_visible()

    @allure.step("播放暂停按钮悬浮")
    def hover_video_stop(self):
        self.page.locator(".el-tooltip").first.hover()

    @allure.step("抓图按钮悬浮")
    def hover_screenshot(self):
        self.page.locator("i:nth-child(2)").hover()

    @allure.step("开始录像按钮悬浮文字")
    def hover_start_record(self):
        self.page.locator(".btn-opr > i:nth-child(3)").hover()

    @allure.step("停止录像按钮悬浮文字")
    def hover_stop_record(self):
        self.page.locator(".btn-opr > i:nth-child(3)").hover()

    @allure.step("连续抓图按钮悬浮文字")
    def hover_continuous_snapshot(self):
        self.page.locator("i:nth-child(4)").hover()

    @allure.step("局部放大按钮悬浮文字")
    def hover_electronic_amplification(self):
        self.page.get_by_role("list").locator("i").first.hover()

    @allure.step("实时温度曲线按钮悬浮文字")
    def hover_real_time_temp_curve(self):
        self.page.get_by_role("list").locator("i").nth(1).hover()

    @allure.step("窗口适应按钮悬浮文字")
    def hover_adapt_screen(self):
        self.page.get_by_role("list").locator("i").nth(2).hover()

    @allure.step("窗口填充按钮悬浮文字")
    def hover_fill_screen(self):
        self.page.get_by_role("list").locator("i").nth(2).hover()

    @allure.step("全屏按钮悬浮文字")
    def hover_full_screen(self):
        self.page.get_by_role("list").locator("i").nth(3).hover()

    @allure.step("断言按钮悬浮文字")
    def assert_float_text(self, value):
        expect(self.page.get_by_text(value, exact=True)).to_be_visible()

    @allure.step("断言已选中可见光通过")
    def assert_vl_pass(self, value):
        ele = self.page.locator(".left-wrap").get_attribute("class")
        assert value in ele

    @allure.step("点击可见光窗口")
    def click_vl_window(self):
        self.page.locator(".video-wrap > canvas").first.click()

    @allure.step("点击红外窗口")
    def click_ir_window(self):
        self.page.locator(".show_window_ir > .video-wrap > canvas").click()

    @allure.step("切换至回放管理")
    def goto_playback_management(self):
        self.page.get_by_text("回放管理").click()

    @allure.step("切换至实时预览")
    def goto_real_time_preview(self):
        self.page.get_by_text("实时预览").click()

    @allure.step("点击登录按钮")
    def click_login_button(self):
        sleep(4)
        self.page.get_by_role("button", name="登录").click()







