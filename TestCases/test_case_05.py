# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/3/4 13:25
# @File :test_case_05.py
# @Project : ZS22A_UI

import os
import re
import allure
import pytest
from playwright.sync_api import sync_playwright
from Pages.AlarmPage.AlarmPage1 import AlarmPage
from Common.ReadYaml import ReadYaml
from Common.AllurePretty import PrettyAllure
from Config.Config import Config

yaml_data = ReadYaml(os.path.join(Config.test_datas_dir, "test_data_05.yaml"))
logindata = yaml_data.read()[0]
Trace = Config.trace5
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
    pageobject.get_by_text("报警管理").click()
    pageobject.get_by_text("温度监测").click()
    pageobject.get_by_role("menuitem", name="全局温度").click()
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
            context.tracing.stop(path="trace5.zip")
        else:
            pass
        context.close()
        browser.close()

"""执行全局温度子模块测试"""
class TestAlarm:

    """勾选全局高温报警"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_01"]))
    def test_case_01(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.click_global_high_temp_box()
        page.click_ok()
        page.click_refresh()
        page.assert_global_high_temp_box(CaseData["断言元素定位"])

    """不勾选全局高温报警"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_02"]))
    def test_case_02(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.click_global_high_temp_box()
        page.click_ok()
        page.click_refresh()
        page.assert_global_high_temp_box(CaseData["断言元素定位"])

    """勾选全局低温报警"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_03"]))
    def test_case_03(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.click_global_low_temp_box()
        page.click_ok()
        page.click_refresh()
        page.assert_global_low_temp_box(CaseData["断言元素定位"])

    """不勾选全局低温报警"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_04"]))
    def test_case_04(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.click_global_low_temp_box()
        page.click_ok()
        page.click_refresh()
        page.assert_global_low_temp_box(CaseData["断言元素定位"])

    """设置高温大于"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_05"]))
    def test_case_05(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.global_high_temp_select()
        page.select_great()
        page.click_ok()
        page.click_refresh()
        page.assert_high_alarm_condition(CaseData["断言元素定位"])

    """设置高温小于"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_06"]))
    def test_case_06(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.global_high_temp_select()
        page.select_less()
        page.click_ok()
        page.click_refresh()
        page.assert_high_alarm_condition(CaseData["断言元素定位"])

    """设置低温大于"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_07"]))
    def test_case_07(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.global_low_temp_select()
        page.select_great()
        page.click_ok()
        page.click_refresh()
        page.assert_low_alarm_condition(CaseData["断言元素定位"])

    """设置低温小于"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_08"]))
    def test_case_08(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.global_low_temp_select()
        page.select_less()
        page.click_ok()
        page.click_refresh()
        page.assert_low_alarm_condition(CaseData["断言元素定位"])

    """设置高温报警阈值为-40"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_09"]))
    def test_case_09(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.set_global_high_temp_value("-40")
        page.click_ok()
        page.click_refresh()
        page.assert_global_high_temp_value(CaseData["断言元素定位"])

    """设置高温报警阈值为200"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_10"]))
    def test_case_10(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.set_global_high_temp_value("200")
        page.click_ok()
        page.click_refresh()
        page.assert_global_high_temp_value(CaseData["断言元素定位"])

    """设置高温报警阈值为2000"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_11"]))
    def test_case_11(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.set_global_high_temp_value("2000")
        page.click_ok()
        page.click_refresh()
        page.assert_global_high_temp_value(CaseData["断言元素定位"])

    """设置高温报警阈值为-41"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_12"]))
    def test_case_12(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.set_global_high_temp_value("-41")
        page.click_ok()
        page.click_refresh()
        page.assert_global_high_temp_value(CaseData["断言元素定位"])

    """设置高温报警阈值为2001"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_13"]))
    def test_case_13(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.set_global_high_temp_value("2001")
        page.click_ok()
        page.click_refresh()
        page.assert_global_high_temp_value(CaseData["断言元素定位"])

    """设置低温报警阈值为-40"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_14"]))
    def test_case_14(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.set_global_low_temp_value("-40")
        page.click_ok()
        page.click_refresh()
        page.assert_global_low_temp_value(CaseData["断言元素定位"])

    """设置低温报警阈值为200"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_15"]))
    def test_case_15(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.set_global_low_temp_value("200")
        page.click_ok()
        page.click_refresh()
        page.assert_global_low_temp_value(CaseData["断言元素定位"])

    """设置低温报警阈值为2000"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_16"]))
    def test_case_16(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.set_global_low_temp_value("2000")
        page.click_ok()
        page.click_refresh()
        page.assert_global_low_temp_value(CaseData["断言元素定位"])

    """设置低温报警阈值为-41"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_17"]))
    def test_case_17(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.set_global_low_temp_value("-41")
        page.click_ok()
        page.click_refresh()
        page.assert_global_low_temp_value(CaseData["断言元素定位"])

    """设置低温报警阈值为2001"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_18"]))
    def test_case_18(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.set_global_low_temp_value("2001")
        page.click_ok()
        page.click_refresh()
        page.assert_global_low_temp_value(CaseData["断言元素定位"])

    """设置去抖动值为0"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_19"]))
    def test_case_19(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.set_debounce_value("0")
        page.click_ok()
        page.click_refresh()
        page.assert_debounce_value(CaseData["断言元素定位"])

    """设置去抖动值为5"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_20"]))
    def test_case_20(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.set_debounce_value("5")
        page.click_ok()
        page.click_refresh()
        page.assert_debounce_value(CaseData["断言元素定位"])

    """设置去抖动值为10"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_21"]))
    def test_case_21(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.set_debounce_value("10")
        page.click_ok()
        page.click_refresh()
        page.assert_debounce_value(CaseData["断言元素定位"])

    """设置去抖动值为-1"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_22"]))
    def test_case_22(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.set_debounce_value("-1")
        page.click_ok()
        page.click_refresh()
        page.assert_debounce_value(CaseData["断言元素定位"])

    """设置去抖动值为11"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_23"]))
    def test_case_23(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.set_debounce_value("11")
        page.click_ok()
        page.click_refresh()
        page.assert_debounce_value(CaseData["断言元素定位"])

    """设置报警间隔时间为30S"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_24"]))
    def test_case_24(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.set_alarm_interval_time()
        page.select_30s()
        page.click_ok()
        page.click_refresh()
        page.assert_alarm_interval_time(CaseData["断言元素定位"])

    """设置报警间隔时间为60S"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_25"]))
    def test_case_25(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.set_alarm_interval_time()
        page.select_60s()
        page.click_ok()
        page.click_refresh()
        page.assert_alarm_interval_time(CaseData["断言元素定位"])

    """设置报警间隔时间为5min"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_26"]))
    def test_case_26(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.set_alarm_interval_time()
        page.select_5min()
        page.click_ok()
        page.click_refresh()
        page.assert_alarm_interval_time(CaseData["断言元素定位"])

    """设置报警间隔时间为10min"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_27"]))
    def test_case_27(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.set_alarm_interval_time()
        page.select_10min()
        page.click_ok()
        page.click_refresh()
        page.assert_alarm_interval_time(CaseData["断言元素定位"])

    """设置报警间隔时间为15min"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_28"]))
    def test_case_28(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.set_alarm_interval_time()
        page.select_15min()
        page.click_ok()
        page.click_refresh()
        page.assert_alarm_interval_time(CaseData["断言元素定位"])

    """设置报警间隔时间为30min"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_29"]))
    def test_case_29(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.set_alarm_interval_time()
        page.select_30min()
        page.click_ok()
        page.click_refresh()
        page.assert_alarm_interval_time(CaseData["断言元素定位"])

    """设置报警间隔时间为60min"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_30"]))
    def test_case_30(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.set_alarm_interval_time()
        page.select_60min()
        page.click_ok()
        page.click_refresh()
        page.assert_alarm_interval_time(CaseData["断言元素定位"])

















































































