#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: 刘涛
# @time: 2024/1/15 10:07
# @file: conftest.py
# @project: ZS22A_UI

import os
import allure
import pytest
import time
from playwright.sync_api import sync_playwright
from Config.Config import Config
from datetime import datetime

pageobject = None
# 获取当前系统时间
now_time = time.strftime("[%Y-%m-%d-%H-%M-%S]", time.localtime())
Trace = Config.trace1


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
        yield pageobject
        pageobject = None
        if Trace:
            context.tracing.stop(path="trace1.zip")
        else:
            pass

        context.close()
        browser.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    获取每个用例状态的钩子函数
    :param item: 测试用例
    :param call: 测试步骤
    :return:
    """
    # 获取钩子方法的调用结果
    out_come = yield
    rep = out_come.get_result()  # 从钩子方法的调用结果中获取测试报告
    # rep.when表示测试步骤，仅仅获取用例call 执行结果是失败的情况, 不包含 setup/teardown
    if rep.when == "call" and rep.failed:
        failures_log = os.path.join(Config.logs, "failures.log")
        mode = "a" if os.path.exists(failures_log) else "w"
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(failures_log, mode) as f:
            f.write(f"{current_time} - ")
            if "CaseData" in item.fixturenames:
                extra = " (%s)" % item.funcargs["CaseData"]
            else:
                extra = ""
            f.write(rep.nodeid + extra + "\n")
            # f.write(f"Exception: {rep.longreprtext}\n")    #记录异常到日志
        # 添加allure报告截图
        if hasattr(pageobject, "screenshot"):
            with allure.step('添加失败截图...'):
                path = Config.test_screenshot_dir + os.path.sep + item.funcargs["CaseData"].get("用例编号") + "失败截图.png"
                file = pageobject.screenshot(path=path)
                allure.attach.file(file, "失败截图", allure.attachment_type.PNG)
