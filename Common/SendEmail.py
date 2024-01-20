#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: 刘涛
@time: 2024/1/15 20:17 
@file: SendEmail.py
@project: ZS22A_UI
"""
import os
import shutil
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from Config.Config import Config


def send_email_allure_report(subject, body, sender_email, receiver_emails, smtp_server, smtp_port, smtp_username,
                             smtp_password, allure_report_path):
    """
    生成 Allure 报告，并发送邮件
    :param subject: 邮件主题
    :param body: 邮件正文内容
    :param sender_email: 发件人邮箱地址
    :param receiver_emails: 接收人邮箱地址列表
    :param smtp_server: SMTP 服务器地址
    :param smtp_port: SMTP 服务器端口
    :param smtp_username: SMTP 服务器用户名
    :param smtp_password: SMTP 服务器密码
    :param allure_report_path: Allure 报告文件夹路径
    :return: 无
    """

    # 构建邮件
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ', '.join(receiver_emails)
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # 写入测试报告启动脚本
    bat_file_path = os.path.join(allure_report_path, '双击我打开测试报告.bat')
    if not os.path.exists(bat_file_path):
        with open(bat_file_path, 'w') as bat_file:
            bat_file.write('@echo off\n'
                           'if "%1" == "h" goto begin\n'
                           'mshta vbscript:createobject("wscript.shell").run("%~nx0 h",0)(window.close)&&exit\n'
                           ':begin\n'
                           'cd /d %~dp0\n'
                           'allure open .')

    # 压缩 Allure 报告目录
    zip_base_name = os.path.join(allure_report_path, 'allure-report')
    shutil.make_archive(zip_base_name, 'zip', allure_report_path)

    # 将压缩的 Allure 报告.zip 文件添加到邮件
    with open(f"{zip_base_name}.zip", "rb") as attachment:
        part = MIMEApplication(attachment.read(), Name="allure-report.zip")
        part['Content-Disposition'] = 'attachment; filename="allure-report.zip"'
        msg.attach(part)

    # 发送邮件
    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        # server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, receiver_emails, msg.as_string())


def SendEmail(sign):
    try:
        if sign:
            send_email_allure_report(
                subject=Config.subject,
                body=Config.body,
                sender_email=Config.sender_email,
                receiver_emails=Config.receiver_emails,
                smtp_server=Config.smtp_server,
                smtp_port=Config.smtp_port,
                smtp_username=Config.smtp_username,
                smtp_password=Config.smtp_password,
                allure_report_path=Config.test_report_dir)
            print("Email sent successfully")
        else:
            pass
    except Exception as e:
        print(f"Error sending email: {e}")
