#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: 刘涛
# @time: 2024/1/15 11:16
# @file: test_case_01.py
# @project: ZS22A_UI

import os
import pytest
from time import sleep
from Pages.LoginPage.LoginPage import LoginPage
from Common.ReadYaml import ReadYaml
from Common.AllurePretty import PrettyAllure
from Config.Config import Config

"""执行登录模块测试"""



class TestLogin:
    """root/admin/user用户登录"""
    yaml_data = ReadYaml(os.path.join(Config.test_datas_dir, "test_data_01.yaml")).read()

    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.smoking
    @pytest.mark.parametrize("CaseData", yaml_data[0:3])
    def test_case_1_3(self, page, CaseData: dict):
        page = LoginPage(page)
        page.browser_operation()
        page.goto_login(CaseData["url地址"])
        page.fill_username(CaseData["账号"])
        page.fill_password(CaseData["密码"])
        page.click_login_button()
        sleep(3)
        page.assert_login_success(CaseData["断言元素定位"])

    """语言切换-英文"""

    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[3]])
    def test_case_04(self, page, CaseData: dict):
        page = LoginPage(page)
        page.browser_operation()
        page.goto_login(CaseData["url地址"])
        page.click_switch_button()
        page.click_switch_english()
        page.assert_switch_language(CaseData["断言元素定位"])

    """语言切换-中文"""

    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[4]])
    def test_case_05(self, page, CaseData: dict):
        page = LoginPage(page)
        page.browser_operation()
        page.goto_login(CaseData["url地址"])
        page.click_switch_button()
        page.click_switch_chinese()
        page.assert_switch_language(CaseData["断言元素定位"])

    """密码-密文"""

    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[5]])
    def test_case_06(self, page, CaseData: dict):
        page = LoginPage(page)
        page.browser_operation()
        page.goto_login(CaseData["url地址"])
        page.assert_passwd__visible(CaseData["断言元素定位"])

    """密码-明文"""

    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[6]])
    def test_case_07(self, page, CaseData: dict):
        page = LoginPage(page)
        page.browser_operation()
        page.goto_login(CaseData["url地址"])
        page.click_passwd__visible()
        page.assert_passwd__visible(CaseData["断言元素定位"])

    """记住密码未勾选"""

    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[7]])
    def test_case_08(self, page, CaseData: dict):
        page = LoginPage(page)
        page.browser_operation()
        page.goto_login(CaseData["url地址"])
        page.assert_remember_password_off(CaseData["断言元素定位"])

    """记住密码已勾选"""

    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[8]])
    def test_case_09(self, page, CaseData: dict):
        page = LoginPage(page)
        page.browser_operation()
        page.goto_login(CaseData["url地址"])
        page.click_remember_password()
        page.assert_remember_password_on(CaseData["断言元素定位"])

    """质感logo"""

    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[9]])
    def test_case_10(self, page, CaseData: dict):
        page = LoginPage(page)
        page.browser_operation()
        page.goto_login(CaseData["url地址"])
        page.assert_images_equal(CaseData["断言元素定位"])

