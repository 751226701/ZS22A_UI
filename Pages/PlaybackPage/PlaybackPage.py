# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/1/31 8:47
# @File :PlaybackPage.py
# @Project : ZS22A_UI

import os.path
import re
import allure
from time import sleep
from Common.Common import Common
from Config.Config import Config
from Common.CompareImage import download_image
from playwright.sync_api import expect


class PlaybackPage(Common):
    __file_type_video = "视频"
    __file_type_image = "图片"
    __channel_vl = "可见光"
    __channel_ir = "红外"
    __event_type = ("form", r"事件类型.*", "请选择")
    __all_documents = "全部文件"
    __object_temp = ("list", "对象温度")
    __global_temp = "全局温度"
    __object_temp_dif = "对象温差"
    __manual_recording = ("list", "手动录像")
    __query = ".icon-file"
    __play_video = "div:nth-child(3) > i:nth-child(3)"
    __next_video = "i:nth-child(4)"
    __previous_video = "div:nth-child(3) > i:nth-child(2)"
    __stop_play_video = "div:nth-child(3) > i"
    __select_magnification = ("请选择", 1)
    __speed_1 = "倍速1.0X"
    __speed_2 = "倍速1.2X"
    __speed_3 = "倍速1.5X"
    __speed_4 = "倍速2.0X"
    __play_photos = ".icon-play"
    __stop_play_photos = ".icon-pause"
    __next_photo = ".opr-box-tool > i:nth-child(3)"
    __previous_photo = ".el-tooltip"

    @allure.step("文件类型选择视频")
    def select_file_type_video(self):
        self.page.get_by_role("radio", name=self.__file_type_video).click()

    @allure.step("文件类型选择图片")
    def select_file_type_image(self):
        self.page.get_by_role("radio", name=self.__file_type_image).click()

    @allure.step("通道类型选择可见光")
    def select_channel_vl(self):
        self.page.get_by_role("radio", name=self.__channel_vl).click()

    @allure.step("通道类型选择红外")
    def select_channel_ir(self):
        self.page.get_by_role("radio", name=self.__channel_ir).click()

    @allure.step("事件类型选择")
    def select_event_type(self):
        text_pattern = re.compile(r"事件类型.*")
        self.page.locator("form").filter(has_text=text_pattern).locator("i").click()

    @allure.step("选择全部文件")
    def select_all_documents(self):
        self.page.get_by_text(self.__all_documents).click()

    @allure.step("选择对象温度")
    def select_object_temp(self):
        self.page.get_by_role("list").get_by_text(self.__object_temp[1]).click()

    @allure.step("选择全局温度")
    def select_global_temp(self):
        self.page.locator("li").filter(has_text="全局温度").click()

    @allure.step("选择对象温差")
    def select_object_temp_dif(self):
        self.page.get_by_text(self.__object_temp_dif).click()

    @allure.step("选择手动录像")
    def select_manual_recording(self):
        self.page.get_by_role("list").get_by_text(self.__manual_recording[1]).click()

    @allure.step("点击查询")
    def click_query(self):
        self._click(self.__query)

    @allure.step("下载回放视频")
    def download_playback_video(self):
        self.page.get_by_role("row").locator("i").nth(1).click()

    @allure.step("下载回放照片")
    def download_playback_picture(self):
        self.page.get_by_role("row").locator("i").nth(1).click()

    @allure.step("选中视频")
    def select_video(self, value):
        """
        :param value: 选中哪一条视频
        :return: 无
        """
        self.page.get_by_role("row").nth(value).click()

    @allure.step("点击播放")
    def click_play_video(self):
        self._click(self.__play_video)

    @allure.step("下一条视频")
    def next_video(self):
        self._click(self.__next_video)

    @allure.step("上一条视频")
    def previous_video(self):
        self._click(self.__previous_video)

    @allure.step("停止播放")
    def stop_play_video(self):
        self._click(self.__stop_play_video)

    @allure.step("断言已停止播放")   # 不适用
    def assert_stop_play_video(self, value):
        target_element = self.page.query_selector('div.opr-box-tool > i:nth-child(2)')
        if target_element:
            class_value = target_element.get_attribute('class')
            print("Class值:", class_value)

    @allure.step("倍率选择")
    def select_magnification(self):
        self. page.get_by_placeholder("请选择").nth(1).click()

    @allure.step("倍率选择1.0X")
    def magnification_1(self):
        self.page.get_by_text(self.__speed_1).click()

    @allure.step("倍率选择1.2X")
    def magnification_2(self):
        self.page.get_by_text(self.__speed_2).click()

    @allure.step("倍率选择1.5X")
    def magnification_3(self):
        self.page.get_by_text(self.__speed_3).click()

    @allure.step("倍率选择2.0X")
    def magnification_4(self):
        self.page.get_by_text(self.__speed_4).click()

    @allure.step("全屏播放")
    def full_screen_play(self):
        self._click(".icon-full")

    @allure.step("退出全屏播放")
    def stop_full_screen_play(self):
        self._click(".icon-full")

    @allure.step("播放图片")
    def play_photos(self):
        self._click(self.__play_photos)

    @allure.step("停止播放图片")
    def stop_play_photos(self):
        self._click(self.__stop_play_photos)

    @allure.step("下一张图片")
    def next_photo(self):
        self. page.locator(self.__next_photo).first.click()

    @allure.step("上一张图片")
    def previous_photo(self):
        self.page.locator(self.__previous_photo).first.click()

    @allure.step("断言列表个数大于1")
    def assert_num_list(self, value):
        element_count = len(self.page.query_selector_all(value))
        assert element_count >= 1

    @allure.step("断言已选中第一个视频元素")
    def assert_selected_video1(self, value):
        element = self.page.query_selector(".el-table__row")
        class_value = element.get_attribute("class")
        assert class_value == value

    @allure.step("断言已选中第二个视频元素")
    def assert_selected_video2(self, value):
        element = self.page.query_selector_all(".el-table__row")
        class_value = element[1].get_attribute("class")
        assert class_value == value

    @allure.step("断言视频倍率")
    def assert_magnification(self, value):
        expect(self.page.get_by_placeholder("请选择").nth(1)).to_have_value(value)

    @allure.step("断言全屏状态")
    def assert_full_screen_status(self, value):
        assert self.page.query_selector(".icon-full").get_attribute("class") == value

    @allure.step("断言当前所选中照片位置")
    def assert_selected_photo(self, value):
        element_list = self.page.query_selector_all(".el-table__row")
        for i, values in enumerate(element_list):
            class_value = values.get_attribute("class")
            if class_value == "el-table__row current-row":
                assert i == value









