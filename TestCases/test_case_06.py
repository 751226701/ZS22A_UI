# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/3/6 10:02
# @File :test_case_06.py
# @Project : ZS22A_UI

import os
import re
import allure
import pytest
from playwright.sync_api import sync_playwright
from Pages.AlarmPage.AlarmPage2 import AlarmPage
from Common.ReadYaml import ReadYaml
from Common.AllurePretty import PrettyAllure
from Config.Config import Config

yaml_data = ReadYaml(os.path.join(Config.test_datas_dir, "test_data_06.yaml"))
logindata = yaml_data.read()[0]
Trace = Config.trace6
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
    pageobject.get_by_text("报警管理").click()
    pageobject.get_by_text("温度监测").click()
    pageobject.get_by_role("menuitem", name="分析对象").click()
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
            context.tracing.stop(path="trace6.zip")
        else:
            pass
        context.close()
        browser.close()

"""执行分析对象子模块测试"""
class TestAlarm:

    """添加一个点分析对象"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_01"]))
    def test_case_01(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.draw_object_on()
        page.click_default()
        page.click_ok()
        page.select_point_brush()
        page.draw_object(134, 93)
        page.click_ok()
        page.assert_draw_object(CaseData['断言元素定位'])

    """添加一个线分析对象"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_02"]))
    def test_case_02(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.draw_object_on()
        page.click_default()
        page.click_ok()
        page.select_line_brush()
        page.draw_object(50, 50)
        page.draw_object(300, 300)
        page.click_ok()
        page.assert_draw_object(CaseData['断言元素定位'])

    """添加一个圆分析对象"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_03"]))
    def test_case_03(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.draw_object_on()
        page.click_default()
        page.click_ok()
        page.select_circle_brush()
        page.draw_object(134, 93)
        page.draw_object(200, 300)
        page.click_ok()
        page.assert_draw_object(CaseData['断言元素定位'])

    """添加一个矩形分析对象"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_04"]))
    def test_case_04(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.draw_object_on()
        page.click_default()
        page.click_ok()
        page.select_rectangle_brush()
        page.draw_object(100, 100)
        page.draw_object(300, 300)
        page.click_ok()
        page.assert_draw_object(CaseData['断言元素定位'])

    """添加一个多边形分析对象"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_05"]))
    def test_case_05(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.draw_object_on()
        page.click_default()
        page.click_ok()
        page.select_polygon_brush()
        page.draw_object(100, 100)
        page.draw_object(150, 150)
        page.draw_object(200, 100)
        page.draw_object(250, 150)
        page.draw_object(300, 100)
        page.draw_object(200, 300)
        page.draw_object(300, 100)
        page.click_ok()
        page.assert_draw_object(CaseData['断言元素定位'])

    """不勾选分析对象点击删除"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_06"]))
    def test_case_06(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.page.wait_for_timeout(2000)
        page.delete()
        page.assert_prompt_is_visible(CaseData['断言元素定位'])

    """全选分析对象后点击删除-取消"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_07"]))
    def test_case_07(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.object_list_all()
        page.delete()
        page.delete_cancel()
        page.click_ok()
        page.assert_draw_object(CaseData['断言元素定位'])

    """全选分析对象后点击删除-确定"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_08"]))
    def test_case_08(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.delete()
        page.delete_confirm()
        page.click_ok()
        page.assert_object_nonexistent(CaseData['断言元素定位'])

    """设置分析对象名称"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_09"]))
    def test_case_09(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.draw_object_on()
        page.click_default()
        page.click_ok()
        page.select_rectangle_brush()
        page.draw_object(100, 100)
        page.draw_object(300, 300)
        page.click_ok()
        page.set_obj_name("矩形分析对象QWer@#__")
        page.click_ok()
        page.assert_obj_name(CaseData['断言元素定位'])

    """温度显示内容默认最高温"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_10"]))
    def test_case_10(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.assert_temp_show(CaseData['断言元素定位'])

    """设置显示最低温"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_11"]))
    def test_case_11(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.select_show()
        page.select_show_min_temp()
        page.click_ok()
        page.click_refresh()
        page.assert_temp_show(CaseData['断言元素定位'])

    """设置显示平均温"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_12"]))
    def test_case_12(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.select_show()
        page.select_show_avg_temp()
        page.click_ok()
        page.click_refresh()
        page.assert_temp_show(CaseData['断言元素定位'])

    """设置显示仅名称"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_13"]))
    def test_case_13(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.select_show()
        page.select_show_name()
        page.click_ok()
        page.click_refresh()
        page.assert_temp_show(CaseData['断言元素定位'])

    """设置显示名称+最高温"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_14"]))
    def test_case_14(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.select_show()
        page.select_show_name_max_temp()
        page.click_ok()
        page.click_refresh()
        page.assert_temp_show(CaseData['断言元素定位'])

    """设置显示名称+最低温"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_15"]))
    def test_case_15(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.select_show()
        page.select_show_name_min_temp()
        page.click_ok()
        page.click_refresh()
        page.assert_temp_show(CaseData['断言元素定位'])

    """设置显示名称+平均温"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_16"]))
    def test_case_16(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.select_show()
        page.select_show_name_avg_temp()
        page.click_ok()
        page.click_refresh()
        page.assert_temp_show(CaseData['断言元素定位'])

    """设置显示为不显示"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_17"]))
    def test_case_17(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.select_show()
        page.select_show_none()
        page.click_ok()
        page.click_refresh()
        page.assert_temp_show(CaseData['断言元素定位'])

    """设置显示为最高温"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_18"]))
    def test_case_18(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.select_show()
        page.select_show_max_temp()
        page.click_ok()
        page.click_refresh()
        page.assert_temp_show(CaseData['断言元素定位'])

    """显示方位默认为上方"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_19"]))
    def test_case_19(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.assert_show_position(CaseData['断言元素定位'])

    """设置显示方位为下方"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_20"]))
    def test_case_20(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.select_show_position()
        page.select_down()
        page.click_ok()
        page.click_refresh()
        page.assert_show_position(CaseData['断言元素定位'])

    """设置显示方位为左方"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_21"]))
    def test_case_21(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.select_show_position()
        page.select_left()
        page.click_ok()
        page.click_refresh()
        page.assert_show_position(CaseData['断言元素定位'])

    """设置显示方位为右方"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_22"]))
    def test_case_22(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.select_show_position()
        page.select_right()
        page.click_ok()
        page.click_refresh()
        page.assert_show_position(CaseData['断言元素定位'])

    """设置显示方位为中间"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_23"]))
    def test_case_23(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.select_show_position()
        page.select_mid()
        page.click_ok()
        page.click_refresh()
        page.assert_show_position(CaseData['断言元素定位'])

    """设置显示方位为上方"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_24"]))
    def test_case_24(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.select_show_position()
        page.select_up()
        page.click_ok()
        page.click_refresh()
        page.assert_show_position(CaseData['断言元素定位'])

    """发射率默认值"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_25"]))
    def test_case_25(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.assert_emiss_value(CaseData['断言元素定位'])

    """发射率设置0.01"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_26"]))
    def test_case_26(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.set_emiss("0.01")
        page.click_ok()
        page.click_refresh()
        page.assert_emiss_value(CaseData['断言元素定位'])

    """发射率设置0.5"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_27"]))
    def test_case_27(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.set_emiss("0.5")
        page.click_ok()
        page.click_refresh()
        page.assert_emiss_value(CaseData['断言元素定位'])

    """发射率设置1"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_28"]))
    def test_case_28(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.set_emiss("1")
        page.click_ok()
        page.click_refresh()
        page.assert_emiss_value(CaseData['断言元素定位'])

    """发射率设置0"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_29"]))
    def test_case_29(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.set_emiss("0")
        page.click_ok()
        page.click_refresh()
        page.assert_emiss_value(CaseData['断言元素定位'])

    """发射率设置1.1"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_30"]))
    def test_case_30(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.set_emiss("1.1")
        page.click_ok()
        page.click_refresh()
        page.assert_emiss_value(CaseData['断言元素定位'])

    """发射率选择不锈钢"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_31"]))
    def test_case_31(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.select_emiss("不锈钢")
        page.click_ok()
        page.click_refresh()
        page.assert_emiss_value(CaseData['断言元素定位'])

    """发射率选择铝板"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_32"]))
    def test_case_32(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.select_emiss("铝板")
        page.click_ok()
        page.click_refresh()
        page.assert_emiss_value(CaseData['断言元素定位'])

    """发射率选择黑铝"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_33"]))
    def test_case_33(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.select_emiss("黑铝")
        page.click_ok()
        page.click_refresh()
        page.assert_emiss_value(CaseData['断言元素定位'])

    """发射率选择沥青"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_34"]))
    def test_case_34(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.select_emiss("沥青")
        page.click_ok()
        page.click_refresh()
        page.assert_emiss_value(CaseData['断言元素定位'])

    """发射率选择黑纸"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_35"]))
    def test_case_35(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.select_emiss("黑纸")
        page.click_ok()
        page.click_refresh()
        page.assert_emiss_value(CaseData['断言元素定位'])

    """发射率选择混凝土"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_36"]))
    def test_case_36(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.select_emiss("混凝土")
        page.click_ok()
        page.click_refresh()
        page.assert_emiss_value(CaseData['断言元素定位'])

    """发射率选择铸铁"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_37"]))
    def test_case_37(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.select_emiss("铸铁")
        page.click_ok()
        page.click_refresh()
        page.assert_emiss_value(CaseData['断言元素定位'])

    """发射率选择石膏"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_38"]))
    def test_case_38(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.select_emiss("石膏")
        page.click_ok()
        page.click_refresh()
        page.assert_emiss_value(CaseData['断言元素定位'])

    """发射率选择橡胶"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_39"]))
    def test_case_39(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.select_emiss("橡胶")
        page.click_ok()
        page.click_refresh()
        page.assert_emiss_value(CaseData['断言元素定位'])

    """发射率选择木"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_40"]))
    def test_case_40(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.select_emiss("木")
        page.click_ok()
        page.click_refresh()
        page.assert_emiss_value(CaseData['断言元素定位'])

    """发射率选择砖"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_41"]))
    def test_case_41(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.select_emiss("砖")
        page.click_ok()
        page.click_refresh()
        page.assert_emiss_value(CaseData['断言元素定位'])

    """发射率选择胶带"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_42"]))
    def test_case_42(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.select_emiss("胶带")
        page.click_ok()
        page.click_refresh()
        page.assert_emiss_value(CaseData['断言元素定位'])

    """发射率选择铜板"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_43"]))
    def test_case_43(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.select_emiss("铜板")
        page.click_ok()
        page.click_refresh()
        page.assert_emiss_value(CaseData['断言元素定位'])

    """发射率选择人体皮肤"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_44"]))
    def test_case_44(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.select_emiss("人体皮肤")
        page.click_ok()
        page.click_refresh()
        page.assert_emiss_value(CaseData['断言元素定位'])

    """发射率选择PVC塑料"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_45"]))
    def test_case_45(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.select_emiss("PVC塑料")
        page.click_ok()
        page.click_refresh()
        page.assert_emiss_value(CaseData['断言元素定位'])

    """发射率选择聚碳酸"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_46"]))
    def test_case_46(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.select_emiss("聚碳酸")
        page.click_ok()
        page.click_refresh()
        page.assert_emiss_value(CaseData['断言元素定位'])

    """发射率选择氧化铜"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_47"]))
    def test_case_47(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.select_emiss("氧化铜")
        page.click_ok()
        page.click_refresh()
        page.assert_emiss_value(CaseData['断言元素定位'])

    """发射率选择锈"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_48"]))
    def test_case_48(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.select_emiss("锈")
        page.click_ok()
        page.click_refresh()
        page.assert_emiss_value(CaseData['断言元素定位'])

    """发射率选油漆"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_49"]))
    def test_case_49(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.select_emiss("油漆")
        page.click_ok()
        page.click_refresh()
        page.assert_emiss_value(CaseData['断言元素定位'])

    """发射率选土壤"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_50"]))
    def test_case_50(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.select_emiss("土壤")
        page.click_ok()
        page.click_refresh()
        page.assert_emiss_value(CaseData['断言元素定位'])

    """发射率选自定义"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_51"]))
    def test_case_51(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.select_emiss("自定义")
        page.click_ok()
        page.click_refresh()
        page.assert_emiss_value(CaseData['断言元素定位'])

    """距离默认值0.5"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_52"]))
    def test_case_52(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.assert_distance_value(CaseData['断言元素定位'])

    """距离设置0.1"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_53"]))
    def test_case_53(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.set_distance("0.1")
        page.click_ok()
        page.click_refresh()
        page.assert_distance_value(CaseData['断言元素定位'])

    """距离设置20"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_54"]))
    def test_case_54(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.set_distance("20")
        page.click_ok()
        page.click_refresh()
        page.assert_distance_value(CaseData['断言元素定位'])

    """距离设置200"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_55"]))
    def test_case_55(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.set_distance("200")
        page.click_ok()
        page.click_refresh()
        page.assert_distance_value(CaseData['断言元素定位'])

    """距离设置0"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_56"]))
    def test_case_56(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.set_distance("0")
        page.click_ok()
        page.click_refresh()
        page.assert_distance_value(CaseData['断言元素定位'])

    """距离设置201"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_57"]))
    def test_case_57(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.set_distance("201")
        page.click_ok()
        page.click_refresh()
        page.assert_distance_value(CaseData['断言元素定位'])

    """反射温度默认值"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_58"]))
    def test_case_58(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.assert_reflect_temp_value(CaseData['断言元素定位'])

    """反射温度设置-40"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_59"]))
    def test_case_59(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.set_reflect_temp("-40")
        page.click_ok()
        page.click_refresh()
        page.assert_reflect_temp_value(CaseData['断言元素定位'])

    """反射温度设置200"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_60"]))
    def test_case_60(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.set_reflect_temp("200")
        page.click_ok()
        page.click_refresh()
        page.assert_reflect_temp_value(CaseData['断言元素定位'])

    """反射温度设置2000"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_61"]))
    def test_case_61(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.set_reflect_temp("2000")
        page.click_ok()
        page.click_refresh()
        page.assert_reflect_temp_value(CaseData['断言元素定位'])

    """反射温度设置-41"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_62"]))
    def test_case_62(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.set_reflect_temp("-41")
        page.click_ok()
        page.click_refresh()
        page.assert_reflect_temp_value(CaseData['断言元素定位'])

    """反射温度设置2001"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_63"]))
    def test_case_63(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.set_reflect_temp("2001")
        page.click_ok()
        page.click_refresh()
        page.assert_reflect_temp_value(CaseData['断言元素定位'])

    """启用配置默认状态"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_64"]))
    def test_case_64(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.assert_alarm_switch_status(CaseData['断言元素定位'])

    """启用配置设置为开"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_65"]))
    def test_case_65(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.alarm_switch()
        page.click_ok()
        page.click_refresh()
        page.assert_alarm_switch_status(CaseData['断言元素定位'])

    """启用配置设置为关"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_66"]))
    def test_case_66(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.alarm_switch()
        page.click_ok()
        page.click_refresh()
        page.assert_alarm_switch_status(CaseData['断言元素定位'])

    """默认最高温报警"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_67"]))
    def test_case_67(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.assert_alarm_type(CaseData['断言元素定位'])

    """设置报警类型为最低温"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_68"]))
    def test_case_68(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.alarm_type_select()
        page.min_temp_alarm()
        page.click_ok()
        page.click_refresh()
        page.assert_alarm_type(CaseData['断言元素定位'])

    """设置报警类型为平均温"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_69"]))
    def test_case_69(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.alarm_type_select()
        page.avg_temp_alarm()
        page.click_ok()
        page.click_refresh()
        page.assert_alarm_type(CaseData['断言元素定位'])

    """设置报警类型为温升"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_70"]))
    def test_case_70(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.alarm_type_select()
        page.temp_rise_alarm()
        page.click_ok()
        page.click_refresh()
        page.assert_alarm_type(CaseData['断言元素定位'])

    """设置报警类型为温差"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_71"]))
    def test_case_71(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.alarm_type_select()
        page.temp_diff_alarm()
        page.click_ok()
        page.click_refresh()
        page.assert_alarm_type(CaseData['断言元素定位'])

    """设置报警类型为最高温"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_72"]))
    def test_case_72(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.alarm_type_select()
        page.max_temp_alarm()
        page.click_ok()
        page.click_refresh()
        page.assert_alarm_type(CaseData['断言元素定位'])

    """报警条件默认值"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_73"]))
    def test_case_73(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.assert_alarm_condition(CaseData['断言元素定位'])

    """设置报警条件为小于"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_74"]))
    def test_case_74(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.select_alarm_condition()
        page.select_less()
        page.click_ok()
        page.click_refresh()
        page.assert_alarm_condition(CaseData['断言元素定位'])

    """设置报警条件为大于"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_75"]))
    def test_case_75(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.select_alarm_condition()
        page.select_great()
        page.click_ok()
        page.click_refresh()
        page.assert_alarm_condition(CaseData['断言元素定位'])

    """报警阈值默认值"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_76"]))
    def test_case_76(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.assert_alarm_threshold(CaseData['断言元素定位'])

    """报警阈值设置-40"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_77"]))
    def test_case_77(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.set_temp_threshold("-40")
        page.click_ok()
        page.click_refresh()
        page.assert_alarm_threshold(CaseData['断言元素定位'])

    """报警阈值设置200"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_78"]))
    def test_case_78(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.set_temp_threshold("200")
        page.click_ok()
        page.click_refresh()
        page.assert_alarm_threshold(CaseData['断言元素定位'])

    """报警阈值设置2000"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_79"]))
    def test_case_79(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.set_temp_threshold("2000")
        page.click_ok()
        page.click_refresh()
        page.assert_alarm_threshold(CaseData['断言元素定位'])

    """报警阈值设置-41"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_80"]))
    def test_case_80(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.set_temp_threshold("-41")
        page.click_ok()
        page.click_refresh()
        page.assert_alarm_threshold(CaseData['断言元素定位'])

    """报警阈值设置2001"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_81"]))
    def test_case_81(self, page, CaseData: dict):
        page = AlarmPage(page)
        page.set_temp_threshold("2001")
        page.click_ok()
        page.click_refresh()
        page.assert_alarm_threshold(CaseData['断言元素定位'])













































































