#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: 刘涛
# @time: 2024/1/15 11:16
# @file: test_case_01.py
# @project: ZS22A_UI

import os
import pytest
import allure
from time import sleep
from playwright.sync_api import sync_playwright
from Pages.LoginPage.LoginPage import LoginPage
from Common.ReadYaml import ReadYaml
from Common.AllurePretty import PrettyAllure
from Config.Config import Config
Trace = Config.trace1
yaml_data = ReadYaml(os.path.join(Config.test_datas_dir, "test_data_01.yaml")).read()

"""执行登录模块测试"""
class TestLogin:
    """root/admin/user用户登录"""
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
        sleep(300)
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

    # """进入修改密码页面"""
    # @PrettyAllure.PrettyAllureWrapper
    # @pytest.mark.parametrize("CaseData", [yaml_data[25]])
    # def test_case_26(self, page, CaseData: dict):
    #     page = LoginPage(page)
    #     page.browser_operation()
    #     page.goto_login(CaseData["url地址"])
    #     page.fill_username(CaseData["账号"])
    #     page.fill_password(CaseData["密码"])
    #     page.click_login_button()
    #     page.click_admin()
    #     page.click_change_password()
    #     page.assert_change_password_notify_on()

"""***************************************************************************************************************"""

pageobject = None
@allure.step("登录")
def login(pageobject, url, user, passwd):
    pageobject.goto(url)
    pageobject.get_by_placeholder("请输入用户名").fill(user)
    pageobject.get_by_placeholder("请输入密码").fill(passwd)
    pageobject.wait_for_timeout(3000)
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
            download_dir = Config.test_download_dir
            try:
                pageobject.on('download',
                              lambda download: download.save_as(os.path.join(download_dir, download.suggested_filename)))
            except Exception as e:
                print(f"保存失败：{e}")
            login(pageobject, yaml_data[1]["url地址"], yaml_data[1]["账号"], yaml_data[1]["密码"])
        yield pageobject
        pageobject = None
        if Trace:
            context.tracing.stop(path="trace1.zip")
        else:
            pass
        context.close()
        browser.close()

