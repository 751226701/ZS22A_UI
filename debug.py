#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: 刘涛
@time: 2024/1/15 13:09 
@file: debug.py
@project: ZS22A_UI
"""
from time import sleep
from playwright.sync_api import Playwright, sync_playwright, expect
import requests


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://192.168.21.153/#/login")

    page.locator('.el-input__inner[placeholder="请输入用户名"]').fill("root")
    page.locator('input[type="password"].el-input__inner').fill("guide123")
    page.locator('.el-checkbox__input').click()
    sleep(4)
    page.locator('button:has-text("登录")').click()
    page.locator("i:nth-child(2)").click()
    sleep(2)
    page.locator(".el-icon-circle-close").click()

    # ---------------------
    sleep(3)
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
