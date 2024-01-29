#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: 刘涛
# @time: 2024/1/16 16:56
# @file: test_case_02.py
# @project: ZS22A_UI

import os
import allure
import pytest
from time import sleep
from playwright.sync_api import sync_playwright
from Pages.PreviewPage.PreviewPage import PreviewPage
from Common.ReadYaml import ReadYaml
from Common.AllurePretty import PrettyAllure
from Config.Config import Config

yaml_data = ReadYaml(os.path.join(Config.test_datas_dir, "test_data_02.yaml")).read()
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
    def test_case_01(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_video_stop()
        page.assert_video_stop(yaml_data[1]["断言元素定位"])

    """开始视频播放"""
    @PrettyAllure.PrettyAllureWarpper
    @pytest.mark.parametrize("CaseData", [yaml_data[2]])
    def test_case_02(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_video_start()
        page.assert_video_start(yaml_data[2]["断言元素定位"])

    """抓图"""
    @PrettyAllure.PrettyAllureWarpper
    @pytest.mark.parametrize("CaseData", [yaml_data[3]])
    def test_case_03(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_screenshot()
        page.assert_click_screenshot(yaml_data[3]["断言元素定位"])

    """关闭抓图弹窗"""
    @PrettyAllure.PrettyAllureWarpper
    @pytest.mark.parametrize("CaseData", [yaml_data[4]])
    def test_case_04(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_screenshot_close()
        page.assert_click_screenshot_close(yaml_data[4]["断言元素定位"])

    """开始录像"""
    @PrettyAllure.PrettyAllureWarpper
    @pytest.mark.parametrize("CaseData", [yaml_data[5]])
    def test_case_05(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_start_record()
        page.assert_start_record(yaml_data[5]["断言元素定位"])
        sleep(5)

    """停止录像"""
    @PrettyAllure.PrettyAllureWarpper
    @pytest.mark.parametrize("CaseData", [yaml_data[6]])
    def test_case_06(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_stop_record()
        page.assert_stop_record(yaml_data[6]["断言元素定位"])

    """连续抓图"""
    @PrettyAllure.PrettyAllureWarpper
    @pytest.mark.parametrize("CaseData", [yaml_data[7]])
    def test_case_07(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_continuous_snapshot()
        page.assert_continuous_snapshot(yaml_data[7]["断言元素定位"])

    """自动聚焦"""
    @PrettyAllure.PrettyAllureWarpper
    @pytest.mark.parametrize("CaseData", [yaml_data[8]])
    def test_case_08(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_auto_focus()
        page.assert_auto_focus(yaml_data[8]["断言元素定位"])

    """电子变倍3X"""
    @PrettyAllure.PrettyAllureWarpper
    @pytest.mark.parametrize("CaseData", [yaml_data[9]])
    def test_case_09(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_electronic_amplification()
        page.select_electronic_amplification_3X()
        page.assert_electronic_amplification(yaml_data[9]["断言元素定位"])

    """电子变倍2X"""
    @PrettyAllure.PrettyAllureWarpper
    @pytest.mark.parametrize("CaseData", [yaml_data[10]])
    def test_case_10(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_electronic_amplification()
        page.select_electronic_amplification_2X()
        page.assert_electronic_amplification(yaml_data[10]["断言元素定位"])

    """电子变倍1X"""
    @PrettyAllure.PrettyAllureWarpper
    @pytest.mark.parametrize("CaseData", [yaml_data[11]])
    def test_case_11(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_electronic_amplification()
        page.select_electronic_amplification_1X()
        page.assert_electronic_amplification(yaml_data[11]["断言元素定位"])

    """开启温度曲线(近4小时最高温)"""
    @PrettyAllure.PrettyAllureWarpper
    @pytest.mark.parametrize("CaseData", [yaml_data[12]])
    def test_case_12(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_real_time_temp_curve()
        page.assert_real_time_temp_curve_start(yaml_data[12]["断言元素定位"])

    """近4小时最低温"""
    @PrettyAllure.PrettyAllureWarpper
    @pytest.mark.parametrize("CaseData", [yaml_data[13]])
    def test_case_13(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_object_temp_select()
        page.select_object_temp_mix()
        page.assert_select_object_temp_success(yaml_data[13]["断言元素定位"])

    """近4小时平均温"""
    @PrettyAllure.PrettyAllureWarpper
    @pytest.mark.parametrize("CaseData", [yaml_data[14]])
    def test_case_14(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_object_temp_select()
        page.select_object_temp_avg()
        page.assert_select_object_temp_success(yaml_data[14]["断言元素定位"])

    """近24小时平均温"""
    @PrettyAllure.PrettyAllureWarpper
    @pytest.mark.parametrize("CaseData", [yaml_data[15]])
    def test_case_15(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_time_range_select()
        page.select_time_range_24H()
        page.assert_select_time_range_success(yaml_data[15]["断言元素定位"])

    """近24小时最低温"""
    @PrettyAllure.PrettyAllureWarpper
    @pytest.mark.parametrize("CaseData", [yaml_data[16]])
    def test_case_16(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_object_temp_select()
        page.select_object_temp_mix()
        page.assert_select_object_temp_success(yaml_data[16]["断言元素定位"])

    """近24小时最高温"""
    @PrettyAllure.PrettyAllureWarpper
    @pytest.mark.parametrize("CaseData", [yaml_data[17]])
    def test_case_17(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_object_temp_select()
        page.select_object_temp_max()
        page.assert_select_object_temp_success(yaml_data[17]["断言元素定位"])

    """近72小时最高温"""
    @PrettyAllure.PrettyAllureWarpper
    @pytest.mark.parametrize("CaseData", [yaml_data[18]])
    def test_case_18(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_time_range_select()
        page.select_time_range_72H()
        page.assert_select_time_range_success(yaml_data[18]["断言元素定位"])

    """近72小时最低温"""
    @PrettyAllure.PrettyAllureWarpper
    @pytest.mark.parametrize("CaseData", [yaml_data[19]])
    def test_case_19(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_object_temp_select()
        page.select_object_temp_mix()
        page.assert_select_object_temp_success(yaml_data[19]["断言元素定位"])

    """近72小时平均温"""
    @PrettyAllure.PrettyAllureWarpper
    @pytest.mark.parametrize("CaseData", [yaml_data[20]])
    def test_case_20(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_object_temp_select()
        page.select_object_temp_avg()
        page.assert_select_object_temp_success(yaml_data[20]["断言元素定位"])

    """关闭实时温度曲线"""
    @PrettyAllure.PrettyAllureWarpper
    @pytest.mark.parametrize("CaseData", [yaml_data[21]])
    def test_case_21(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_real_time_temp_curve()
        page.assert_real_time_temp_curve_stop(yaml_data[21]["断言元素定位"])

    """窗口填充"""
    @PrettyAllure.PrettyAllureWarpper
    @pytest.mark.parametrize("CaseData", [yaml_data[22]])
    def test_case_22(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_fill_or_adapt()
        page.assert_fill_or_adapt(yaml_data[22]["断言元素定位"])

    """窗口适应"""
    @PrettyAllure.PrettyAllureWarpper
    @pytest.mark.parametrize("CaseData", [yaml_data[23]])
    def test_case_23(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_fill_or_adapt()
        page.assert_fill_or_adapt(yaml_data[23]["断言元素定位"])

    """窗口填充"""
    @PrettyAllure.PrettyAllureWarpper
    @pytest.mark.parametrize("CaseData", [yaml_data[24]])
    def test_case_24(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_full_screen()

    """退出窗口填充"""
    @PrettyAllure.PrettyAllureWarpper
    @pytest.mark.parametrize("CaseData", [yaml_data[25]])
    def test_case_25(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_full_screen_exit()

