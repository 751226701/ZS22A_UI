# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/3/6 10:02
# @File :AlarmPage2.py
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
    # 分析对象子模块元素定位
    __point = ".el-tooltip"
    __line = "i:nth-child(2)"
    __circle = ".video-head-i > i:nth-child(3)"
    __rectangle = "i:nth-child(4)"
    __polygon = "i:nth-child(5)"
    __brush = ".video-main > canvas"
    __vl_record_box = ("label", "可见光录像", "span", 1)
    __ir_record_box = ("label", "红外录像", "span", 1)
    __record_time = ("报警联动设置", "form div", "录像可见光录像 红外录像 录像时间 s(10~300)", "textbox")
    __vl_capture_box = ("label", "可见光抓图", "span", 1)
    __ir_capture_box = ("label", "红外抓图", "span", 1)
    __email_switch = ("div", r"^邮件通知$", "span")
    __light_switch = ".el-switch__core"
    __duration = ("报警联动设置", "form div", "灯光 持续时间 s(10~300)", "textbox")
    __object_list_all = ("row", "序号 名称 最高温 最低温 平均温", "span", 1)
    __sync_config = "同步配置"
    __delete = "删除"
    __confirm = ("删除", "确定")
    __cancel = "取消"
    __obj_name = ".el-col > .el-form-item > .el-form-item__content > .el-input > .el-input__inner"
    __select_show = "分析对象详情(123)"
    __show_max_temp = "最高温"
    __show_min_temp = "最低温"
    __show_avg_temp = "平均温"
    __show_name = "仅名称"
    __show_name_max = "名称+最高温"
    __show_name_min = "名称+最低温"
    __show_name_avg = "名称+平均温"
    __show_none = "不显示"
    __select_display_pos = "分析对象详情(123)"
    __up = "上方"
    __down = "下方"
    __left = "左方"
    __right = "右方"
    __mid = "中间"
    __emiss = ".el-form-item__content > div:nth-child(2) > .el-input > .el-input__inner"
    __distance = "div:nth-child(5) > .el-form-item > .el-form-item__content > .el-input > .el-input__inner"
    __ref_temp = "div:nth-child(6) > .el-form-item > .el-form-item__content > .el-input > .el-input__inner"
    __alarm_enable = ("报警参数设置", "switch", "span")
    __alarm_temp_select = ("报警参数设置", "i")
    __max_temp_alarm = "最高温"
    __min_temp_alarm = "最低温"
    __avg_temp_alarm = "平均温"
    __temp_raise_alarm = "温升"
    __temp_diff_alarm = "温差"
    __select_alarm_condition = ("报警参数设置", "i", 1)
    __select_great = ">"
    __select_less = "<"
    __temp_threshold = ("报警参数设置", "textbox", 2)
    __debounce = ("报警参数设置", "textbox", 3)
    __alarm_interval_time = ("报警参数设置", "请选择", 2)
    __alarm_interval_time_30S = "30s"
    __alarm_interval_time_60S = "60s"
    __alarm_interval_time_5min = "5min"
    __alarm_interval_time_10min = "10min"
    __alarm_interval_time_15min = "15min"
    __alarm_interval_time_30min = "30min"
    __alarm_interval_time_60min = "60min"
    __default = "默认"
    __refresh = "刷新"
    __ok = "确定"

    @allure.step("选择点分析对象画笔")
    def select_point_brush(self):
        self.page.locator(self.__point).first.click()

    @allure.step("选择线分析对象画笔")
    def select_line_brush(self):
        self.page.locator(self.__line).first.click()

    @allure.step("选择圆分析对象画笔")
    def select_circle_brush(self):
        self.page.locator(self.__circle).click()

    @allure.step("选择矩形分析对象画笔")
    def select_rectangle_brush(self):
        self.page.locator(self.__rectangle).first.click()

    @allure.step("选择多边形分析对象画笔")
    def select_polygon_brush(self):
        self.page.locator(self.__polygon).first.click()

    @allure.step("使可以画分析对象")
    def draw_object_on(self):
        """
        添加分析对象之前，先调用此接口；（概率性进入分析对象页面无法定位到视频画面）
        :return: 无
        """
        element = self.page.locator(self.__brush)
        while True:
            sleep(1)
            if element.is_visible():
                # print("可以画分析对象")
                break
            else:
                # print("不能画分析对象，切换页面")
                self.page.get_by_role("menuitem", name="全局温度").click()
                self.page.get_by_role("menuitem", name="分析对象").click()

    @allure.step("画分析对象")
    def draw_object(self, x, y):
        """
        根据分析对象类型确定调用次数
        点：一次
        线，圆，矩形：两次
        多边形：七次
        :param x: 横坐标
        :param y: 纵坐标
        :return: 无
        """
        self.page.locator(self.__brush).click(position={"x": x, "y": y})

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
        (self.page.get_by_label(self.__record_time[0]).
         locator(self.__record_time[1]).
         filter(has_text=self.__record_time[2]).
         get_by_role("textbox").fill(value))

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
        (self.page.get_by_label("报警联动设置").locator("form div").
         filter(has_text="音频播放 持续时间 s(10~300)").get_by_role("switch").locator("span").click())

    @allure.step("设置音频播放时间")
    def set_audio_time(self, value):
        (self.page.get_by_label("报警联动设置").locator("form div").
         filter(has_text="音频播放 持续时间 s(10~300)").get_by_role("textbox").fill("99"))

    @allure.step("点击灯光开关")
    def click_light_switch(self):
        self.page.locator(self.__light_switch).nth(1).click()

    @allure.step("设置灯光持续时间")
    def set_light_duration(self, value):
        (self.page.get_by_label("报警联动设置").
         locator("form div").filter(has_text="灯光 持续时间 s(10~300)").
         get_by_role("textbox").fill(value))

    @allure.step("点击报警输出开关")
    def click_alarm_output_switch(self):
        (self.page.get_by_label("报警联动设置").locator("form div").
         filter(has_text="报警输出 持续时间 s(10~300)").get_by_role("switch").locator("span").click())

    @allure.step("设置报警输出时间")
    def set_alarm_output_time(self, value):
        (self.page.get_by_label("报警联动设置").locator("form div").
         filter(has_text="报警输出 持续时间 s(10~300)").get_by_role("textbox").fill(value))

    @allure.step("分析对象列表全选框")
    def object_list_all(self):
        self.page.get_by_role("row", name = self.__object_list_all[1]).locator("span").nth(1).click()

    @allure.step("同步配置")
    def sync_config(self):
        self.page.get_by_role("button", name=self.__sync_config).click()

    @allure.step("删除")
    def delete(self):
        self.page.get_by_role("button", name=self.__delete).click()

    @allure.step("确定删除")
    def delete_confirm(self):
        (self.page.get_by_label(self.__confirm[0]).
         get_by_role("button", name=self.__confirm[1]).click())

    @allure.step("取消删除")
    def delete_cancel(self):
        self.page.get_by_role("button", name=self.__cancel).click()

    @allure.step("设置分析对象名称")
    def set_obj_name(self, value):
        self.page.locator(self.__obj_name).first.fill(value)

    @allure.step("选择显示内容")
    def select_show(self):
        self.page.get_by_label(self.__select_show).locator("i").first.click()

    @allure.step("选择最高温")
    def select_show_max_temp(self):
        self.page.get_by_role("list").get_by_text("最高温", exact=True).click()

    @allure.step("选择最低温")
    def select_show_min_temp(self):
        self.page.get_by_role("list").get_by_text("最低温", exact=True).click()

    @allure.step("选择平均温")
    def select_show_avg_temp(self):
        self.page.get_by_role("list").get_by_text("平均温", exact=True).click()

    @allure.step("仅名称")
    def select_show_name(self):
        self.page.get_by_text(self.__show_name).click()

    @allure.step("名称+最高温")
    def select_show_name_max_temp(self):
        self.page.get_by_text(self.__show_name_max).click()

    @allure.step("名称+最低温")
    def select_show_name_min_temp(self):
        self.page.get_by_text(self.__show_name_min).click()

    @allure.step("名称+平均温")
    def select_show_name_avg_temp(self):
        self.page.get_by_text(self.__show_name_avg).click()

    @allure.step("不显示")
    def select_show_none(self):
        self.page.get_by_text(self.__show_none).click()

    @allure.step("选择显示方位")
    def select_show_position(self):
        self.page.get_by_label(self.__select_display_pos).locator("i").nth(1).click()

    @allure.step("选择左方")
    def select_left(self):
        self.page.get_by_text(self.__left).click()

    @allure.step("选择右方")
    def select_right(self):
        self.page.get_by_text(self.__right).click()

    @allure.step("选择上方")
    def select_up(self):
        self.page.get_by_text(self.__up).click()

    @allure.step("选择下方")
    def select_down(self):
        self.page.get_by_text(self.__down).click()

    @allure.step("选择中间")
    def select_mid(self):
        self.page.get_by_text(self.__mid).click()

    @allure.step("设置发射率")
    def set_emiss(self, value):
        self.page.locator(self.__emiss).first.fill(value)

    @allure.step("设置距离")
    def set_distance(self, value):
        self.page.locator(self.__distance).fill(value)

    @allure.step("设置反射温度")
    def set_reflect_temp(self, value):
        self.page.locator(self.__ref_temp).fill(value)

    @allure.step("报警配置开关")
    def alarm_switch(self):
        self.page.get_by_label("报警参数设置").get_by_role("switch").locator("span").click()

    @allure.step("报警类型选择")
    def alarm_type_select(self):
        self.page.get_by_label("报警参数设置").locator("i").first.click()

    @allure.step("高温报警")
    def max_temp_alarm(self):
        self. page.get_by_role("list").get_by_text(self.__max_temp_alarm).click()

    @allure.step("低温报警")
    def min_temp_alarm(self):
        self.page.get_by_role("list").get_by_text(self.__min_temp_alarm).click()

    @allure.step("平均温报警")
    def avg_temp_alarm(self):
        self.page.get_by_role("list").get_by_text(self.__avg_temp_alarm).click()

    @allure.step("温升报警")
    def temp_rise_alarm(self):
        self. page.get_by_text(self.__temp_raise_alarm).click()

    @allure.step("温差报警")
    def temp_diff_alarm(self):
        self.page.get_by_text(self.__temp_diff_alarm, exact=True).click()

    @allure.step("选择报警条件")
    def select_alarm_condition(self):
        self.page.get_by_label("报警参数设置").locator("i").nth(1).click()

    @allure.step("选择大于")
    def select_great(self):
        self.page.locator("li").filter(has_text=">").click()

    @allure.step("选择小于")
    def select_less(self):
        self.page.locator("li").filter(has_text="<").click()

    @allure.step("设置温度阈值")
    def set_temp_threshold(self, value):
        self.page.get_by_label("报警参数设置").get_by_role("textbox").nth(2).fill(value)

    @allure.step("设置去抖动时间")
    def set_debounce_time(self, value):
        self.page.get_by_label("报警参数设置").get_by_role("textbox").nth(3).fill(value)

    @allure.step("选择报警间隔时间")
    def select_alarm_interval_time(self):
        self. page.get_by_label("报警参数设置").get_by_placeholder("请选择").nth(2).click()

    @allure.step("选择30s")
    def select_30s(self):
        self. page.get_by_text("30s").click()

    @allure.step("选择60s")
    def select_60s(self):
        self.page.get_by_text("60s").click()

    @allure.step("选择5min")
    def select_5min(self):
        self.page.get_by_text("5min", exact=True).click()

    @allure.step("选择10min")
    def select_10min(self):
        self.page.get_by_text("10min").click()

    @allure.step("选择15min")
    def select_15min(self):
        self.page.get_by_text("15min").click()

    @allure.step("选择30min")
    def select_30min(self):
        self.page.get_by_text("30min").click()

    @allure.step("选择60min")
    def select_60min(self):
        self.page.get_by_text("60min").click()

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


















































































































