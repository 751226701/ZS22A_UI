#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: 刘涛
# @time: 2024/1/15 10:46
# @file: LoginPage.py
# @project: ZS22A_UI

from PIL import Image
import io
import base64
import os.path
import allure
from time import sleep
from Common.Common import Common
from Config.Config import Config
from Common.CompareImage import compare_images, download_image
from playwright.sync_api import expect


class LoginPage(Common):
    # 元素定位器
    __username = '.el-input__inner[placeholder="请输入用户名"]'
    __password = 'input[type="password"].el-input__inner'
    __remember_password = '.el-checkbox__input'
    __login_button = 'button:has-text("登录")'
    __switch_button = "请选择"
    __switch_english = ("li", "English")
    __switch_chinese = "简体中文"
    __password_visible = "form i"

    def login(self):
        self.goto_login(Config.url)
        self.fill_username("root")
        self.fill_password("guide123")
        sleep(4)
        self.click_login_button()
        return self.page

    @allure.step("打开登录页面")
    def goto_login(self, url):
        self._goto_url(url)

    @allure.step("输入账号")
    def fill_username(self, value):
        self._fill(self.__username, value)

    @allure.step("清空账号内容")
    def clear_username(self):
        self. page.locator("form i").nth(1).click()

    @allure.step("断言账号输入内容")
    def assert_username(self, value):
        assert self.page.get_by_placeholder("请输入用户名").input_value() == value

    @allure.step("输入密码")
    def fill_password(self, value):
        self._fill(self.__password, value)

    @allure.step("清空密码内容")
    def clear_password(self):
        self.page.locator("form i").nth(3).click()

    @allure.step("断言密码输入内容")
    def assert_password(self, value):
        assert self.page.get_by_placeholder("请输入密码").input_value() == value

    @allure.step("断言账号输入框提示语")
    def assert_username_placeholder(self, value):
        all_inputs = self.page.query_selector_all('input[type="text"]')
        if all_inputs:
            placeholder_value = all_inputs[1].get_attribute('placeholder')
            assert placeholder_value == value

    @allure.step("断言密码输入框提示语")
    def assert_password_placeholder(self, value):
        pwd_value = self.page.locator('input[type="password"]').get_attribute('placeholder')
        assert pwd_value == value

    @allure.step("点击密码密文明文显示按钮")
    def click_passwd__visible(self):
        self.page.locator(self.__password_visible).nth(4).click()

    @allure.step("断言密码显示类型")
    def assert_passwd__visible(self, value):
        assert self.page.get_by_placeholder("请输入密码").get_attribute('type') == value

    @allure.step("记住密码")
    def click_remember_password(self):
        self._click(self.__remember_password)

    @allure.step("断言记住密码未勾选")
    def assert_remember_password_off(self, value):
        expect(self.page.locator(value).nth(1)).not_to_be_checked()

    @allure.step("断言记住密码已勾选")
    def assert_remember_password_on(self, value):
        expect(self.page.locator(value).nth(1)).to_be_checked()

    @allure.step("点击登录按钮")
    def click_login_button(self):
        sleep(4)
        self._click(self.__login_button)

    @allure.step("断言登录按钮不可点击")
    def assert_login_button(self, value):
        elements = self.page.locator(self.__login_button).get_attribute('class')
        if elements:
            classes = elements.split()
            assert value in classes

    @allure.step("断言错误账户登录提示弹窗可见")
    def assert_username_error(self):
        expect(self.page.get_by_text("用户名不存在！")).to_be_visible()

    @allure.step("断言错误账户登录提示弹窗不可见")
    def assert_username_error2(self):
        expect(self.page.get_by_text("用户名不存在！")).not_to_be_visible()

    @allure.step("断言错误密码登录提示弹窗可见")
    def assert_password_error(self):
        expect(self.page.get_by_text("密码不正确！")).to_be_visible()

    @allure.step("断言错误密码登录提示弹窗不可见")
    def assert_password_error2(self):
        expect(self.page.get_by_text("密码不正确！")).not_to_be_visible()

    @allure.step("点击警告弹窗确定按钮")
    def click_warning_confirm(self):
        self.page.get_by_role("button", name="确定").click()

    @allure.step("断言账户已被锁定")
    def assert_account_lock(self):
        expect(self.page.get_by_text("目前该账户已被锁定，请于稍后尝试登录！")).to_be_visible()

    @allure.step("断言系统标题为空格")
    def assert_system_title(self, value):
        text = self.page.locator(".title-name").text_content()
        assert text == value

    @allure.step("断言版权所属为空")
    def assert_copyright_ownership(self, value):
        text = self.page.locator(".version-box").text_content()
        assert text == value

    @allure.step("断言登录成功")
    def assert_login_success(self, locator):
        self._ele_to_be_visible(locator)

    @allure.step("点击选择语言")
    def click_switch_button(self):
        self.page.get_by_placeholder(self.__switch_button).click()

    @allure.step("语言切换为英文")
    def click_switch_english(self):
        self.page.locator(self.__switch_english[0]).filter(has_text=self.__switch_english[1]).click()

    @allure.step("语言切换为中文")
    def click_switch_chinese(self):
        self.page.get_by_text(self.__switch_chinese).click()

    @allure.step("断言是否切换成功")
    def assert_switch_language(self, value):
        expect(self.page.get_by_placeholder(value[0])).to_have_value(value[1])

    @allure.step("断言是否为高德红外logo")
    def assert_images_equal(self, value):
        """logo比对"""
        style_property = self.page.eval_on_selector(value, 'el => getComputedStyle(el).backgroundImage')
        image_url = style_property.replace('url("', '').replace('")', '')
        save_path = os.path.join(Config.test_files_dir, 'ACTUAL_LOGO.png')
        self.download_image(image_url, save_path)
        assert compare_images(os.path.join(Config.test_files_dir, 'ACTUAL_LOGO.png'),
                                os.path.join(Config.test_files_dir, 'EXPECT_LOGO.png'))

    def browser_operation(self, reload=True, forward=False, back=False):
        self._browser_operation(reload=reload, forward=forward, back=back)



















    @allure.step("点击admin用户")
    def click_admin(self):
        self.page.get_by_role("button", name="admin").click()

    @allure.step("点击退出登录")
    def click_logout(self):
        self.page.get_by_text("退出登录").click()

    @allure.step("点击确认退出")
    def click_confirm_exit(self):
        self.page.get_by_role("button", name="确认退出").click()


