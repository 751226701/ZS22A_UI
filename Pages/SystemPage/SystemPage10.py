# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/3/21 9:27
# @File :SystemPage10
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

class SystemPage(Common):
    # 界面设置子模块元素定位
    __test = ""
    __language = r"^系统语言简体中文 English$|^系统语言$"
    __main_logo = r"^主页面logo 选择 建议：JPG、PNG格式，图片尺寸为116\*42PX，大小在500KB以内$"
    __logo_logo = r"^登录页logo 选择 建议：JPG、PNG格式，图片尺寸为216\*68PX，大小在500KB以内$"
    __time_format = r"^时间格式12小时制 24小时制$|^时间格式$"
    __timezone = "时区设置(UTC+08:00"
    __temp_unit = r"^温度单位摄氏度℃ 华氏度℉$|^温度单位$"

    @allure.step("简体中文")
    def set_cn(self):
        self.page.locator("div").filter(has_text=re.compile(self.__language)).get_by_placeholder("请选择").click()
        self.page.get_by_text("简体中文").click()

    @allure.step("English")
    def set_en(self):
        self.page.locator("div").filter(has_text=re.compile(self.__language)).get_by_placeholder("请选择").click()
        self.page.get_by_text("English").click()

    @allure.step("设置系统名称")
    def set_system_name(self, name):
        self.page.locator("div").filter(has_text=re.compile(r"^系统名称$")).get_by_role("textbox").fill(name)

    @allure.step("点击上传主页面logo按钮")
    def click_upload_main_logo(self):
        """
        :param picture_path: 照片路径
        :return:
        """
        (self. page.locator("div").filter(has_text=re.compile(self.__main_logo)).
         get_by_role("button").click())

    @allure.step("点击上传登录页logo按钮")
    def click_upload_login_logo(self):
        """
        :param picture_path:照片路径
        :return:
        """
        (self.page.locator("div").filter(has_text=re.compile(self.__logo_logo)).
         get_by_role("button").click())

    @allure.step("设置版权所属")
    def set_copyright(self, value):
        self.page.locator("div").filter(has_text=re.compile(r"^版权所属$")).get_by_role("textbox").fill(value)

    @allure.step("12小时制")
    def set_12_hour(self):
        self.page.locator("div").filter(has_text=re.compile(self.__time_format)).get_by_placeholder("请选择").click()
        self.page.get_by_text("12小时制").click()

    @allure.step("24小时制")
    def set_24_hour(self):
        self.page.locator("div").filter(has_text=re.compile(self.__time_format)).get_by_placeholder("请选择").click()
        self.page.get_by_text("24小时制").click()

    @allure.step("选择时区")
    def set_timezone(self, value):
        """
        :param value: 具体时区，例："(UTC-09:00)阿拉斯加"
        :return:无
        """
        self.page.locator("form div").filter(has_text=re.compile("^时区设置")).get_by_placeholder("请选择").click()
        self.page.get_by_text(value).click()

    @allure.step("时间校正")
    def set_time_correct(self):
        self.page.get_by_role("button", name="同步PC").click()

    @allure.step("摄氏度")
    def set_celsius(self):
        self.page.locator("div").filter(has_text=re.compile(self.__temp_unit)).get_by_placeholder("请选择").click()
        self.page.get_by_text("摄氏度℃").click()

    @allure.step("华氏度")
    def set_fahrenheit(self):
        self.page.locator("div").filter(has_text=re.compile(self.__temp_unit)).get_by_placeholder("请选择").click()
        self.page.get_by_text("华氏度℉").click()

    @allure.step("米")
    def set_meter(self):
        self.page.locator("div").filter(has_text=re.compile(r"^距离单位$|^距离单位米 英尺$")).get_by_placeholder("请选择").click()
        self.page.get_by_text("米").click()

    @allure.step("英尺")
    def set_feet(self):
        self.page.locator("div").filter(has_text=re.compile(r"^距离单位$|^距离单位米 英尺$")).get_by_placeholder("请选择").click()
        self.page.get_by_text("英尺").click()

    @allure.step("点击默认")
    def click_default(self):
        self.page.get_by_role("button", name="默认").click()

    @allure.step("点击刷新")
    def click_refresh(self):
        self.page.get_by_role("button", name="刷新").click()

    @allure.step("点击确定")
    def click_ok(self):
        self.page.get_by_role("button", name="确定").click()

