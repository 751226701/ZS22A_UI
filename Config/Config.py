#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: 刘涛
# @time: 2024/1/15 10:05
# @file: Config.py
# @project: ZS22A_UI

import os
class Config:
    # 项目地址
    url = "http://192.168.21.171/#/login"

    # 项目根目录
    root_dir = os.path.split(os.path.split(__file__)[0])[0]
    test_cases_dir = root_dir + os.path.sep + "TestCases"
    test_datas_dir = root_dir + os.path.sep + "TestDatas"
    test_files_dir = root_dir + os.path.sep + "TestFiles"
    test_report_dir = root_dir + os.path.sep + "TestReport" + os.path.sep + "AllureReport"
    test_result_dir = root_dir + os.path.sep + "TestReport" + os.path.sep + "AllureResult"
    test_screenshot_dir = root_dir + os.path.sep + "TestReport" + os.path.sep + "Screenshot"
    test_download_dir = root_dir + os.path.sep + "TestReport" + os.path.sep + "Download\\"
    logs = root_dir + os.path.sep + "Logs"

    # 使用的浏览器
    browser = "chrome"

    # 邮件发送参数配置
    subject = "ZS22A Allure 测试报告"                # 邮件主题，可编辑
    body = "请查收测试报告,系统自动发送，无需回复"        # 邮件内容，可编辑
    sender_email = "liutao@guideir.com"             # 替换为自己的邮箱
    receiver_emails = ["751226701@qq.com"]          # 替换为需要接受测试报告的邮箱
    smtp_server = "112.53.42.125"                   # 不变
    smtp_port = 465                                 # 不变
    smtp_username = "liutao@guideir.com"            # 替换为自己的邮箱
    smtp_password = "dD8Eut5Hwv7BwWP7"              # 替换为自己的邮箱授权码
    allure_report_path = test_report_dir

    # 是否记录trace, trace1对应第一个测试文件，以此类推
    # 开启trace后会以截图的形式记录执行的每一个步骤，但会占用系统资源
    # 浏览器打开网站trace.playwright.dev   将trace.zip文件拖入浏览器即可查看
    trace1 = False   # 登录模块
    trace2 = False   # 实时预览
    trace3 = False   # 回放管理
    trace4 = False   # 统计报表
    trace5 = False   # 全局温度
    trace6 = False   # 分析对象


if __name__ == '__main__':
    print(Config.root_dir)
    print(Config.test_cases_dir)
    print(Config.test_download_dir)

