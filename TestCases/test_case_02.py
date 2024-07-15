#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: 刘涛
# @time: 2024/1/16 16:56
# @file: test_case_02.py
# @project: ZS22A_UI

import os
import allure
import pytest
from playwright.sync_api import sync_playwright, expect
from Pages.PreviewPage.PreviewPage import PreviewPage
from Common.ReadYaml import ReadYaml
from Common.AllurePretty import PrettyAllure
from Config.Config import Config

yaml_data = ReadYaml(os.path.join(Config.test_datas_dir, "test_data_02.yaml")).read()
logindata = yaml_data[0]
Trace = Config.trace2
pageobject = None

@allure.step("登录")
def login(pageobject, url, user, passwd):
    pageobject.goto(url)
    pageobject.get_by_placeholder("请输入用户名").fill(user)
    pageobject.get_by_placeholder("请输入密码").fill(passwd)
    pageobject.locator("label span").nth(1).click()
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
            login(pageobject, logindata["url地址"], logindata["账号"], logindata["密码"])
        yield pageobject
        pageobject = None
        if Trace:
            context.tracing.stop(path="trace2.zip")
        else:
            pass
        context.close()
        browser.close()


"""执行实时预览模块测试"""
class TestPreview:

    """暂停视频播放"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[1]])
    def test_case_01(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_video_stop()
        page.assert_video_stop(CaseData["断言元素定位"])

    """开始视频播放"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[2]])
    def test_case_02(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_video_start()
        page.assert_video_start(CaseData["断言元素定位"])

    """抓图"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[3]])
    def test_case_03(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_screenshot()
        page.assert_click_screenshot(CaseData["断言元素定位"])

    """关闭抓图弹窗"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[4]])
    def test_case_04(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_screenshot_close()
        page.assert_click_screenshot_close(CaseData["断言元素定位"])

    """可见光录像"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[5]])
    def test_case_05(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_start_record()
        # page.assert_start_ir_record(CaseData["断言元素定位"])
        page.assert_start_vl_record(CaseData["断言元素定位"])
        page.page.wait_for_timeout(5000)

    """可见光停止录像"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[6]])
    def test_case_06(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_stop_record()
        # page.assert_stop_ir_record(CaseData["断言元素定位"])
        page.assert_stop_vl_record(CaseData["断言元素定位"])

    """连续抓图"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[7]])
    def test_case_07(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_continuous_snapshot()
        page.assert_continuous_snapshot(CaseData["断言元素定位"])

    """自动聚焦"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[8]])
    def test_case_08(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_auto_focus()
        page.assert_auto_focus(CaseData["断言元素定位"])

    """可见光电子变倍"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[9]])
    def test_case_09(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_electronic_amplification()
        page.page.mouse.move(x=200, y=400)
        page.page.mouse.down()
        page.page.mouse.move(x=400, y=600)
        page.page.mouse.up()
        page.assert_electronic_amplification(CaseData["断言元素定位"], 1, 1)

    """红外电子变倍"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[10]])
    def test_case_10(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.page.mouse.move(x=1200, y=400)
        page.page.mouse.down()
        page.page.mouse.move(x=1400, y=600)
        page.page.mouse.up()
        page.assert_electronic_amplification(CaseData["断言元素定位"], 1, 1)

    """关闭电子变倍"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[11]])
    def test_case_11(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_electronic_amplification()
        page.assert_electronic_amplification(CaseData["断言元素定位"], 3, 1)

    """开启温度曲线(近4小时最高温)"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[12]])
    def test_case_12(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_real_time_temp_curve()
        page.assert_real_time_temp_curve_start(CaseData["断言元素定位"])

    """近4小时最低温"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[13]])
    def test_case_13(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_object_temp_select()
        page.select_object_temp_mix()
        page.assert_select_object_temp_success(CaseData["断言元素定位"])

    """近4小时平均温"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[14]])
    def test_case_14(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_object_temp_select()
        page.select_object_temp_avg()
        page.assert_select_object_temp_success(CaseData["断言元素定位"])

    """近24小时平均温"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[15]])
    def test_case_15(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_time_range_select()
        page.select_time_range_24H()
        page.assert_select_time_range_success(CaseData["断言元素定位"])

    """近24小时最低温"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[16]])
    def test_case_16(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_object_temp_select()
        page.select_object_temp_mix()
        page.assert_select_object_temp_success(CaseData["断言元素定位"])

    """近24小时最高温"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[17]])
    def test_case_17(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_object_temp_select()
        page.select_object_temp_max()
        page.assert_select_object_temp_success(CaseData["断言元素定位"])

    """近72小时最高温"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[18]])
    def test_case_18(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_time_range_select()
        page.select_time_range_72H()
        page.assert_select_time_range_success(CaseData["断言元素定位"])

    """近72小时最低温"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[19]])
    def test_case_19(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_object_temp_select()
        page.select_object_temp_mix()
        page.assert_select_object_temp_success(CaseData["断言元素定位"])

    """近72小时平均温"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[20]])
    def test_case_20(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_object_temp_select()
        page.select_object_temp_avg()
        page.assert_select_object_temp_success(CaseData["断言元素定位"])

    """关闭实时温度曲线"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[21]])
    def test_case_21(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_real_time_temp_curve()
        page.assert_real_time_temp_curve_stop(CaseData["断言元素定位"])

    """窗口填充"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[22]])
    def test_case_22(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_fill_or_adapt()
        page.assert_fill_or_adapt(CaseData["断言元素定位"])

    """窗口适应"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[23]])
    def test_case_23(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_fill_or_adapt()
        page.assert_fill_or_adapt(CaseData["断言元素定位"])

    """全屏显示"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[24]])
    def test_case_24(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_full_screen()
        page.page.wait_for_timeout(2000)
        page.assert_full_screen(CaseData["断言元素定位"], 1)

    """退出全屏显示"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[25]])
    def test_case_25(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_full_screen_exit()
        # page.page.wait_for_timeout(2000)
        # page.assert_full_screen(CaseData["断言元素定位"], 2)

    """单红外通道全屏显示"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[26]])
    def test_case_26(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_ir_full_screen()

    """单红外通道退出全屏显示"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[27]])
    def test_case_27(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_ir_full_screen_exit()

    """单可见光通道全屏显示"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[28]])
    def test_case_28(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_vl_full_screen()

    """单可见光通道退出全屏显示"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[29]])
    def test_case_29(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_vl_full_screen_exit()

    """视频暂停按钮悬浮文字"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[30]])
    def test_case_30(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.hover_video_stop()
        page.assert_float_text(CaseData["断言元素定位"])

    """视频暂停按钮悬浮文字"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[31]])
    def test_case_31(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_video_stop()
        page.hover_video_stop()
        page.assert_float_text(CaseData["断言元素定位"])

    """抓图按钮悬浮文字"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[32]])
    def test_case_32(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.hover_screenshot()
        page.assert_float_text(CaseData["断言元素定位"])

    """开始录像按钮悬浮文字"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[33]])
    def test_case_33(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.hover_start_record()
        page.assert_float_text(CaseData["断言元素定位"])

    """停止录像按钮悬浮文字"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[34]])
    def test_case_34(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_start_record()
        page.hover_start_record()
        page.assert_float_text(CaseData["断言元素定位"])
        page.click_stop_record()

    """连续抓图按钮悬浮文字"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[35]])
    def test_case_35(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.hover_continuous_snapshot()
        page.assert_float_text(CaseData["断言元素定位"])

    """局部放大按钮悬浮文字"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[36]])
    def test_case_36(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.hover_electronic_amplification()
        page.assert_float_text(CaseData["断言元素定位"])

    """实时温度曲线按钮悬浮文字"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[37]])
    def test_case_37(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.hover_real_time_temp_curve()
        page.assert_float_text(CaseData["断言元素定位"])

    """窗口适应按钮悬浮文字"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[38]])
    def test_case_38(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.hover_adapt_screen()
        page.assert_float_text(CaseData["断言元素定位"])

    """窗口填充按钮悬浮文字"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[39]])
    def test_case_39(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_fill_or_adapt()
        page.hover_fill_screen()
        page.assert_float_text(CaseData["断言元素定位"])
        page.click_fill_or_adapt()

    """全屏按钮悬浮文字"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[40]])
    def test_case_40(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.hover_full_screen()
        page.assert_float_text(CaseData["断言元素定位"])

    """进入到预览界面-默认选中可见光通道界面"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[41]])
    def test_case_41(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.page.get_by_text("回放管理").click()
        page.page.get_by_text("实时预览").click()
        page.assert_vl_pass(CaseData["断言元素定位"])

    """暂停后切换到其它界面"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[42]])
    def test_case_42(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_video_stop()
        page.hover_video_stop()
        page.assert_float_text(CaseData["断言元素定位"][0])
        page.page.get_by_text("回放管理").click()
        page.page.get_by_text("实时预览").click()
        page.hover_video_stop()
        page.assert_float_text(CaseData["断言元素定位"][1])

    """画面暂停时可抓图"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[43]])
    def test_case_43(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_video_stop()
        page.click_screenshot()
        page.assert_click_screenshot(CaseData["断言元素定位"])
        page.click_screenshot_close()

    """红外录像"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[44]])
    def test_case_44(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_ir_window()
        page.click_start_record()
        page.assert_start_ir_record(CaseData["断言元素定位"])
        page.page.wait_for_timeout(5000)

    """红外停止录像"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[45]])
    def test_case_45(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_stop_record()
        page.assert_stop_ir_record(CaseData["断言元素定位"])

    """录像过程中切换到其他网页或子菜单"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[46]])
    def test_case_46(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_start_record()
        page.goto_playback_management()
        page.page.wait_for_timeout(1000)
        page.goto_real_time_preview()
        page.assert_start_vl_record(CaseData["断言元素定位"])
        page.page.wait_for_timeout(1000)
        page.click_stop_record()

    """录像过程中刷新界面不会停止录像"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[47]])
    def test_case_47(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_start_record()
        page._browser_operation(reload=True)
        page.click_login_button()
        page.page.wait_for_timeout(1000)
        page.assert_start_vl_record(CaseData["断言元素定位"])
        page.click_stop_record()

    """录像过程中退出登录不会停止录像"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", [yaml_data[48]])
    def test_case_48(self, page, CaseData: dict):
        page = PreviewPage(page)
        page.click_start_record()
        page.click_admin()
        page.click_logout()
        page.click_confirm_exit()
        page.click_login_button()
        page.page.wait_for_timeout(1000)
        page.assert_start_vl_record(CaseData["断言元素定位"])
        page.click_stop_record()





































