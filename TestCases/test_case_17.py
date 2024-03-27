# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/3/19 15:43
# @File :test_case_17
# @Project : ZS22A_UI

import os
import re
import allure
import pytest
from playwright.sync_api import sync_playwright
from Pages.SystemPage.SystemPage5 import SystemPage
from Common.ReadYaml import ReadYaml
from Common.AllurePretty import PrettyAllure
from Config.Config import Config

yaml_data = ReadYaml(os.path.join(Config.test_datas_dir, "test_data_17.yaml")).read()
logindata = yaml_data[0]
Trace = Config.trace17
pageobject = None
DOWNLOAD_FLAG = False

@allure.step("登录")
def login(pageobject, url, user, passwd):
    pageobject.goto(url)
    pageobject.get_by_placeholder("请输入用户名").fill(user)
    pageobject.get_by_placeholder("请输入密码").fill(passwd)
    pageobject.wait_for_timeout(3000)
    pageobject.get_by_role("button", name="登录").click()
    pageobject.get_by_text("系统管理").click()
    pageobject.get_by_text("测温设置", exact=True).click()
    pageobject.get_by_role("menuitem", name="全局测温设置").click()
def on_download(download):
    global DOWNLOAD_FLAG
    DOWNLOAD_FLAG = True
    download.save_as(os.path.join(Config.test_download_dir, download.suggested_filename))
def set_download_flag(flag):
    global DOWNLOAD_FLAG
    DOWNLOAD_FLAG = flag

@pytest.fixture(scope="class")
def page():
    global pageobject
    with sync_playwright() as play:
        browser = play.chromium.launch(
            headless=False,
            channel=Config.browser,
            args=['--start-maximized'],
            slow_mo=500)

        context = browser.new_context(no_viewport=True)
        if Trace:
            context.tracing.start(screenshots=True, snapshots=True, sources=True)
        else:
            pass
        if pageobject is None:
            pageobject = context.new_page()
            try:
                pageobject.on('download', on_download)
            except Exception as e:
                print(f"保存失败：{e}")
            login(pageobject, logindata["url地址"], logindata["账号"], logindata["密码"])
        yield pageobject
        pageobject = None
        if Trace:
            context.tracing.stop(path="trace17.zip")
        else:
            pass
        context.close()
        browser.close()

"""执行全局测温设置子模块测试"""
class TestAlarm:

    """设置鼠标点击温度显示"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[1]])
    def test_case_01(self, page, CaseData: dict):
        page = SystemPage(page)
        page.click_mouse_temp_switch()
        page.click_temp_level_select()
        page.select_550()
        page.select_color_bar("黑热")
        page.select_color_bar("彩虹1")
        page.select_color_bar("人体筛查")
        page.select_color_bar("医疗A")
        page.click_color_bar_switch()
        page.click_hot_cold_switch()
        page.set_emiss("0.5")
        page.select_emiss("不锈钢")
        page.select_emiss("石膏")
        page.select_emiss("铜板")
        page.set_distance("9")
        page.set_reflect("999")
        page.set_isotherm("0.5")
        page.click_isotherm_switch()
        page.close_isotherm()
        page.set_isotherm_high()
        page.set_isotherm_low()
        page.set_isotherm_range()
        page.set_isotherm_range_out()
        page.set_isotherm_high_value("88")
        page.set_isotherm_low_value("88")



























