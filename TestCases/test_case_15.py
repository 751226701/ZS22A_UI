# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/3/19 14:14
# @File :test_case_15
# @Project : ZS22A_UI

import os
import re
import allure
import pytest
from playwright.sync_api import sync_playwright
from Pages.SystemPage.SystemPage3 import SystemPage
from Common.ReadYaml import ReadYaml
from Common.AllurePretty import PrettyAllure
from Config.Config import Config

yaml_data = ReadYaml(os.path.join(Config.test_datas_dir, "test_data_15.yaml"))
logindata = yaml_data.read()[0]
Trace = Config.trace15
pageobject = None
DOWNLOAD_FLAG = False

@allure.step("登录")
def login(pageobject, url, user, passwd):
    pageobject.goto(url)
    pageobject.get_by_placeholder("请输入用户名").fill(user)
    pageobject.get_by_placeholder("请输入密码").fill(passwd)
    pageobject.locator("label span").nth(1).click()
    pageobject.wait_for_timeout(3000)
    pageobject.get_by_role("button", name="登录").click()
    pageobject.get_by_text("系统管理").click()
    pageobject.get_by_role("menuitem", name="OSD设置").click()
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
            context.tracing.stop(path="trace15.zip")
        else:
            pass
        context.close()
        browser.close()

"""执行OSD设置子模块测试"""
class TestAlarm:

    """全局温度显示默认值"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_01"]))
    def test_case_01(self, page, CaseData: dict):
        page = SystemPage(page)
        page.click_default()
        page.click_ok()
        page.assert_temp_type(CaseData["断言元素定位"])

    """全局温度显示默认显示"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_02"]))
    def test_case_02(self, page, CaseData: dict):
        page = SystemPage(page)
        page.click_default()
        page.click_ok()
        page.assert_global_temp_box(CaseData["断言元素定位"])

    """全局温度显示设置最高温"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_03"]))
    def test_case_03(self, page, CaseData: dict):
        page = SystemPage(page)
        page.select_temp_type()
        page.max_temp()
        page.click_ok()
        page.click_refresh()
        page.assert_temp_type(CaseData["断言元素定位"])

    """全局温度显示设置最低温"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_04"]))
    def test_case_04(self, page, CaseData: dict):
        page = SystemPage(page)
        page.select_temp_type()
        page.min_temp()
        page.click_ok()
        page.click_refresh()
        page.assert_temp_type(CaseData["断言元素定位"])

    """全局温度显示设置平均温"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_05"]))
    def test_case_05(self, page, CaseData: dict):
        page = SystemPage(page)
        page.select_temp_type()
        page.avg_temp()
        page.click_ok()
        page.click_refresh()
        page.assert_temp_type(CaseData["断言元素定位"])

    """全局温度显示设置最高温+最低温"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_06"]))
    def test_case_06(self, page, CaseData: dict):
        page = SystemPage(page)
        page.select_temp_type()
        page.max_min_temp()
        page.click_ok()
        page.click_refresh()
        page.assert_temp_type(CaseData["断言元素定位"])

    """全局温度显示设置最高温+平均温"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_07"]))
    def test_case_07(self, page, CaseData: dict):
        page = SystemPage(page)
        page.select_temp_type()
        page.max_avg_temp()
        page.click_ok()
        page.click_refresh()
        page.assert_temp_type(CaseData["断言元素定位"])

    """全局温度显示设置平均温+最低温"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_08"]))
    def test_case_08(self, page, CaseData: dict):
        page = SystemPage(page)
        page.select_temp_type()
        page.min_avg_temp()
        page.click_ok()
        page.click_refresh()
        page.assert_temp_type(CaseData["断言元素定位"])

    """全局温度显示设置最高温+最低温+平均温"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_09"]))
    def test_case_09(self, page, CaseData: dict):
        page = SystemPage(page)
        page.select_temp_type()
        page.max_min_avg_temp()
        page.click_ok()
        page.click_refresh()
        page.assert_temp_type(CaseData["断言元素定位"])

    """全局温度显示设置不显示"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_10"]))
    def test_case_10(self, page, CaseData: dict):
        page = SystemPage(page)
        page.click_global_temp_box()
        page.click_ok()
        page.click_refresh()
        page.assert_temp_type(CaseData["断言元素定位"])

    """日期显示默认显示"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_11"]))
    def test_case_11(self, page, CaseData: dict):
        page = SystemPage(page)
        page.click_default()
        page.click_ok()
        page.assert_date_box(CaseData["断言元素定位"])

    """日期显示设置不显示"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_12"]))
    def test_case_12(self, page, CaseData: dict):
        page = SystemPage(page)
        page.click_date_box()
        page.click_ok()
        page.click_refresh()
        page.assert_date_box(CaseData["断言元素定位"])

    """日期显示设置显示"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_13"]))
    def test_case_13(self, page, CaseData: dict):
        page = SystemPage(page)
        page.click_date_box()
        page.click_ok()
        page.click_refresh()
        page.assert_date_box(CaseData["断言元素定位"])

    """字符串默认不显示"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_14"]))
    def test_case_14(self, page, CaseData: dict):
        page = SystemPage(page)
        page.click_default()
        page.click_ok()
        page.assert_string_box(CaseData["断言元素定位"])

    """设置字符串内容"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_15"]))
    def test_case_15(self, page, CaseData: dict):
        page = SystemPage(page)
        page.set_string_content(CaseData["断言元素定位"])
        page.click_ok()
        page.click_refresh()
        page.assert_string_content(CaseData["断言元素定位"])

    """设置字符串显示"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_16"]))
    def test_case_16(self, page, CaseData: dict):
        page = SystemPage(page)
        page.click_string_box()
        page.click_ok()
        page.click_refresh()
        page.assert_string_box(CaseData["断言元素定位"])

    """设置字符串不显示"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_17"]))
    def test_case_17(self, page, CaseData: dict):
        page = SystemPage(page)
        page.click_string_box()
        page.click_ok()
        page.click_refresh()
        page.assert_string_box(CaseData["断言元素定位"])

    """通道名称默认不显示"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_18"]))
    def test_case_18(self, page, CaseData: dict):
        page = SystemPage(page)
        page.click_default()
        page.click_ok()
        page.assert_channel_name_box(CaseData["断言元素定位"])

    """设置通道名称内容"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_19"]))
    def test_case_19(self, page, CaseData: dict):
        page = SystemPage(page)
        page.set_channel_name(CaseData["断言元素定位"])
        page.click_ok()
        page.click_refresh()
        page.assert_channel_name(CaseData["断言元素定位"])

    """设置通道名称显示"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_20"]))
    def test_case_20(self, page, CaseData: dict):
        page = SystemPage(page)
        page.click_channel_name_box()
        page.click_ok()
        page.click_refresh()
        page.assert_channel_name_box(CaseData["断言元素定位"])

    """设置通道名称不显示"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_21"]))
    def test_case_21(self, page, CaseData: dict):
        page = SystemPage(page)
        page.click_channel_name_box()
        page.click_ok()
        page.click_refresh()
        page.assert_channel_name_box(CaseData["断言元素定位"])






























