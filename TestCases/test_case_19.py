# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/3/20 8:50
# @File :test_case_19
# @Project : ZS22A_UI

import os
import re
import allure
import pytest
from playwright.sync_api import sync_playwright
from Pages.SystemPage.SystemPage7 import SystemPage
from Common.ReadYaml import ReadYaml
from Common.AllurePretty import PrettyAllure
from Config.Config import Config

yaml_data = ReadYaml(os.path.join(Config.test_datas_dir, "test_data_19.yaml")).read()
logindata = yaml_data[0]
Trace = Config.trace19
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
    pageobject.get_by_text("外设管理", exact=True).click()
    pageobject.get_by_role("menuitem", name="补光灯").click()
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
            context.tracing.stop(path="trace19.zip")
        else:
            pass
        context.close()
        browser.close()


"""执行补光灯子模块测试"""

class TestAlarm:
    """设置补光灯"""

    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[1]])
    def test_case_01(self, page, CaseData: dict):
        page = SystemPage(page)
        page.select_light_mode()
        page.select_time_auto()
        page.select_light_mode()
        page.select_manual()
        page.select_light_switch()
        page.select_light_brightness("80")

















