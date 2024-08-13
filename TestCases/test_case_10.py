# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/3/18 16:16
# @File :test_case_10.py
# @Project : ZS22A_UI

import os
import re
import allure
import pytest
from playwright.sync_api import sync_playwright
from Pages.AlarmPage.AlarmPage6 import AlarmPage
from Common.ReadYaml import ReadYaml
from Common.AllurePretty import PrettyAllure
from Config.Config import Config

yaml_data = ReadYaml(os.path.join(Config.test_datas_dir, "test_data_10.yaml"))
logindata = yaml_data.read()[0]
Trace = Config.trace10
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
    pageobject.get_by_text("其他事件").click()
    pageobject.get_by_role("menuitem", name="非法访问").click()
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
            context.tracing.stop(path="trace10.zip")
        else:
            pass
        context.close()
        browser.close()

"""执行非法访问子模块测试"""

class TestAlarm:

    """启用状态默认关"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_01']))
    def test_case_01(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.click_default()
        page.click_ok()
        page.click_refresh()
        page.assert_alarm_switch(CaseData['断言元素定位'])

    """启用报警"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_02']))
    def test_case_02(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.alarm_switch()
        page.click_ok()
        page.click_refresh()
        page.assert_alarm_switch(CaseData['断言元素定位'])

    """关闭报警"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_03']))
    def test_case_03(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.alarm_switch()
        page.click_ok()
        page.click_refresh()
        page.assert_alarm_switch(CaseData['断言元素定位'])

    """锁定阈值默认值"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_04']))
    def test_case_04(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.click_default()
        page.click_ok()
        page.click_refresh()
        page.set_lock_threshold(CaseData['断言元素定位'])

    """锁定阈值设置3"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_05']))
    def test_case_05(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.set_lock_threshold("3")
        page.click_ok()
        page.click_refresh()
        page.set_lock_threshold(CaseData['断言元素定位'])

    """锁定阈值设置10"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_06']))
    def test_case_06(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.set_lock_threshold("10")
        page.click_ok()
        page.click_refresh()
        page.set_lock_threshold(CaseData['断言元素定位'])

    """锁定阈值设置2"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_07']))
    def test_case_07(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.set_lock_threshold("2")
        page.click_ok()
        page.click_refresh()
        page.set_lock_threshold(CaseData['断言元素定位'])

    """锁定阈值设置11"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_08']))
    def test_case_08(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.set_lock_threshold("11")
        page.click_ok()
        page.click_refresh()
        page.set_lock_threshold(CaseData['断言元素定位'])

    """报警间隔时间默认值"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_09']))
    def test_case_09(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.click_default()
        page.click_ok()
        page.click_refresh()
        page.assert_alarm_interval(CaseData['断言元素定位'])

    """报警间隔时间设置30s"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_10']))
    def test_case_10(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.alarm_interval()
        page.alarm_interval_30s()
        page.click_ok()
        page.click_refresh()
        page.assert_alarm_interval(CaseData['断言元素定位'])

    """报警间隔时间设置60s"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_11']))
    def test_case_11(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.alarm_interval()
        page.alarm_interval_60s()
        page.click_ok()
        page.click_refresh()
        page.assert_alarm_interval(CaseData['断言元素定位'])

    """报警间隔时间设置5min"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_12']))
    def test_case_12(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.alarm_interval()
        page.alarm_interval_5min()
        page.click_ok()
        page.click_refresh()
        page.assert_alarm_interval(CaseData['断言元素定位'])

    """报警间隔时间设置10min"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_13']))
    def test_case_13(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.alarm_interval()
        page.alarm_interval_10min()
        page.click_ok()
        page.click_refresh()
        page.assert_alarm_interval(CaseData['断言元素定位'])

    """报警间隔时间设置15min"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_14']))
    def test_case_14(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.alarm_interval()
        page.alarm_interval_15min()
        page.click_ok()
        page.click_refresh()
        page.assert_alarm_interval(CaseData['断言元素定位'])

    """报警间隔时间设置30min"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_15']))
    def test_case_15(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.alarm_interval()
        page.alarm_interval_30min()
        page.click_ok()
        page.click_refresh()
        page.assert_alarm_interval(CaseData['断言元素定位'])

    """报警间隔时间设置60min"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_16']))
    def test_case_16(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.alarm_interval()
        page.alarm_interval_60min()
        page.click_ok()
        page.click_refresh()
        page.assert_alarm_interval(CaseData['断言元素定位'])

    """邮件通知默认关"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_17']))
    def test_case_17(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.click_default()
        page.click_ok()
        page.click_refresh()
        page.assert_email_switch(CaseData['断言元素定位'])

    """启用邮件通知"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_18']))
    def test_case_18(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.click_email_switch()
        page.click_ok()
        page.click_refresh()
        page.assert_email_switch(CaseData['断言元素定位'])

    """关闭邮件通知"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_19']))
    def test_case_19(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.click_email_switch()
        page.click_ok()
        page.click_refresh()
        page.assert_email_switch(CaseData['断言元素定位'])









