#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: 刘涛
# @time: 2024/1/15 13:09
# @file: debug.py
# @project: ZS22A_UI

from time import sleep

import yaml
from playwright.sync_api import Playwright, sync_playwright, expect
import requests
import re
import os
import allure
import pytest
from time import sleep
from playwright.sync_api import sync_playwright
from Pages.PreviewPage.PreviewPage import PreviewPage
from Common.ReadYaml import ReadYaml
from Common.AllurePretty import PrettyAllure
from Config.Config import Config


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(
        headless=False,
        channel=Config.browser,
        args=['--start-maximized'],
        slow_mo=500)
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto("http://192.168.21.115/#/login")

    page.locator('.el-input__inner[placeholder="请输入用户名"]').fill("root")
    page.locator('input[type="password"].el-input__inner').fill("guide123")
    page.locator('.el-checkbox__input').click()
    sleep(4)
    page.locator('button:has-text("登录")').click()
    sleep(2)
    page.get_by_role("list").locator("i").first.click()
    page.locator(".scale-ir-box").click(position={"x": 152, "y": 209})
    page.locator(".scale-ir-box").click(position={"x": 255, "y": 338})

    # page.locator(".video-wrap > canvas").dblclick()
    # expect(page.locator("li:nth-child(5) > .el-tooltip")).to_be_visible()

    # ---------------------
    sleep(3)
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)



