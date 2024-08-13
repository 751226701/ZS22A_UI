#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: 刘涛
# @time: 2024/1/15 10:08
# @file: runner.py
# @project: ZS22A_UI

import os
import pytest
from Config.Config import Config
from Common.SendEmail import SendEmail

if __name__ == '__main__':
    AllureReport = Config.test_report_dir
    AllureResult = Config.test_result_dir
    Screenshot = Config.test_screenshot_dir
    Download = Config.test_download_dir
    os.system(f"del {os.path.join(Screenshot, '*.png')}")
    os.system(f"del {os.path.join(Download, '*.jpg')}")
    os.system(f"del {os.path.join(Download, '*.mp4')}")
    pytest.main(["-v", "-s", f'--alluredir={AllureResult}', "--clean-alluredir"])  # 执行用例生成测试结果
    os.system(f'allure generate {AllureResult} -o {AllureReport} --clean')  # 生成测试报告
    SendEmail(sign=False)  # 发送测试报告邮件

