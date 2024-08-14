# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/3/19 9:16
# @File :test_case_12
# @Project : ZS22A_UI

import os
import re
import allure
import pytest
from playwright.sync_api import sync_playwright
from Pages.AlarmPage.AlarmPage8 import AlarmPage
from Common.ReadYaml import ReadYaml
from Common.AllurePretty import PrettyAllure
from Config.Config import Config

yaml_data = ReadYaml(os.path.join(Config.test_datas_dir, "test_data_12.yaml"))
logindata = yaml_data.read()[0]
Trace = Config.trace12
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
    pageobject.get_by_text("报警事件").click()
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
            context.tracing.stop(path="trace12.zip")
        else:
            pass
        context.close()
        browser.close()

"""执行报警事件子模块测试"""
class TestAlarm:

    """报警类型选择全部"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_01']))
    def test_case_01(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.alarm_type_select()
        page.select_all()
        page.query_alarm_event()
        page.assert_alarm_type(CaseData['断言元素定位'])

    """报警类型选择全局温度"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_02']))
    def test_case_02(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.alarm_type_select()
        page.cancel_all()
        page.select_global_temp()
        page.query_alarm_event()
        page.assert_alarm_type(CaseData['断言元素定位'])

    """报警类型选择对象温度"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_03']))
    def test_case_03(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.alarm_type_select()
        page.cancel_global_temp()
        page.cancel_object_temp()
        page.query_alarm_event()
        page.assert_alarm_type(CaseData['断言元素定位'])

    """报警类型选择对象温差"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_04']))
    def test_case_04(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.alarm_type_select()
        page.cancel_object_temp()
        page.select_object_temp_diff()
        page.query_alarm_event()
        page.assert_alarm_type(CaseData['断言元素定位'])

    """报警类型选择存储异常"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_05']))
    def test_case_05(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.alarm_type_select()
        page.cancel_object_temp_diff()
        page.select_storage_abnormal()
        page.query_alarm_event()
        page.assert_alarm_type(CaseData['断言元素定位'])

    """报警类型选择网络异常"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_06']))
    def test_case_06(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.alarm_type_select()
        page.cancel_storage_abnormal()
        page.select_network_abnormal()
        page.query_alarm_event()
        page.assert_alarm_type(CaseData['断言元素定位'])

    """报警类型选择非法访问"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_07']))
    def test_case_07(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.alarm_type_select()
        page.cancel_network_abnormal()
        page.select_illegal_access()
        page.query_alarm_event()
        page.assert_alarm_type(CaseData['断言元素定位'])

    """报警类型选择报警输入"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_08']))
    def test_case_08(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.alarm_type_select()
        page.cancel_illegal_access()
        page.select_alarm_input()
        page.query_alarm_event()
        page.assert_alarm_type(CaseData['断言元素定位'])

    """静音"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_09']))
    def test_case_09(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.page.locator(".el-tooltip").click()
        page.assert_mute_button(CaseData['断言元素定位'])

    """取消静音"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_10']))
    def test_case_10(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.page.locator(".el-tooltip").click()
        page.assert_mute_button(CaseData['断言元素定位'])

    """报警复归"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_11']))
    def test_case_11(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.click_recovery_button()
        page.assert_alert(CaseData['断言元素定位'])

    """清空报警"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_12']))
    def test_case_12(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.page.wait_for_timeout(3000)
        page.click_clear_alarm()
        page.click_ok_clear_alarm()
        page.assert_alert(CaseData['断言元素定位'])




