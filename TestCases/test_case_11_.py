#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: 刘涛
@time: 2024/1/16 16:56 
@file: test_case_11_.py
@project: ZS22A_UI
"""
import os
import allure
import pytest
from time import sleep
from playwright.sync_api import sync_playwright
from Pages.PreviewPage.PreviewPage import PreviewPage
from Common.ReadYaml import ReadYaml
from Common.AllurePretty import PrettyAllure
from Config.Config import Config

yaml_data = ReadYaml(os.path.join(Config.test_datas_dir, "test_data_11_.yaml")).read()
logindata = yaml_data[0]
Trace = Config.trace2
pageobject = None


@allure.step("登录")
def login(pageobject, url, user, passwd):
    pageobject.goto(url)
    pageobject.get_by_placeholder("请输入用户名").fill(user)
    pageobject.get_by_placeholder("请输入密码").fill(passwd)
    sleep(3)
    pageobject.get_by_role("button", name="登录").click()


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
            login(pageobject, logindata["url地址"], logindata["账号"], logindata["密码"])
        yield pageobject
        pageobject = None
        if Trace:
            context.tracing.stop(path="trace2.zip")
        else:
            pass
        context.close()
        browser.close()


"""执行实时预览模块测试"""


class TestPreview:
    """暂停视频播放"""

    @PrettyAllure.PrettyAllureWarpper
    @pytest.mark.parametrize("CaseData", [yaml_data[1]])
    def test_case_11(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_video_stop()

    """开始视频播放"""

    @PrettyAllure.PrettyAllureWarpper
    @pytest.mark.parametrize("CaseData", [yaml_data[2]])
    def test_case_12(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_video_start()
