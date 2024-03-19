# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/3/19 10:36
# @File :SystemPage1
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

class SystemPage(Common):
    # 画面设置子模块元素定位
    __ir = "亮度 % 对比度 % 锐度 % 自动快门补偿间隔 分钟 ("
    __shutter = r"^自动快门补偿间隔 分钟 \(1-20\)$"
    __rotate = "亮度 % 对比度 % 锐度 % 自动快门补偿间隔 分钟 ("
    __detail = "form:nth-child(2) > div > .el-form-item__content > .el-switch > .el-switch__core"
    __space_noise = "div:nth-child(2) > .el-form-item__content > .el-switch > .el-switch__core"
    __time_noise = "div:nth-child(3) > .el-form-item__content > .el-switch > .el-switch__core"
    __value = "细节增强 % 空域降噪 % 时域降噪 %"

    @allure.step("设置可见光亮度")
    def set_vl_light(self, value):
        (self.page.get_by_label("可见光画面设置").locator("form div").
         filter(has_text="亮度 %").get_by_role("textbox").fill(value))

    @allure.step("设置可见光对比度")
    def set_vl_contrast(self, value):
        (self.page.get_by_label("可见光画面设置").locator("form div").
         filter(has_text="对比度 %").get_by_role("textbox").fill(value))

    @allure.step("设置可见光饱和度")
    def set_vl_saturation(self, value):
        (self.page.get_by_label("可见光画面设置").locator("form div").
         filter(has_text="饱和度 %").get_by_role("textbox").fill(value))

    @allure.step("设置可见光锐度")
    def set_vl_sharpness(self, value):
        (self.page.get_by_label("可见光画面设置").locator("form div").
         filter(has_text="锐度 %").get_by_role("textbox").fill(value))

    @allure.step("背光补偿选择")
    def set_backlight_compensation(self):
        self.page.get_by_placeholder("请选择").click()

    @allure.step("选择关闭")
    def select_close(self):
        self.page.get_by_text("关闭").click()

    @allure.step("选择上")
    def select_up(self):
        self.page.get_by_text("上").click()

    @allure.step("选择下")
    def select_down(self):
        self.page.get_by_text("下").click()

    @allure.step("选择左")
    def select_left(self):
        self.page.get_by_text("左").click()

    @allure.step("选择右")
    def select_right(self):
        self.page.get_by_text("右").click()

    @allure.step("选择中心")
    def select_center(self):
        self.page.get_by_text("中心").click()

    @allure.step("选择自动")
    def select_auto(self):
        self.page.get_by_text("自动", exact=True).click()

    @allure.step("点击强光抑制开关")
    def click_lux_compensation(self):
        self. page.locator("div").filter(has_text=re.compile(r"^强光抑制$")).locator("span").click()

    @allure.step("点击可见光画面旋转开关")
    def vl_rotate(self):
        self.page.locator("div").filter(has_text=re.compile(r"^旋转180°$")).locator("span").click()

    @allure.step("设置红外亮度")
    def set_ir_light(self, value):
        (self.page.locator("form").filter(has_text=self.__ir).get_by_role("textbox").first.fill(value))

    @allure.step("设置红外对比度")
    def set_ir_contrast(self, value):
        (self.page.locator("form").filter(has_text=self.__ir).get_by_role("textbox").nth(1).fill(value))

    @allure.step("设置红外锐度")
    def set_ir_sharpness(self, value):
        (self.page.locator("form").filter(has_text=self.__ir).get_by_role("textbox").nth(2).fill(value))

    @allure.step("设置自动快门补偿间隔")
    def set_auto_shutter_interval(self, value):
        (self.page.locator("div").filter(has_text=re.compile(self.__shutter)).get_by_role("textbox").fill(value))

    @allure.step("点击快门补偿")
    def click_shutter_compensation(self):
        self.page.get_by_role("button", name="快门补偿").click()

    @allure.step("点击红外画面旋转开关")
    def ir_rotate(self):
        self.page.locator("form").filter(has_text=self.__rotate).get_by_role("switch").locator("span").click()

    @allure.step("点击细节增强开关")
    def click_detail_enhancement(self):
        self.page.locator(self.__detail).first.click()

    @allure.step("点击空域降噪开关")
    def click_space_noise_reduction(self):
        self.page.locator(self.__space_noise).click()

    @allure.step("点击时域降噪开关")
    def click_time_noise_reduction(self):
        self.page.locator(self.__time_noise).click()

    @allure.step("设置细节增强值")
    def set_detail_enhancement(self, value):
        self.page.locator("form").filter(has_text=self.__value).get_by_role("textbox").first.fill(value)

    @allure.step("设置空域降噪值")
    def set_space_noise_reduction(self, value):
        self.page.locator("form").filter(has_text=self.__value).get_by_role("textbox").nth(1).fill(value)

    @allure.step("设置时域降噪值")
    def set_time_noise_reduction(self, value):
        self.page.locator("form").filter(has_text=self.__value).get_by_role("textbox").nth(2).fill(value)

    @allure.step("点击默认")
    def click_default(self):
        self.page.get_by_role("button", name="默认").click()

    @allure.step("点击刷新")
    def click_refresh(self):
        self.page.get_by_role("button", name="刷新").click()

    @allure.step("点击确定")
    def click_ok(self):
        self.page.get_by_role("button", name="确定").click()








































































































































































