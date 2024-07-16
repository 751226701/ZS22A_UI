# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/2/2 14:05
# @File :test_case_03.py
# @Project : ZS22A_UI

import os
import allure
import pytest
from playwright.sync_api import sync_playwright
from Pages.PlaybackPage.PlaybackPage import PlaybackPage
from Common.ReadYaml import ReadYaml
from Common.AllurePretty import PrettyAllure
from Config.Config import Config

yaml_data = ReadYaml(os.path.join(Config.test_datas_dir, "test_data_03.yaml"))
logindata = yaml_data.read()[0]
Trace = Config.trace3
pageobject = None
DOWNLOAD_FLAG = False

@allure.step("登录")
def login(pageobject, url, user, passwd):
    pageobject.goto(url)
    pageobject.get_by_placeholder("请输入用户名").fill(user)
    pageobject.get_by_placeholder("请输入密码").fill(passwd)
    pageobject.locator("label span").nth(1).click()
    pageobject.wait_for_timeout(3000)
    pageobject.get_by_role("button", name="登录").click()
    pageobject.get_by_text("回放管理").click()
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
            context.tracing.stop(path="trace3.zip")
        else:
            pass
        context.close()
        browser.close()

"""执行回放管理模块测试"""
class TestPlayBack:

    """搜索全部可见光视频"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_01"]))
    def test_case_01(self, page, CaseData: dict):
        page = PlaybackPage(page)
        page.click_query()
        page.page.wait_for_timeout(1000)
        page.click_query()
        page.assert_num_list(CaseData['断言元素定位'])

    """搜索对象温度可见光视频"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_02"]))
    def test_case_02(self, page, CaseData: dict):
        page = PlaybackPage(page)
        page.select_event_type()
        page.select_object_temp()
        page.click_query()
        page.assert_num_list(CaseData['断言元素定位'])

    """搜索全局温度可见光视频"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_03"]))
    def test_case_03(self, page, CaseData: dict):
        page = PlaybackPage(page)
        page.select_event_type()
        page.select_global_temp()
        page.click_query()
        page.assert_num_list(CaseData['断言元素定位'])

    """搜索对象温差可见光视频"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_04"]))
    def test_case_04(self, page, CaseData: dict):
        page = PlaybackPage(page)
        page.select_event_type()
        page.select_object_temp_dif()
        page.click_query()
        page.assert_num_list(CaseData['断言元素定位'])

    """搜索手动录像视频"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_05"]))
    def test_case_05(self, page, CaseData: dict):
        page = PlaybackPage(page)
        page.select_event_type()
        page.select_manual_recording()
        page.click_query()
        page.assert_num_list(CaseData['断言元素定位'])

    """搜索全部红外视频"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_06"]))
    def test_case_06(self, page, CaseData: dict):
        page = PlaybackPage(page)
        page.select_channel_ir()
        page.select_event_type()
        page.select_all_documents()
        page.click_query()
        page.assert_num_list(CaseData['断言元素定位'])

    """搜索对象温度红外视频"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_07"]))
    def test_case_07(self, page, CaseData: dict):
        page = PlaybackPage(page)
        page.select_channel_ir()
        page.select_event_type()
        page.select_object_temp()
        page.click_query()
        page.assert_num_list(CaseData['断言元素定位'])

    """搜索全局温度红外视频"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_08"]))
    def test_case_08(self, page, CaseData: dict):
        page = PlaybackPage(page)
        page.select_channel_ir()
        page.select_event_type()
        page.select_global_temp()
        page.click_query()
        page.assert_num_list(CaseData['断言元素定位'])

    """搜索对象温差红外视频"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_09"]))
    def test_case_09(self, page, CaseData: dict):
        page = PlaybackPage(page)
        page.select_channel_ir()
        page.select_event_type()
        page.select_object_temp_dif()
        page.click_query()
        page.assert_num_list(CaseData['断言元素定位'])

    """下载回放视频"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_10"]))
    def test_case_10(self, page, CaseData: dict):
        page = PlaybackPage(page)
        page.select_channel_ir()
        page.select_event_type()
        page.select_all_documents()
        page.click_query()
        page.download_playback_video()
        assert DOWNLOAD_FLAG == CaseData['断言元素定位']
        set_download_flag(False)

    """搜索全部可见光照片"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_11"]))
    def test_case_11(self, page, CaseData: dict):
        page = PlaybackPage(page)
        page.select_file_type_image()
        page.select_channel_vl()
        page.select_event_type()
        page.select_all_documents()
        page.click_query()

    """搜索对象温度可见光照片"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_12"]))
    def test_case_12(self, page, CaseData: dict):
        page = PlaybackPage(page)
        page.select_file_type_image()
        page.select_channel_vl()
        page.select_event_type()
        page.select_object_temp()
        page.click_query()

    """搜索全局温度可见光照片"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_13"]))
    def test_case_13(self, page, CaseData: dict):
        page = PlaybackPage(page)
        page.select_file_type_image()
        page.select_channel_vl()
        page.select_event_type()
        page.select_global_temp()
        page.click_query()

    """搜索对象温差可见光照片"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_14"]))
    def test_case_14(self, page, CaseData: dict):
        page = PlaybackPage(page)
        page.select_file_type_image()
        page.select_channel_vl()
        page.select_event_type()
        page.select_object_temp_dif()
        page.click_query()

    """搜索全部红外照片"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_15"]))
    def test_case_15(self, page, CaseData: dict):
        page = PlaybackPage(page)
        page.select_file_type_image()
        page.select_channel_ir()
        page.select_event_type()
        page.select_all_documents()
        page.click_query()

    """搜索对象温度红外照片"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_16"]))
    def test_case_16(self, page, CaseData: dict):
        page = PlaybackPage(page)
        page.select_file_type_image()
        page.select_channel_ir()
        page.select_event_type()
        page.select_object_temp()
        page.click_query()

    """搜索全局温度红外照片"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_17"]))
    def test_case_17(self, page, CaseData: dict):
        page = PlaybackPage(page)
        page.select_file_type_image()
        page.select_channel_ir()
        page.select_event_type()
        page.select_global_temp()
        page.click_query()

    """搜索对象温差红外照片"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_18"]))
    def test_case_18(self, page, CaseData: dict):
        page = PlaybackPage(page)
        page.select_file_type_image()
        page.select_channel_ir()
        page.select_event_type()
        page.select_object_temp_dif()
        page.click_query()

    """下载回放照片"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_19"]))
    def test_case_19(self, page, CaseData: dict):
        page = PlaybackPage(page)
        page.select_file_type_image()
        page.select_channel_vl()
        page.select_event_type()
        page.select_all_documents()
        page.click_query()
        page.download_playback_picture()
        assert DOWNLOAD_FLAG == CaseData['断言元素定位']
        set_download_flag(False)

    """选择第一条视频播放"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_20"]))
    def test_case_20(self, page, CaseData: dict):
        page = PlaybackPage(page)
        page.select_file_type_video()
        page.select_channel_ir()
        page.select_event_type()
        page.select_all_documents()
        page.click_query()
        page.select_video(1)  # 选择第一个视频
        page.page.wait_for_timeout(10000)
        page.assert_selected_video1(CaseData['断言元素定位'])

    """选择下一条视频"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_21"]))
    def test_case_21(self, page, CaseData: dict):
        page = PlaybackPage(page)
        page.select_file_type_video()
        page.select_channel_ir()
        page.select_event_type()
        page.select_all_documents()
        page.click_query()
        page.select_video(1)  # 选择第一个视频
        page.next_video()
        page.assert_selected_video2(CaseData['断言元素定位'])

    """选择上一条视频"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_22"]))
    def test_case_22(self, page, CaseData: dict):
        page = PlaybackPage(page)
        page.select_file_type_video()
        page.select_channel_ir()
        page.select_event_type()
        page.select_all_documents()
        page.click_query()
        page.select_video(2)  # 选择第一个视频
        page.previous_video()
        page.assert_selected_video1(CaseData['断言元素定位'])

    """停止播放视频"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_23"]))
    def test_case_23(self, page, CaseData: dict):
        page = PlaybackPage(page)
        page.select_file_type_video()
        page.select_channel_ir()
        page.select_event_type()
        page.select_all_documents()
        page.click_query()
        page.select_video(1)
        page.page.wait_for_timeout(5000)
        page.stop_play_video()

    """视频倍速1.2X"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_24"]))
    def test_case_24(self, page, CaseData: dict):
        page = PlaybackPage(page)
        page.select_file_type_video()
        page.select_channel_ir()
        page.select_event_type()
        page.select_all_documents()
        page.click_query()
        page.select_magnification()
        page.magnification_2()
        page.assert_magnification(CaseData['断言元素定位'])

    """视频倍速1.5X"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_25"]))
    def test_case_25(self, page, CaseData: dict):
        page = PlaybackPage(page)
        page.select_file_type_video()
        page.select_channel_ir()
        page.select_event_type()
        page.select_all_documents()
        page.click_query()
        page.select_magnification()
        page.magnification_3()
        page.assert_magnification(CaseData['断言元素定位'])

    """视频倍速2.0X"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_26"]))
    def test_case_26(self, page, CaseData: dict):
        page = PlaybackPage(page)
        page.select_file_type_video()
        page.select_channel_ir()
        page.select_event_type()
        page.select_all_documents()
        page.click_query()
        page.select_magnification()
        page.magnification_4()
        page.assert_magnification(CaseData['断言元素定位'])

    """视频倍速1.0X"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_27"]))
    def test_case_27(self, page, CaseData: dict):
        page = PlaybackPage(page)
        page.select_file_type_video()
        page.select_channel_ir()
        page.select_event_type()
        page.select_all_documents()
        page.click_query()
        page.select_magnification()
        page.magnification_1()
        page.assert_magnification(CaseData['断言元素定位'])

    """全屏播放"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_28"]))
    def test_case_28(self, page, CaseData: dict):
        page = PlaybackPage(page)
        page.select_file_type_video()
        page.select_channel_ir()
        page.select_event_type()
        page.select_all_documents()
        page.click_query()
        page.full_screen_play()
        page.assert_full_screen_status(CaseData['断言元素定位'])

    """退出全屏播放"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_29"]))
    def test_case_29(self, page, CaseData: dict):
        page = PlaybackPage(page)
        page.stop_full_screen_play()
        page.assert_full_screen_status(CaseData['断言元素定位'])

    """照片播放后暂停"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_30"]))
    def test_case_30(self, page, CaseData: dict):
        page = PlaybackPage(page)
        page.select_file_type_image()
        page.select_channel_ir()
        page.select_event_type()
        page.select_all_documents()
        page.click_query()
        page.play_photos()
        page.page.wait_for_timeout(10000)
        page.assert_selected_photo(CaseData['断言元素定位'])
        page.stop_play_photos()

    """下一张照片"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_31"]))
    def test_case_31(self, page, CaseData: dict):
        page = PlaybackPage(page)
        page.next_photo()
        page.assert_selected_photo(CaseData['断言元素定位'])

    """上一张照片"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_32"]))
    def test_case_32(self, page, CaseData: dict):
        page = PlaybackPage(page)
        page.previous_photo()
        page.assert_selected_photo(CaseData['断言元素定位'])






