# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/3/8 10:29
# @File :test_case_07.py
# @Project : ZS22A_UI

import os
import re
import allure
import pytest
from playwright.sync_api import sync_playwright
from Pages.AlarmPage.AlarmPage3 import AlarmPage
from Common.ReadYaml import ReadYaml
from Common.AllurePretty import PrettyAllure
from Config.Config import Config

yaml_data = ReadYaml(os.path.join(Config.test_datas_dir, "test_data_07.yaml"))
logindata = yaml_data.read()[0]
Trace = Config.trace7
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
    pageobject.get_by_role("menuitem", name="对象温差").click()
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
            context.tracing.stop(path="trace7.zip")
        else:
            pass
        context.close()
        browser.close()

"""执行对象温差子模块测试"""
class TestAlarm:

    """去抖动默认值"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_01"]))
    def test_case_01(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.click_default()
        page.assert_debounce_time(CaseData["断言元素定位"])

    """去抖动设置0"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_02"]))
    def test_case_02(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.set_debounce_time("0")
        page.click_ok()
        page.click_refresh()
        page.assert_debounce_time(CaseData["断言元素定位"])

    """去抖动设置3"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_03"]))
    def test_case_03(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.set_debounce_time("3")
        page.click_ok()
        page.click_refresh()
        page.assert_debounce_time(CaseData["断言元素定位"])

    """去抖动设置10"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_04"]))
    def test_case_04(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.set_debounce_time("10")
        page.click_ok()
        page.click_refresh()
        page.assert_debounce_time(CaseData["断言元素定位"])

    """去抖动设置-1"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_05"]))
    def test_case_05(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.set_debounce_time("-1")
        page.click_ok()
        page.click_refresh()
        page.assert_debounce_time(CaseData["断言元素定位"])

    """去抖动设置-1"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_06"]))
    def test_case_06(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.set_debounce_time("11")
        page.click_ok()
        page.click_refresh()
        page.assert_debounce_time(CaseData["断言元素定位"])

    """报警间隔时间默认值"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_07"]))
    def test_case_07(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.assert_alarm_interval_time(CaseData["断言元素定位"])

    """报警间隔时间设置30s"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_08"]))
    def test_case_08(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.select_alarm_interval_time()
        page.select_30s()
        page.click_ok()
        page.click_refresh()
        page.assert_alarm_interval_time(CaseData["断言元素定位"])

    """报警间隔时间设置60s"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_09"]))
    def test_case_09(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.select_alarm_interval_time()
        page.select_60s()
        page.click_ok()
        page.click_refresh()
        page.assert_alarm_interval_time(CaseData["断言元素定位"])

    """报警间隔时间设置5min"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_10"]))
    def test_case_10(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.select_alarm_interval_time()
        page.select_5min()
        page.click_ok()
        page.click_refresh()
        page.assert_alarm_interval_time(CaseData["断言元素定位"])

    """报警间隔时间设置10min"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_11"]))
    def test_case_11(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.select_alarm_interval_time()
        page.select_10min()
        page.click_ok()
        page.click_refresh()
        page.assert_alarm_interval_time(CaseData["断言元素定位"])

    """报警间隔时间设置15min"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_12"]))
    def test_case_12(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.select_alarm_interval_time()
        page.select_15min()
        page.click_ok()
        page.click_refresh()
        page.assert_alarm_interval_time(CaseData["断言元素定位"])

    """报警间隔时间设置30min"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_13"]))
    def test_case_13(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.select_alarm_interval_time()
        page.select_30min()
        page.click_ok()
        page.click_refresh()
        page.assert_alarm_interval_time(CaseData["断言元素定位"])

    """报警间隔时间设置60min"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_14"]))
    def test_case_14(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.select_alarm_interval_time()
        page.select_60min()
        page.click_ok()
        page.click_refresh()
        page.assert_alarm_interval_time(CaseData["断言元素定位"])

    """可见光录像默认勾选"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_15"]))
    def test_case_15(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.assert_vl_record_box(CaseData["断言元素定位"])

    """取消可见光录像"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_16"]))
    def test_case_16(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.click_vl_record_box()
        page.click_ok()
        page.click_refresh()
        page.assert_vl_record_box(CaseData["断言元素定位"])

    """勾选可见光录像"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_17"]))
    def test_case_17(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.click_vl_record_box()
        page.click_ok()
        page.click_refresh()
        page.assert_vl_record_box(CaseData["断言元素定位"])

    """红外录像默认勾选"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_18"]))
    def test_case_18(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.assert_ir_record_box(CaseData["断言元素定位"])

    """取消红外录像"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_19"]))
    def test_case_19(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.click_ir_record_box()
        page.click_ok()
        page.click_refresh()
        page.assert_ir_record_box(CaseData["断言元素定位"])

    """勾选红外录像"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_20"]))
    def test_case_20(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.click_ir_record_box()
        page.click_ok()
        page.click_refresh()
        page.assert_ir_record_box(CaseData["断言元素定位"])

    """录像时间默认值"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_21"]))
    def test_case_21(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.assert_record_time(CaseData["断言元素定位"])

    """录像时间设置10"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_22"]))
    def test_case_22(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.set_record_time("10")
        page.click_ok()
        page.click_refresh()
        page.assert_record_time(CaseData["断言元素定位"])

    """录像时间设置20"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_23"]))
    def test_case_23(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.set_record_time("20")
        page.click_ok()
        page.click_refresh()
        page.assert_record_time(CaseData["断言元素定位"])

    """录像时间设置300"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_24"]))
    def test_case_24(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.set_record_time("300")
        page.click_ok()
        page.click_refresh()
        page.assert_record_time(CaseData["断言元素定位"])

    """录像时间设置9"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_25"]))
    def test_case_25(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.set_record_time("9")
        page.click_ok()
        page.click_refresh()
        page.assert_record_time(CaseData["断言元素定位"])

    """录像时间设置301"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_26"]))
    def test_case_26(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.set_record_time("301")
        page.click_ok()
        page.click_refresh()
        page.assert_record_time(CaseData["断言元素定位"])

    """可见光抓图默认勾选"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_27"]))
    def test_case_27(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.assert_vl_capture_box(CaseData["断言元素定位"])

    """取消可见光抓图"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_28"]))
    def test_case_28(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.click_vl_capture_box()
        page.click_ok()
        page.click_refresh()
        page.assert_vl_capture_box(CaseData["断言元素定位"])

    """勾选可见光抓图"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_29"]))
    def test_case_29(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.click_vl_capture_box()
        page.click_ok()
        page.click_refresh()
        page.assert_vl_capture_box(CaseData["断言元素定位"])

    """红外抓图默认勾选"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_30"]))
    def test_case_30(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.assert_ir_capture_box(CaseData["断言元素定位"])

    """取消红外抓图"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_31"]))
    def test_case_31(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.click_ir_capture_box()
        page.click_ok()
        page.click_refresh()
        page.assert_ir_capture_box(CaseData["断言元素定位"])

    """勾选红外抓图"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_32"]))
    def test_case_32(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.click_ir_capture_box()
        page.click_ok()
        page.click_refresh()
        page.assert_ir_capture_box(CaseData["断言元素定位"])

    """邮件通知默认关闭"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_33"]))
    def test_case_33(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.assert_email_switch(CaseData["断言元素定位"])

    """开启邮件通知"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_34"]))
    def test_case_34(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.click_email_switch()
        page.click_ok()
        page.click_refresh()
        page.assert_email_switch(CaseData["断言元素定位"])

    """关闭邮件通知"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_35"]))
    def test_case_35(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.click_email_switch()
        page.click_ok()
        page.click_refresh()
        page.assert_email_switch(CaseData["断言元素定位"])














