#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: 刘涛
# @time: 2024/1/15 10:02
# @file: Common.py
# @project: ZS22A_UI

import os
import allure
import base64
import requests
from PIL import Image
from io import BytesIO
from playwright.sync_api import expect, Page
from Config.Config import Config


class Common:
    def __init__(self, page: Page):
        self.page = page

    def _goto_url(self, url):
        """打开网页"""
        self.page.goto(url)

    def _click(self, locator, frame_locator=None):
        """
        点击元素
        :param locator: 传入元素定位器
        :param frame_locator: 传入frame框架的的定位器，如果没有传入，则一般点击
        :return:
        """
        try:
            if frame_locator is not None:
                self.page.frame_locator(frame_locator).locator(locator).click()
            else:
                self.page.click(locator)
        except Exception as e:
            print(e)

    def _hover(self, locator, frame_locator=None):
        """
        鼠标悬浮
        :param locator: 传入元素定位器
        :param frame_locator: 传入frame框架的的定位器，如果没有传入，则一般点击
        :return:
        """
        try:
            if frame_locator is not None:
                self.page.frame_locator(frame_locator).locator(locator).hover()
            else:
                self.page.hover(locator)
        except Exception as e:
            print(e)

    def _fill(self, locator, value, frame_locator=None):
        """
        定位元素，输入内容
        :param locator:传入元素定位器
        :param value:传入输入的值
        :param frame_locator: 传入frame框架
        :return:
        """
        try:
            if frame_locator is not None:
                self.page.frame_locator(selector=frame_locator).locator(selector_or_locator=locator).fill(value)
            else:
                self.page.fill(selector=locator, value=value)
        except Exception as e:
            print(e)

    def _type(self, locator, value, frame_locator=None):
        """
        模拟人工输入，一个键一个键的输入
        :param locator:传入元素定位器
        :param value:传入输入的值
        :param frame_locator: 传入frame框架
        :return:
        """
        try:
            if frame_locator is not None:
                self.page.frame_locator(selector=frame_locator).locator(selector_or_locator=locator).type(text=value,
                                                                                                          delay=100)
            else:
                self.page.type(selector=locator, text=value, delay=100)
        except Exception as e:
            print(e)

    def _file(self, locator, files, frame_locator=None):
        """
        上传文件的方法
        :param locator: 定位器
        :param files: 单个文件名，或者列表存放多个文件
        :param frame_locator: iframe框架定位器，如果没有就不传
        :return:
        """
        try:
            if frame_locator is not None:
                self.page.frame_locator(frame_locator).locator(locator).set_input_files(files=files)
            else:
                self.page.locator(locator).set_input_files(files=files)
        except Exception as e:
            print(e)

    def _ele_to_be_visible(self, locator):
        """断言元素可见"""
        return expect(self.page.locator(locator)).to_be_visible()

    def _ele_to_be_visible_force(self, locator, frame_locator=None, timout: int = 5):
        """强制等待某个元素可见"""
        ele = None
        if frame_locator is not None:
            ele = self.page.frame_locator(frame_locator).locator(locator)
        else:
            ele = self.page.locator(locator)
        for t in range(0, timout):
            self.page.wait_for_timeout(500)
            if ele.is_visible():
                break
        else:
            raise Exception("元素未找到!")

    def _ele_is_checked(self, selector):
        """判断元素是否被选选中"""
        return self.page.is_checked(selector)

    def _browser_operation(self, reload=False, forward=False, back=False):
        """浏览器操作，reload 刷新，forward 前进，back 后退"""
        if reload:
            self.page.reload()
        if back:
            self.page.go_back()
        if forward:
            self.page.go_forward()

    def screenshot(self, path, full_page=True, locator=None):
        """截图功能，默认截取全屏，如果传入定位器表示截取元素"""
        if locator is not None:
            self.page.locator(locator).screenshot(path=path)
            return path
        self.page.screenshot(path=path, full_page=full_page)
        return path

    @staticmethod
    def savescreenshot(page, CaseData):
        """保存截图到固定路径，以用例标题命名"""
        filename = os.path.join(Config.test_screenshot_dir, f"{CaseData.get('用例标题')}.png")
        page.screenshot(path=filename)
        allure.attach.file(source=filename, name=CaseData.get('用例标题'), attachment_type=allure.attachment_type.PNG)

    @staticmethod
    def download_image(image_url, save_path):
        if image_url.startswith('data:image'):
            _, image_data = image_url.split(',', 1)
            image_bytes = base64.b64decode(image_data)
            with open(save_path, 'wb') as f:
                f.write(image_bytes)
        else:
            response = requests.get(image_url)
            with open(save_path, 'wb') as f:
                f.write(response.content)
