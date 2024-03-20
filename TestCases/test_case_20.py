# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/3/20 9:13
# @File :test_case_20
# @Project : ZS22A_UI

import os
import re
import allure
import pytest
from playwright.sync_api import sync_playwright
from Pages.SystemPage.SystemPage8 import SystemPage
from Common.ReadYaml import ReadYaml
from Common.AllurePretty import PrettyAllure
from Config.Config import Config

yaml_data = ReadYaml(os.path.join(Config.test_datas_dir, "test_data_20.yaml")).read()
logindata = yaml_data[0]
Trace = Config.trace20
pageobject = None
DOWNLOAD_FLAG = False

@allure.step("登录")
def login(pageobject, url, user, passwd):
    pageobject.goto(url)
    pageobject.get_by_placeholder("请输入用户名").fill(user)
    pageobject.get_by_placeholder("请输入密码").fill(passwd)
    pageobject.wait_for_timeout(3000)
    pageobject.get_by_role("button", name="登录").click()
    pageobject.get_by_text("系统管理").click()
    pageobject.get_by_text("系统配置", exact=True).click()
    pageobject.get_by_role("menuitem", name="网络设置").click()
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
            context.tracing.stop(path="trace20.zip")
        else:
            pass
        context.close()
        browser.close()


"""执行网络设置子模块测试"""

class TestAlarm:
    """设置主机名称"""

    @PrettyAllure.PrettyAllureWarpper
    @pytest.mark.parametrize("CaseData", [yaml_data[1]])
    def test_case_01(self, page, CaseData: dict):
        page = SystemPage(page)
        page.set_hostname("123")
        page.select_dhcp()
        page.select_static_ip()
        page.set_ipv4_address("192.168.1.1")
        page.set_ipv4_subnet_mask("192.168.1.1")
        page.set_ipv4_gateway("192.168.1.1")
        page.ipv6_enable_switch()
        page.ipv6_auto()
        page.ipv6_manual()
        page.set_ipv6_address("192.168.1.1")
        page.set_ipv6_subnet_mask("192.168.1.1")
        page.set_ipv6_gateway("192.168.1.1")
        page.set_primary_dns("192.168.1.1")
        page.set_secondary_dns("192.168.1.1")
        page.switch_to_smtp_setting()
        page.set_receiver("1", "751226701@qq.com")
        page.set_receiver("2", "751226701@qq.com")
        page.set_receiver("3", "751226701@qq.com")
        page.set_receiver("4", "751226701@qq.com")
        page.set_receiver("5", "751226701@qq.com")
        page.switch_to_28181_setting()
        page.select_protocol_udp()
        page.select_protocol_tcp()
        page.select_channel_1()
        page.select_channel_2()
        page.switch_to_whitelist_setting()
        page.add_ip("192.168.21.111")
        page.add_ip_segment("192.168.21.1",  "192.168.21.255")
        page.add_mac("1E:50:8F:C1:00:08")
        page.whitelist_enable_switch()
        page.select_all()
        page.click_clear()
































