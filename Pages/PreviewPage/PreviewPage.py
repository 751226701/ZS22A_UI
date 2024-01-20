#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: 刘涛
# @time: 2024/1/17 9:57
# @file: PreviewPage.py
# @project: ZS22A_UI

import os.path
import allure
from time import sleep
from Common.Common import Common
from Config.Config import Config
from Common.CompareImage import are_images_equal, download_image
from playwright.sync_api import expect


class PreviewPage(Common):
    __video_start = ".el-tooltip"
    __video_stop = ".el-tooltip"
    __screenshot = "i:nth-child(2)"
    __screenshot_close = ".el-icon-circle-close"

    @allure.step("点击暂停播放")
    def click_video_start(self):
        self._click(self.__video_stop)

    @allure.step("点击开始播放")
    def click_video_stop(self):
        sleep(1)
        self._click(self.__video_stop)

    @allure.step("点击抓图")
    def click_screenshot(self):
        self._click(self.__screenshot)

    @allure.step("点击关闭抓图框")
    def click_screenshot_close(self):
        self._click(self.__screenshot_close)
