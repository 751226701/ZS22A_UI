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
    pageobject.locator("label span").nth(1).click()
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
        page.select_object_temp()
        page.select_object_temp_high()
        page.search_temperature_curve()
        page.page.wait_for_timeout(1000)
        page.assert_selected_object_temp(CaseData['断言元素定位'])

    """查看所有分析对象最低温温度曲线"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[2]])
    def test_case_02(self, page, CaseData: dict):
        page = ReportPage(page)
        page.select_object_temp()
        page.select_object_temp_low()
        page.search_temperature_curve()
        page.page.wait_for_timeout(1000)
        page.assert_selected_object_temp(CaseData['断言元素定位'])

    """查看所有分析对象平均温温度曲线"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[3]])
    def test_case_03(self, page, CaseData: dict):
        page = ReportPage(page)
        page.select_object_temp()
        page.select_object_temp_avg()
        page.search_temperature_curve()
        page.page.wait_for_timeout(1000)
        page.assert_selected_object_temp(CaseData['断言元素定位'])

    """取消点分析对象复选框后查询温度曲线"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[4]])
    def test_case_04(self, page, CaseData: dict):
        page = ReportPage(page)
        page.select_point()
        page.search_temperature_curve()
        page.page.wait_for_timeout(1000)
        page.assert_unselected_point()

    """取消线分析对象复选框后查询温度曲线"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[5]])
    def test_case_05(self, page, CaseData: dict):
        page = ReportPage(page)
        page.select_line()
        page.search_temperature_curve()
        page.page.wait_for_timeout(1000)
        page.assert_unselected_line()

    """取消圆分析对象复选框后查询温度曲线"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[6]])
    def test_case_06(self, page, CaseData: dict):
        page = ReportPage(page)
        page.select_round()
        page.search_temperature_curve()
        page.page.wait_for_timeout(1000)
        page.assert_unselected_round()

    """取消矩形分析对象复选框后查询温度曲线"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[7]])
    def test_case_07(self, page, CaseData: dict):
        page = ReportPage(page)
        page.select_rectangle()
        page.search_temperature_curve()
        page.page.wait_for_timeout(1000)
        page.assert_unselected_rectangle()

    """取消多边形分析对象复选框后查询温度曲线"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[8]])
    def test_case_08(self, page, CaseData: dict):
        page = ReportPage(page)
        page.select_polygon()
        page.search_temperature_curve()
        page.page.wait_for_timeout(1000)
        page.assert_select_object()

    """选择所有分析对象复选框后查询温度曲线"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[9]])
    def test_case_09(self, page, CaseData: dict):
        page = ReportPage(page)
        page.select_point()
        page.select_line()
        page.select_round()
        page.select_rectangle()
        page.select_polygon()
        page.search_temperature_curve()
        page.page.wait_for_timeout(1000)
        page.assert_selected_point()
        page.assert_selected_line()
        page.assert_selected_round()
        page.assert_selected_rectangle()
        page.assert_selected_polygon()

    """取消全选"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[10]])
    def test_case_10(self, page, CaseData: dict):
        page = ReportPage(page)
        page.select_all()
        page.search_temperature_curve()
        page.assert_unselected_all()

    """下载温度曲线截图"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[11]])
    def test_case_11(self, page, CaseData: dict):
        page = ReportPage(page)
        page.select_all()
        page.search_temperature_curve()
        page.download_temperature_curve_image()
        page.page.wait_for_timeout(1000)
        assert DOWNLOAD_FLAG == True
        set_download_flag(False)

    """按1min间隔导出报表"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[12]])
    def test_case_12(self, page, CaseData: dict):
        page = ReportPage(page)
        page.select_period()
        page.select_period_1min()
        page.export_report()
        page.page.wait_for_timeout(5000)
        assert DOWNLOAD_FLAG == True
        set_download_flag(False)

    """按5min间隔导出报表"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[13]])
    def test_case_13(self, page, CaseData: dict):
        page = ReportPage(page)
        page.select_period()
        page.select_period_5min()
        page.export_report()
        page.page.wait_for_timeout(5000)
        assert DOWNLOAD_FLAG == True
        set_download_flag(False)

    """按10min间隔导出报表"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[14]])
    def test_case_14(self, page, CaseData: dict):
        page = ReportPage(page)
        page.select_period()
        page.select_period_10min()
        page.export_report()
        page.page.wait_for_timeout(5000)
        assert DOWNLOAD_FLAG == True
        set_download_flag(False)

    """按15min间隔导出报表"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[15]])
    def test_case_15(self, page, CaseData: dict):
        page = ReportPage(page)
        page.select_period()
        page.select_period_15min()
        page.export_report()
        page.page.wait_for_timeout(5000)
        assert DOWNLOAD_FLAG == True
        set_download_flag(False)

    """按60min间隔导出报表"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[16]])
    def test_case_16(self, page, CaseData: dict):
        page = ReportPage(page)
        page.select_period()
        page.select_period_60min()
        page.export_report()
        page.page.wait_for_timeout(5000)
        assert DOWNLOAD_FLAG == True
        set_download_flag(False)



























































































