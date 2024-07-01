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

    """系统标题为空"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[3]])
    def test_case_04(self, page, CaseData: dict):
        page = LoginPage(page)
        page.browser_operation()
        page.goto_login(CaseData["url地址"])
        print(CaseData["断言元素定位"])
        page.assert_system_title(CaseData["断言元素定位"])

    """版权所属为空"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[4]])
    def test_case_05(self, page, CaseData: dict):
        page = LoginPage(page)
        page.browser_operation()
        page.goto_login(CaseData["url地址"])
        print(CaseData["断言元素定位"])
        page.assert_copyright_ownership(CaseData["断言元素定位"])

    """质感logo"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[5]])
    def test_case_06(self, page, CaseData: dict):
        page = LoginPage(page)
        page.browser_operation()
        page.goto_login(CaseData["url地址"])
        page.assert_images_equal(CaseData["断言元素定位"])

    """登录时不输入账号密码"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[6]])
    def test_case_07(self, page, CaseData: dict):
        page = LoginPage(page)
        page.browser_operation()
        page.goto_login(CaseData["url地址"])
        page.click_login_button()
        page.assert_login_button(CaseData["断言元素定位"])

    """账号密码提示内容"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[7]])
    def test_case_08(self, page, CaseData: dict):
        page = LoginPage(page)
        page.browser_operation()
        page.goto_login(CaseData["url地址"])
        page.assert_username_placeholder(CaseData["断言元素定位"][0])
        page.assert_password_placeholder(CaseData["断言元素定位"][1])

    """账户输入小于32个字符"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[8]])
    def test_case_09(self, page, CaseData: dict):
        page = LoginPage(page)
        page.browser_operation()
        page.goto_login(CaseData["url地址"])
        page.fill_username(CaseData["断言元素定位"][0])
        page.assert_username(CaseData["断言元素定位"][1])

    """账户输入大于32个字符"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[9]])
    def test_case_10(self, page, CaseData: dict):
        page = LoginPage(page)
        page.browser_operation()
        page.goto_login(CaseData["url地址"])
        page.fill_username(CaseData["断言元素定位"][0])
        page.assert_username(CaseData["断言元素定位"][1])

    """密码输入小于32个字符"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[10]])
    def test_case_11(self, page, CaseData: dict):
        page = LoginPage(page)
        page.browser_operation()
        page.goto_login(CaseData["url地址"])
        page.fill_password(CaseData["断言元素定位"][0])
        page.assert_password(CaseData["断言元素定位"][1])

    """密码输入大于32个字符"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[11]])
    def test_case_12(self, page, CaseData: dict):
        page = LoginPage(page)
        page.browser_operation()
        page.goto_login(CaseData["url地址"])
        page.fill_password(CaseData["断言元素定位"][0])
        page.assert_password(CaseData["断言元素定位"][1])

    """登录时输入用户名不输入密码"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[12]])
    def test_case_13(self, page, CaseData: dict):
        page = LoginPage(page)
        page.browser_operation()
        page.goto_login(CaseData["url地址"])
        page.fill_username(CaseData["账号"])
        page.assert_login_button(CaseData["断言元素定位"])

    """登录时不输入用户名但输入密码"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[13]])
    def test_case_14(self, page, CaseData: dict):
        page = LoginPage(page)
        page.browser_operation()
        page.goto_login(CaseData["url地址"])
        page.fill_password(CaseData["密码"])
        page.assert_login_button(CaseData["断言元素定位"])

    """输入错误用户名登录"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[14]])
    def test_case_15(self, page, CaseData: dict):
        page = LoginPage(page)
        page.browser_operation()
        page.goto_login(CaseData["url地址"])
        page.fill_username(CaseData["账号"])
        page.fill_password(CaseData["密码"])
        page.click_login_button()
        page.assert_username_error()
        page.click_warning_confirm()
        page.assert_username_error2()

    """输入错误密码登录"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[15]])
    def test_case_16(self, page, CaseData: dict):
        page = LoginPage(page)
        page.browser_operation()
        page.goto_login(CaseData["url地址"])
        page.fill_username(CaseData["账号"])
        page.fill_password(CaseData["密码"])
        page.click_login_button()
        page.assert_password_error()
        page.click_warning_confirm()
        page.assert_password_error2()

    """账户密码输入框中删除按钮功能正常"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[16]])
    def test_case_17(self, page, CaseData: dict):
        page = LoginPage(page)
        page.browser_operation()
        page.goto_login(CaseData["url地址"])
        page.fill_username(CaseData["账号"])
        page.fill_password(CaseData["密码"])
        page.assert_username(CaseData["账号"])
        page.assert_password(CaseData["密码"])
        page.clear_username()
        page.clear_password()
        page.assert_username(CaseData["断言元素定位"])
        page.assert_password(CaseData["断言元素定位"])
        page.fill_username(CaseData["账号"])
        page.fill_password(CaseData["密码"])
        page.assert_username(CaseData["账号"])
        page.assert_password(CaseData["密码"])

    """记住密码未勾选"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[17]])
    def test_case_18(self, page, CaseData: dict):
        page = LoginPage(page)
        page.browser_operation()
        page.goto_login(CaseData["url地址"])
        page.fill_username(CaseData["账号"])
        page.fill_password(CaseData["密码"])
        page.assert_remember_password_off(CaseData["断言元素定位"])
        page.click_login_button()
        page.click_admin()
        page.click_logout()
        page.click_confirm_exit()
        page.assert_username("")
        page.assert_password("")

    """记住密码已勾选"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[18]])
    def test_case_19(self, page, CaseData: dict):
        page = LoginPage(page)
        page.browser_operation()
        page.goto_login(CaseData["url地址"])
        page.fill_username(CaseData["账号"])
        page.fill_password(CaseData["密码"])
        page.click_remember_password()
        page.assert_remember_password_on(CaseData["断言元素定位"])
        page.click_login_button()
        page.click_admin()
        page.click_logout()
        page.click_confirm_exit()
        page.assert_username(CaseData["账号"])
        page.assert_password(CaseData["密码"])

    """多次使用错误的密码登录账号被锁定"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[19]])
    def test_case_20(self, page, CaseData: dict):
        page = LoginPage(page)
        page.browser_operation()
        page.goto_login(CaseData["url地址"])
        page.fill_username(CaseData["账号"])
        page.fill_password(CaseData["密码"])
        for i in range(4):
            page.click_login_button()
            page.click_warning_confirm()
        page.click_login_button()
        page.assert_account_lock()
        page.click_warning_confirm()

    """达到账户锁定时间之后可以正常登录"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[20]])
    def test_case_21(self, page, CaseData: dict):
        page = LoginPage(page)
        page.browser_operation()
        page.goto_login(CaseData["url地址"])
        page.fill_username(CaseData["账号"])
        page.fill_password(CaseData["密码"])
        for i in range(4):
            page.click_login_button()
            page.click_warning_confirm()
        page.click_login_button()
        page.assert_account_lock()
        page.click_warning_confirm()
        sleep(30)
        page.browser_operation()
        page.fill_username("admin")
        page.fill_password("admin123")
        page.click_login_button()
        page.assert_login_success(CaseData["断言元素定位"])

    """语言切换-英文"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[21]])
    def test_case_22(self, page, CaseData: dict):
        page = LoginPage(page)
        page.browser_operation()
        page.goto_login(CaseData["url地址"])
        page.click_switch_button()
        page.click_switch_english()
        page.assert_switch_language(CaseData["断言元素定位"])

    """语言切换-中文"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[22]])
    def test_case_23(self, page, CaseData: dict):
        page = LoginPage(page)
        page.browser_operation()
        page.goto_login(CaseData["url地址"])
        page.click_switch_button()
        page.click_switch_chinese()
        page.assert_switch_language(CaseData["断言元素定位"])

    """密码-密文"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[23]])
    def test_case_24(self, page, CaseData: dict):
        page = LoginPage(page)
        page.browser_operation()
        page.goto_login(CaseData["url地址"])
        page.assert_passwd__visible(CaseData["断言元素定位"])

    """密码-明文"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[24]])
    def test_case_25(self, page, CaseData: dict):
        page = LoginPage(page)
        page.browser_operation()
        page.goto_login(CaseData["url地址"])
        page.click_passwd__visible()
        page.assert_passwd__visible(CaseData["断言元素定位"])





