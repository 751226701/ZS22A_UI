# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/2/29 16:51
# @File :test_case_04.py
# @Project : ZS22A_UI

import os
import allure
import pytest
from playwright.sync_api import sync_playwright
from Pages.ReportPage.ReportPage import ReportPage
from Common.ReadYaml import ReadYaml
from Common.AllurePretty import PrettyAllure
from Config.Config import Config

yaml_data = ReadYaml(os.path.join(Config.test_datas_dir, "test_data_04.yaml")).read()
logindata = yaml_data[0]
Trace = Config.trace4
pageobject = None
DOWNLOAD_FLAG = False

@allure.step("登录")
def login(pageobject, url, user, passwd):
    pageobject.goto(url)
    pageobject.get_by_placeholder("请输入用户名").fill(user)
    pageobject.get_by_placeholder("请输入密码").fill(passwd)
    pageobject.wait_for_timeout(3000)
    pageobject.get_by_role("button", name="登录").click()
    pageobject.get_by_text("统计报表").click()
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
            context.tracing.stop(path="trace4.zip")
        else:
            pass
        context.close()
        browser.close()

"""执行统计报表模块测试"""
class TestPlayBack:

    """查看所有分析对象最高温温度曲线"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[1]])
    def test_case_01(self, page, CaseData: dict):
        page = ReportPage(page)
        page.search_temperature_curve()


    """查看所有分析对象最低温温度曲线"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[2]])
    def test_case_02(self, page, CaseData: dict):
        page = ReportPage(page)
        page.select_object_temp()
        page.select_object_temp_low()
        page.search_temperature_curve()

    """查看所有分析对象平均温温度曲线"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[3]])
    def test_case_03(self, page, CaseData: dict):
        page = ReportPage(page)
        page.select_object_temp()
        page.select_object_temp_avg()
        page.search_temperature_curve()

    """取消全选"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[4]])
    def test_case_04(self, page, CaseData: dict):
        page = ReportPage(page)
        page.select_all()

    """全选"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[5]])
    def test_case_05(self, page, CaseData: dict):
        page = ReportPage(page)
        page.select_all()

    """下载温度曲线截图"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[6]])
    def test_case_06(self, page, CaseData: dict):
        page = ReportPage(page)
        page.search_temperature_curve()
        page.download_temperature_curve_image()
        assert DOWNLOAD_FLAG == True
        set_download_flag(False)

    """导出报表"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[7]])
    def test_case_07(self, page, CaseData: dict):
        page = ReportPage(page)
        page.search_temperature_curve()
        page.export_report()
        page.page.wait_for_timeout(5000)
        assert DOWNLOAD_FLAG == True
        set_download_flag(False)



































































































