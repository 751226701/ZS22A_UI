# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/3/18 17:20
# @File :test_case_11
# @Project : ZS22A_UI

import os
import re
import allure
import pytest
from playwright.sync_api import sync_playwright
from Pages.AlarmPage.AlarmPage7 import AlarmPage
from Common.ReadYaml import ReadYaml
from Common.AllurePretty import PrettyAllure
from Config.Config import Config

yaml_data = ReadYaml(os.path.join(Config.test_datas_dir, "test_data_11.yaml")).read()
logindata = yaml_data[0]
Trace = Config.trace11
pageobject = None
DOWNLOAD_FLAG = False

@allure.step("登录")
def login(pageobject, url, user, passwd):
    pageobject.goto(url)
    pageobject.get_by_placeholder("请输入用户名").fill(user)
    pageobject.get_by_placeholder("请输入密码").fill(passwd)
    pageobject.wait_for_timeout(3000)
    pageobject.get_by_role("button", name="登录").click()
    pageobject.get_by_text("报警管理").click()
    pageobject.get_by_text("其他事件").click()
    pageobject.get_by_role("menuitem", name="报警输入").click()
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
            context.tracing.stop(path="trace11.zip")
        else:
            pass
        context.close()
        browser.close()

"""执行报警输入子模块测试"""
class TestAlarm:

    """设置报警输入报警"""
    @PrettyAllure.PrettyAllureWarpper
    @pytest.mark.parametrize("CaseData", [yaml_data[1]])
    def test_case_01(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.alarm_switch()
        page.sensor_type()
        page.sensor_type_normal()
        page.set_debounce_time("5")
        page.set_alarm_interval_time()
        page.alarm_interval_10min()
        page.click_vl_record_box()
        page.click_ir_record_box()
        page.set_record_time("200")
        page.click_vl_capture_box()
        page.click_ir_capture_box()
        page.click_email_switch()
        page.click_audio_switch()
        page.click_light_switch()
        page.click_alarm_output_switch()
        page.set_audio_time("99")
        page.set_light_time("99")
        page.set_alarm_output_time("99")



