# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/3/19 10:38
# @File :test_case_13
# @Project : ZS22A_UI

import os
import re
import allure
import pytest
from playwright.sync_api import sync_playwright
from Pages.SystemPage.SystemPage1 import SystemPage
from Common.ReadYaml import ReadYaml
from Common.AllurePretty import PrettyAllure
from Config.Config import Config

yaml_data = ReadYaml(os.path.join(Config.test_datas_dir, "test_data_13.yaml"))
logindata = yaml_data.read()[0]
Trace = Config.trace13
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
            context.tracing.stop(path="trace13.zip")
        else:
            pass
        context.close()
        browser.close()

"""执行画面设置子模块测试"""
class TestAlarm:

    """亮度默认值"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_01']))
    def test_case_01(self, page, CaseData: dict):
        page = SystemPage(page)
        page.click_default()
        page.click_ok()
        page.assert_vl_light(CaseData["断言元素定位"])

    """亮度设置0"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_02']))
    def test_case_02(self, page, CaseData: dict):
        page = SystemPage(page)
        page.set_vl_light("0")
        page.click_ok()
        page.click_refresh()
        page.assert_vl_light(CaseData["断言元素定位"])

    """亮度设置40"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_03']))
    def test_case_03(self, page, CaseData: dict):
        page = SystemPage(page)
        page.set_vl_light("40")
        page.click_ok()
        page.click_refresh()
        page.assert_vl_light(CaseData["断言元素定位"])

    """亮度设置100"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_04']))
    def test_case_04(self, page, CaseData: dict):
        page = SystemPage(page)
        page.set_vl_light("100")
        page.click_ok()
        page.click_refresh()
        page.assert_vl_light(CaseData["断言元素定位"])

    """亮度设置-1"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_05']))
    def test_case_05(self, page, CaseData: dict):
        page = SystemPage(page)
        page.set_vl_light("-1")
        page.click_ok()
        page.click_refresh()
        page.assert_vl_light(CaseData["断言元素定位"])

    """亮度设置101"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_06']))
    def test_case_06(self, page, CaseData: dict):
        page = SystemPage(page)
        page.set_vl_light("101")
        page.click_ok()
        page.click_refresh()
        page.assert_vl_light(CaseData["断言元素定位"])

    """对比度默认值"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_07']))
    def test_case_07(self, page, CaseData: dict):
        page = SystemPage(page)
        page.click_default()
        page.click_ok()
        page.assert_vl_contrast(CaseData["断言元素定位"])

    """对比度设置0"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_08']))
    def test_case_08(self, page, CaseData: dict):
        page = SystemPage(page)
        page.set_vl_contrast("0")
        page.click_ok()
        page.click_refresh()
        page.assert_vl_contrast(CaseData["断言元素定位"])

    """对比度设置40"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_09']))
    def test_case_09(self, page, CaseData: dict):
        page = SystemPage(page)
        page.set_vl_contrast("40")
        page.click_ok()
        page.click_refresh()
        page.assert_vl_contrast(CaseData["断言元素定位"])

    """对比度设置100"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_10']))
    def test_case_10(self, page, CaseData: dict):
        page = SystemPage(page)
        page.set_vl_contrast("100")
        page.click_ok()
        page.click_refresh()
        page.assert_vl_contrast(CaseData["断言元素定位"])

    """对比度设置-1"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_11']))
    def test_case_11(self, page, CaseData: dict):
        page = SystemPage(page)
        page.set_vl_contrast("-1")
        page.click_ok()
        page.click_refresh()
        page.assert_vl_contrast(CaseData["断言元素定位"])

    """对比度设置101"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_12']))
    def test_case_12(self, page, CaseData: dict):
        page = SystemPage(page)
        page.set_vl_contrast("101")
        page.click_ok()
        page.click_refresh()
        page.assert_vl_contrast(CaseData["断言元素定位"])

    """饱和度默认值"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_13']))
    def test_case_13(self, page, CaseData: dict):
        page = SystemPage(page)
        page.click_default()
        page.click_ok()
        page.assert_vl_saturation(CaseData["断言元素定位"])

    """饱和度设置0"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_14']))
    def test_case_14(self, page, CaseData: dict):
        page = SystemPage(page)
        page.set_vl_saturation("0")
        page.click_ok()
        page.click_refresh()
        page.assert_vl_saturation(CaseData["断言元素定位"])

    """饱和度设置40"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_15']))
    def test_case_15(self, page, CaseData: dict):
        page = SystemPage(page)
        page.set_vl_saturation("40")
        page.click_ok()
        page.click_refresh()
        page.assert_vl_saturation(CaseData["断言元素定位"])

    """饱和度设置100"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_16']))
    def test_case_16(self, page, CaseData: dict):
        page = SystemPage(page)
        page.set_vl_saturation("100")
        page.click_ok()
        page.click_refresh()
        page.assert_vl_saturation(CaseData["断言元素定位"])

    """饱和度设置-1"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_17']))
    def test_case_17(self, page, CaseData: dict):
        page = SystemPage(page)
        page.set_vl_saturation("-1")
        page.click_ok()
        page.click_refresh()
        page.assert_vl_saturation(CaseData["断言元素定位"])

    """饱和度设置101"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_18']))
    def test_case_18(self, page, CaseData: dict):
        page = SystemPage(page)
        page.set_vl_saturation("101")
        page.click_ok()
        page.click_refresh()
        page.assert_vl_saturation(CaseData["断言元素定位"])

    """锐度默认值"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_19']))
    def test_case_19(self, page, CaseData: dict):
        page = SystemPage(page)
        page.click_default()
        page.click_ok()
        page.assert_vl_sharpness(CaseData["断言元素定位"])

    """锐度设置0"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_20']))
    def test_case_20(self, page, CaseData: dict):
        page = SystemPage(page)
        page.set_vl_sharpness("0")
        page.click_ok()
        page.click_refresh()
        page.assert_vl_sharpness(CaseData["断言元素定位"])

    """锐度设置40"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_21']))
    def test_case_21(self, page, CaseData: dict):
        page = SystemPage(page)
        page.set_vl_sharpness("40")
        page.click_ok()
        page.click_refresh()
        page.assert_vl_sharpness(CaseData["断言元素定位"])

    """锐度设置100"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_22']))
    def test_case_22(self, page, CaseData: dict):
        page = SystemPage(page)
        page.set_vl_sharpness("100")
        page.click_ok()
        page.click_refresh()
        page.assert_vl_sharpness(CaseData["断言元素定位"])

    """锐度设置-1"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_23']))
    def test_case_23(self, page, CaseData: dict):
        page = SystemPage(page)
        page.set_vl_sharpness("-1")
        page.click_ok()
        page.click_refresh()
        page.assert_vl_sharpness(CaseData["断言元素定位"])

    """锐度设置101"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_24']))
    def test_case_24(self, page, CaseData: dict):
        page = SystemPage(page)
        page.set_vl_sharpness("101")
        page.click_ok()
        page.click_refresh()
        page.assert_vl_sharpness(CaseData["断言元素定位"])

    """背光补偿默认状态"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_25']))
    def test_case_25(self, page, CaseData: dict):
        page = SystemPage(page)
        page.click_default()
        page.click_ok()
        page.assert_backlight_compensation(CaseData["断言元素定位"])

    """背光补偿设置上"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_26']))
    def test_case_26(self, page, CaseData: dict):
        page = SystemPage(page)
        page.set_backlight_compensation()
        page.select_up()
        page.click_ok()
        page.click_refresh()
        page.assert_backlight_compensation(CaseData["断言元素定位"])

    """背光补偿设置下"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_27']))
    def test_case_27(self, page, CaseData: dict):
        page = SystemPage(page)
        page.set_backlight_compensation()
        page.select_down()
        page.click_ok()
        page.click_refresh()
        page.assert_backlight_compensation(CaseData["断言元素定位"])

    """背光补偿设置左"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_28']))
    def test_case_28(self, page, CaseData: dict):
        page = SystemPage(page)
        page.set_backlight_compensation()
        page.select_left()
        page.click_ok()
        page.click_refresh()
        page.assert_backlight_compensation(CaseData["断言元素定位"])

    """背光补偿设置右"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_29']))
    def test_case_29(self, page, CaseData: dict):
        page = SystemPage(page)
        page.set_backlight_compensation()
        page.select_right()
        page.click_ok()
        page.click_refresh()
        page.assert_backlight_compensation(CaseData["断言元素定位"])

    """背光补偿设置中心"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_30']))
    def test_case_30(self, page, CaseData: dict):
        page = SystemPage(page)
        page.set_backlight_compensation()
        page.select_center()
        page.click_ok()
        page.click_refresh()
        page.assert_backlight_compensation(CaseData["断言元素定位"])

    """背光补偿设置自动"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(['test_case_31']))
    def test_case_31(self, page, CaseData: dict):
        page = SystemPage(page)
        page.set_backlight_compensation()
        page.select_auto()
        page.click_ok()
        page.click_refresh()
        page.assert_backlight_compensation(CaseData["断言元素定位"])




