class TestLoginEx:
    """进入修改密码页面"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[25]])
    def test_case_26(self, page, CaseData: dict):
        page = LoginPage(page)
        page.click_admin()
        page.click_change_password()
        page.assert_change_password_notify_on()
        page.click_cancel()

    """修改密码-取消"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[26]])
    def test_case_27(self, page, CaseData: dict):
        page = LoginPage(page)
        page.click_admin()
        page.click_change_password()
        page.click_cancel()
        page.assert_change_password__notify_off()

    """修改密码-点击X"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[27]])
    def test_case_28(self, page, CaseData: dict):
        page = LoginPage(page)
        page.click_admin()
        page.click_change_password()
        page.close_change_password_notify()
        page.assert_change_password__notify_off()

    """原始密码不输入"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[28]])
    def test_case_29(self, page, CaseData: dict):
        page = LoginPage(page)
        page.click_admin()
        page.click_change_password()
        page.fill_new_password("admin1234")
        page.fill_confirm_password("admin1234")
        page.click_confirm()
        page.assert_input_placeholder(CaseData["断言元素定位"])
        page.close_change_password_notify()

    """原始密码显示/隐藏"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[29]])
    def test_case_30(self, page, CaseData: dict):
        page = LoginPage(page)
        page.click_admin()
        page.click_change_password()
        page.fill_original_password(CaseData["密码"])
        page.assert_password_visible(1, CaseData["断言元素定位"][0])
        page.click_original_password_visible()
        page.assert_password_visible(1, CaseData["断言元素定位"][1])
        page.close_change_password_notify()

    """新密码不输入"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[30]])
    def test_case_31(self, page, CaseData: dict):
        page = LoginPage(page)
        page.click_admin()
        page.click_change_password()
        page.fill_original_password("admin123")
        page.fill_confirm_password("admin1234")
        page.click_confirm()
        page.assert_input_placeholder(CaseData["断言元素定位"])
        page.close_change_password_notify()

    """新密码输入长度刚好满足最小长度要求"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[31]])
    def test_case_32(self, page, CaseData: dict):
        page = LoginPage(page)
        page.click_admin()
        page.click_change_password()
        page.fill_new_password("123456")
        page.click_confirm()
        page.assert_input_placeholder2(CaseData["断言元素定位"])
        page.close_change_password_notify()

    """新密码输入长度小于6"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[32]])
    def test_case_33(self, page, CaseData: dict):
        page = LoginPage(page)
        page.click_admin()
        page.click_change_password()
        page.fill_new_password("12345")
        page.click_confirm()
        page.assert_input_placeholder(CaseData["断言元素定位"])
        page.close_change_password_notify()

    """新密码输入长度刚好满足最大长度要求"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[33]])
    def test_case_34(self, page, CaseData: dict):
        page = LoginPage(page)
        page.click_admin()
        page.click_change_password()
        page.fill_new_password("12345678901234567890")
        page.click_confirm()
        page.assert_input_placeholder2(CaseData["断言元素定位"])
        page.close_change_password_notify()

    """新密码输入长度大于20"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[34]])
    def test_case_35(self, page, CaseData: dict):
        page = LoginPage(page)
        page.click_admin()
        page.click_change_password()
        page.fill_new_password("123456789012345678901")
        page.click_confirm()
        page.assert_input_placeholder(CaseData["断言元素定位"])
        page.close_change_password_notify()

    """新密码输入特殊符号"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[35]])
    def test_case_36(self, page, CaseData: dict):
        page = LoginPage(page)
        page.click_admin()
        page.click_change_password()
        page.fill_new_password("!!!!!!")
        page.click_confirm()
        page.assert_input_placeholder2(CaseData["断言元素定位"])
        page.close_change_password_notify()

    """新密码输入长度正确的纯数字密码"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[36]])
    def test_case_37(self, page, CaseData: dict):
        page = LoginPage(page)
        page.click_admin()
        page.click_change_password()
        page.fill_new_password("123456")
        page.click_confirm()
        page.assert_input_placeholder2(CaseData["断言元素定位"])
        page.close_change_password_notify()

    """新密码输入长度正确的纯字母密码"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[37]])
    def test_case_38(self, page, CaseData: dict):
        page = LoginPage(page)
        page.click_admin()
        page.click_change_password()
        page.fill_new_password("qwertyUI")
        page.click_confirm()
        page.assert_input_placeholder2(CaseData["断言元素定位"])
        page.close_change_password_notify()

    """新密码输入长度正确的大小写和数字组合密码"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[38]])
    def test_case_39(self, page, CaseData: dict):
        page = LoginPage(page)
        page.click_admin()
        page.click_change_password()
        page.fill_new_password("Adm123")
        page.click_confirm()
        page.assert_input_placeholder2(CaseData["断言元素定位"])
        page.close_change_password_notify()

    """新密码输入长度正确的汉字"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[39]])
    def test_case_40(self, page, CaseData: dict):
        page = LoginPage(page)
        page.click_admin()
        page.click_change_password()
        page.fill_new_password("新密码测试中")
        page.click_confirm()
        page.assert_input_placeholder(CaseData["断言元素定位"])
        page.close_change_password_notify()

    """新密码显示/隐藏"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[40]])
    def test_case_41(self, page, CaseData: dict):
        page = LoginPage(page)
        page.browser_operation()
        page.goto_login(CaseData["url地址"])
        page.fill_username(CaseData["账号"])
        page.fill_password(CaseData["密码"])
        page.click_login_button()
        page.click_admin()
        page.click_change_password()
        page.fill_new_password("admin123")
        page.assert_password_visible(2, CaseData["断言元素定位"][0])
        page.click_new_password_visible()
        page.assert_password_visible(2, CaseData["断言元素定位"][1])
        page.close_change_password_notify()

    """确认密码不输入"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[41]])
    def test_case_42(self, page, CaseData: dict):
        page = LoginPage(page)
        page.click_admin()
        page.click_change_password()
        page.fill_original_password("admin123")
        page.fill_new_password("admin1234")
        page.click_confirm()
        page.assert_input_placeholder(CaseData["断言元素定位"])
        page.close_change_password_notify()

    """确认密码输入长度刚好满足最小长度要求"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[42]])
    def test_case_43(self, page, CaseData: dict):
        page = LoginPage(page)
        page.click_admin()
        page.click_change_password()
        page.fill_original_password("admin123")
        page.fill_new_password("admin1234")
        page.fill_confirm_password("123456")
        page.click_confirm()
        page.assert_input_placeholder2(CaseData["断言元素定位"])
        page.close_change_password_notify()

    """确认密码输入长度小于6"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[43]])
    def test_case_44(self, page, CaseData: dict):
        page = LoginPage(page)
        page.click_admin()
        page.click_change_password()
        page.fill_original_password("admin123")
        page.fill_new_password("123456")
        page.fill_confirm_password("12345")
        page.click_confirm()
        page.assert_input_placeholder(CaseData["断言元素定位"])
        page.close_change_password_notify()

    """确认密码输入长度刚好满足最大长度要求"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[44]])
    def test_case_45(self, page, CaseData: dict):
        page = LoginPage(page)
        page.click_admin()
        page.click_change_password()
        page.fill_original_password("admin123")
        page.fill_new_password("123456")
        page.fill_confirm_password("12345678901234567890")
        page.click_confirm()
        page.assert_input_placeholder2(CaseData["断言元素定位"])
        page.close_change_password_notify()

    """确认密码输入长度大于20"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[45]])
    def test_case_46(self, page, CaseData: dict):
        page = LoginPage(page)
        page.click_admin()
        page.click_change_password()
        page.fill_original_password("admin123")
        page.fill_new_password("123456")
        page.fill_confirm_password("123456789012345678901")
        page.click_confirm()
        page.assert_input_placeholder(CaseData["断言元素定位"])
        page.close_change_password_notify()

    """确认密码输入特殊符号"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[46]])
    def test_case_47(self, page, CaseData: dict):
        page = LoginPage(page)
        page.click_admin()
        page.click_change_password()
        page.fill_new_password("!!!!!!")
        page.fill_confirm_password("!!!!!!")
        page.click_confirm()
        page.assert_input_placeholder2(CaseData["断言元素定位"])
        page.close_change_password_notify()

    """确认密码输入长度正确的纯数字密码"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[47]])
    def test_case_48(self, page, CaseData: dict):
        page = LoginPage(page)
        page.click_admin()
        page.click_change_password()
        page.fill_new_password("123456")
        page.fill_confirm_password("123456")
        page.click_confirm()
        page.assert_input_placeholder2(CaseData["断言元素定位"])
        page.close_change_password_notify()

    """确认密码输入长度正确的纯字母密码"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[48]])
    def test_case_49(self, page, CaseData: dict):
        page = LoginPage(page)
        page.click_admin()
        page.click_change_password()
        page.fill_new_password("qwertyUI")
        page.fill_confirm_password("qwertyUI")
        page.click_confirm()
        page.assert_input_placeholder2(CaseData["断言元素定位"])
        page.close_change_password_notify()

    """确认密码输入长度正确的大小写和数字组合密码"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[49]])
    def test_case_50(self, page, CaseData: dict):
        page = LoginPage(page)
        page.click_admin()
        page.click_change_password()
        page.fill_new_password("Adm123")
        page.fill_confirm_password("Adm123")
        page.click_confirm()
        page.assert_input_placeholder2(CaseData["断言元素定位"])
        page.close_change_password_notify()

    """确认密码输入长度正确的汉字"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[50]])
    def test_case_51(self, page, CaseData: dict):
        page = LoginPage(page)
        page.click_admin()
        page.click_change_password()
        page.fill_new_password("新密码测试中")
        page.fill_confirm_password("新密码测试中")
        page.click_confirm()
        page.assert_input_placeholder(CaseData["断言元素定位"])
        page.close_change_password_notify()

    """确认密码显示/隐藏"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[51]])
    def test_case_52(self, page, CaseData: dict):
        page = LoginPage(page)
        page.browser_operation()
        page.goto_login(CaseData["url地址"])
        page.fill_username(CaseData["账号"])
        page.fill_password(CaseData["密码"])
        page.click_login_button()
        page.click_admin()
        page.click_change_password()
        page.fill_confirm_password("admin123")
        page.assert_password_visible(3, CaseData["断言元素定位"][0])
        page.click_confirm_password_visible()
        page.assert_password_visible(3, CaseData["断言元素定位"][1])
        page.close_change_password_notify()

    """确认密码与新密码不一致"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[52]])
    def test_case_53(self, page, CaseData: dict):
        page = LoginPage(page)
        page.click_admin()
        page.click_change_password()
        page.fill_new_password("admin123")
        page.fill_confirm_password("admin1234")
        page.click_confirm()
        page.assert_input_placeholder(CaseData["断言元素定位"])
        page.close_change_password_notify()

    """原始密码与新密码一致"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[53]])
    def test_case_54(self, page, CaseData: dict):
        page = LoginPage(page)
        page.click_admin()
        page.click_change_password()
        page.fill_original_password("admin123")
        page.fill_new_password("admin123")
        page.fill_confirm_password("admin123")
        page.click_confirm()
        page.assert_input_placeholder(CaseData["断言元素定位"])
        page.close_change_password_notify()

    """原始密码-新密码-确认密码均不满足条件"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[54]])
    def test_case_55(self, page, CaseData: dict):
        page = LoginPage(page)
        page.click_admin()
        page.click_change_password()
        page.fill_original_password("12345")
        page.fill_new_password("adm12")
        page.fill_confirm_password("admin123")
        page.click_confirm()
        page.assert_password_error_placeholder(0, CaseData["断言元素定位"][0])
        page.assert_password_error_placeholder(1, CaseData["断言元素定位"][1])
        page.assert_password_error_placeholder(2, CaseData["断言元素定位"][2])
        page.close_change_password_notify()

    """原始密码不对"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[55]])
    def test_case_56(self, page, CaseData: dict):
        page = LoginPage(page)
        page.click_admin()
        page.click_change_password()
        page.fill_original_password("123456")
        page.fill_new_password("admin123")
        page.fill_confirm_password("admin123")
        page.click_confirm()
        page.assert_input_placeholder(CaseData["断言元素定位"])

    """修改密码"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[56]])
    def test_case_57(self, page, CaseData: dict):
        page = LoginPage(page)
        page.click_admin()
        page.click_change_password()
        page.fill_original_password("admin123")
        page.fill_new_password("admin123456789")
        page.fill_confirm_password("admin123456789")
        page.click_confirm()

        page.fill_username("admin")
        page.fill_password("admin123456789")
        page.click_login_button()
        page.click_admin()
        page.click_change_password()
        page.fill_original_password("admin123456789")
        page.fill_new_password("admin123")
        page.fill_confirm_password("admin123")
        page.click_confirm()

        page.fill_username(CaseData["账号"])
        page.fill_password(CaseData["密码"])
        page.click_login_button()

    """帮助-中文"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[57]])
    def test_case_58(self, page, CaseData: dict):
        page = LoginPage(page)
        page.click_admin()
        page.click_help()

    """退出登录"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[58]])
    def test_case_59(self, page, CaseData: dict):
        page = LoginPage(page)
        page.click_admin()
        page.click_logout()
        page.click_confirm_exit()
        page.assert_logout_success()

    """退出登录-取消"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[59]])
    def test_case_60(self, page, CaseData: dict):
        page = LoginPage(page)
        page.browser_operation()
        page.goto_login(CaseData["url地址"])
        page.fill_username(CaseData["账号"])
        page.fill_password(CaseData["密码"])
        page.click_login_button()
        page.click_admin()
        page.click_logout()
        page.click_cancel()




















