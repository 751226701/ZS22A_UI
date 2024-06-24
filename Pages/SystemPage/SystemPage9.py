# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/3/21 8:46
# @File :SystemPage9
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
    # 存储设置子模块元素定位
    __test = ""
    __disk = r"^硬盘满时覆盖 停止录像/抓图$|^硬盘满时$"
    __record_time = r"^最大录像时长 min 5~60分钟，且文件大小不超过999M$"

    @allure.step("点清除数据")
    def click_clear_data(self):
        self.page.get_by_role("button", name="清除数据").click()

    @allure.step("确定")
    def click_confirm(self):
        self.page.get_by_label("提示").get_by_role("button", name="确定").click()

    @allure.step("取消")
    def click_cancel(self):
        self.page.get_by_label("提示").get_by_role("button", name="取消").click()

    @allure.step("硬盘满时-覆盖")
    def click_disk_full_cover(self):
        self.page.locator("div").filter(has_text=re.compile(self.__disk)).locator("i").click()
        self.page.get_by_text("覆盖").click()

    @allure.step("硬盘满时-停止录像/抓图")
    def click_disk_full_stop(self):
        self.page.locator("div").filter(has_text=re.compile(self.__disk)).locator("i").click()
        self.page.get_by_text("停止录像/抓图").click()

    @allure.step("下载日志")
    def click_download_log(self):
        self.page.get_by_role("button", name="下载日志").click()

    @allure.step("设置最大录像时长")
    def set_max_record_time(self, value):
        self.page.locator("div").filter(has_text=re.compile(self.__record_time)).get_by_role("textbox").fill(value)

    @allure.step("设置抓图间隔时间")
    def set_capture_interval(self, value):
        self.page.locator("div").filter(has_text=re.compile(r"^抓图间隔时间 s 1~30$")).get_by_role("textbox").fill(value)

    @allure.step("设置抓图数量")
    def set_capture_number(self, value):
        self.page.locator("div").filter(has_text=re.compile(r"^抓图数量 张 1~30$")).get_by_role("textbox").fill(value)

    # FTP
    @allure.step("切换至FTP页面")
    def click_ftp(self):
        self.page.get_by_role("tab", name="FTP").click()

    @allure.step("启用开关")
    def click_switch(self):
        self.page.get_by_role("switch").locator("span").click()

    @allure.step("设置服务器地址")
    def set_server_address(self, value):
        self.page.locator("div").filter(has_text=re.compile(r"^服务器地址$")).get_by_role("textbox").fill(value)

    @allure.step("设置端口")
    def set_port(self, value):
        self.page.locator("div").filter(has_text=re.compile(r"^端口 0~65535$")).get_by_role("textbox").fill(value)

    @allure.step("设置用户名")
    def set_username(self, value):
        self.page.locator("div").filter(has_text=re.compile(r"^用户名$")).get_by_role("textbox").fill(value)

    @allure.step("设置密码")
    def set_password(self, value):
        self.page.locator("input[type=\"password\"]").fill(value)

    @allure.step("设置远程存储目录")
    def set_remote_directory(self, value):
        self.page.locator("div").filter(has_text=re.compile(r"^远程存储目录$")).get_by_role("textbox").fill(value)

    @allure.step("点击默认")
    def click_default(self):
        self.page.get_by_role("button", name="默认").click()

    @allure.step("点击刷新")
    def click_refresh(self):
        self.page.get_by_role("button", name="刷新").click()

    @allure.step("点击确定")
    def click_ok(self):
        self.page.get_by_role("button", name="确定").click()














