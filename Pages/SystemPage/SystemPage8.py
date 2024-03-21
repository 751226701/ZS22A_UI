# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/3/20 9:13
# @File :SystemPage8
# @Project : ZS22A_UI

from PIL import Image
import io
import re
import base64
import os.path
import allure
from time import sleep
from Common.Common import Common
from Config.Config import Config
from Common.CompareImage import are_images_equal, download_image
from playwright.sync_api import expect

class SystemPage(Common):
    # 网络设置子模块元素定位
    __test = ""
    __email_type = r"^邮箱类型无 QQ 新浪 163 126 自定义$|^邮箱类型$"
    __anon_box = r"^匿名 注意：选择不支持匿名的邮箱类型，会导致邮件无法正常发送$"
    __encrypt = r"^加密方式$|^加密方式NoneTLSSSL$"
    __theme = r"^主题 支持附件（100字符以内）$"
    __protocol = r"^信令传输协议UDP TCP$|^信令传输协议$"
    __channel = r"^通道相关信息通道1 通道2$|^通道相关信息$"

    # TCP/IP
    @allure.step("设置主机名称")
    def set_hostname(self, value):
        self.page.locator("div").filter(has_text=re.compile(r"^主机名称$")).get_by_role("textbox").fill(value)

    @allure.step("静态IP")
    def select_static_ip(self):
        self. page.get_by_role("radio", name="静态").click()

    @allure.step("DHCP")
    def select_dhcp(self):
        self.page.get_by_role("radio", name="DHCP").click()

    @allure.step("IPV4地址设置")
    def set_ipv4_address(self, value):
        self.page.locator("div").filter(has_text=re.compile(r"^IPv4地址$")).get_by_role("textbox").fill(value)

    @allure.step("IPV4子网掩码设置")
    def set_ipv4_subnet_mask(self, value):
        self.page.locator("div").filter(has_text=re.compile(r"^IPv4子网掩码$")).get_by_role("textbox").fill(value)

    @allure.step("IPV4网关设置")
    def set_ipv4_gateway(self, value):
        self.page.locator("div").filter(has_text=re.compile(r"^IPv4默认网关$")).get_by_role("textbox").fill(value)

    @allure.step("IPV6启用开关")
    def ipv6_enable_switch(self):
        self.page.get_by_role("switch").locator("span").click()

    @allure.step("IPV6手动模式")
    def ipv6_manual(self):
        self.page.locator("div").filter(has_text=re.compile(r"^IPv6模式$|^IPv6模式手动 自动$")).locator("i").click()
        self.page.get_by_text("手动").click()

    @allure.step("IPV6自动模式")
    def ipv6_auto(self):
        self.page.locator("div").filter(has_text=re.compile(r"^IPv6模式$|^IPv6模式手动 自动$")).locator("i").click()
        self.page.get_by_text("自动").click()

    @allure.step("IPV6地址设置")
    def set_ipv6_address(self, value):
        self. page.locator("div").filter(has_text=re.compile(r"^IPv6地址$")).get_by_role("textbox").fill(value)

    @allure.step("IPV6子网掩码设置")
    def set_ipv6_subnet_mask(self, value):
        self.page.locator("div").filter(has_text=re.compile(r"^IPv6子网掩码 \(3~127\)$")).get_by_role("textbox").fill(value)

    @allure.step("IPV6网关设置")
    def set_ipv6_gateway(self, value):
        self.page.locator("div").filter(has_text=re.compile(r"^IPv6默认网关$")).get_by_role("textbox").fill(value)

    @allure.step("首选DNS设置")
    def set_primary_dns(self, value):
        self.page.locator("div").filter(has_text=re.compile(r"^首选DNS$")).get_by_role("textbox").fill(value)

    @allure.step("备选选DNS设置")
    def set_secondary_dns(self, value):
        self.page.locator("div").filter(has_text=re.compile(r"^备选DNS$")).get_by_role("textbox").fill(value)

    # 端口设置
    @allure.step("切换至端口设置页面")
    def switch_to_port_setting(self):
        self.page.get_by_role("tab", name="端口设置").click()

    @allure.step("设置最大连接数")
    def set_max_connection(self, value):
        self. page.locator("div").filter(has_text=re.compile(r"^最大连接数 1~20$")).get_by_role("textbox").fill(value)

    @allure.step("HTTP端口设置")
    def set_http_port(self, value):
        self.page.locator("div").filter(has_text=re.compile(r"^HTTP端口 1024~65535,80$")).get_by_role("textbox").fill(value)

    @allure.step("RTSP端口设置")
    def set_rtsp_port(self, value):
        self.page.locator("div").filter(has_text=re.compile(r"^RTSP端口 加密 1024~65535,554$")).get_by_role("textbox").fill(value)

    # SMTP设置
    @allure.step("切换至SMTP设置页面")
    def switch_to_smtp_setting(self):
        self.page.get_by_role("tab", name="SMTP设置").click()

    @allure.step("邮箱类型选择")
    def select_email_type(self):
        self.page.locator("div").filter(has_text=re.compile(self.__email_type)).get_by_placeholder("请选择").click()

    @allure.step("无")
    def select_email_type_no(self):
        self.page.get_by_role("list").get_by_text("无").click()

    @allure.step("QQ")
    def select_email_type_qq(self):
        self.page.get_by_text("QQ", exact=True).click()

    @allure.step("新浪")
    def select_email_type_sina(self):
        self.page.get_by_text("新浪").click()

    @allure.step("163")
    def select_email_type_163(self):
        self.page.get_by_text("163", exact=True).click()

    @allure.step("126")
    def select_email_type_126(self):
        self.page.get_by_text("126", exact=True).click()

    @allure.step("自定义")
    def select_email_type_custom(self):
        self.page.get_by_text("自定义").click()

    @allure.step("SMTP服务器设置")
    def set_smtp_server(self, value):
        self.page.locator("div").filter(has_text=re.compile(r"^SMTP服务器$")).get_by_role("textbox").fill(value)

    @allure.step("端口设置")
    def set_smtp_port(self, value):
        self.page.locator("div").filter(has_text=re.compile(r"^端口$")).get_by_role("textbox").fill(value)

    @allure.step("用户名设置")
    def set_smtp_username(self, value):
        self.page.locator("div").filter(has_text=re.compile(r"^用户名$")).get_by_role("textbox").fill(value)

    @allure.step("密码设置")
    def set_smtp_password(self, value):
        self.page.locator("input[type=\"password\"]").fill(value)

    @allure.step("发件人设置")
    def set_smtp_sender(self, value):
        self.page.locator("div").filter(has_text=re.compile(r"^发件人$")).get_by_role("textbox").fill(value)

    @allure.step("匿名复选框")
    def anonymous_checkbox(self):
        self.page.locator("div").filter(has_text=re.compile(self.__anon_box)).locator("span").nth(1).click()

    @allure.step("加密方式选择")
    def select_encryption_type(self):
        self.page.locator("div").filter(has_text=re.compile(self.__encrypt)).get_by_placeholder("请选择").click()

    @allure.step("None")
    def select_encryption_type_none(self):
        self.page.get_by_text("None").click()

    @allure.step("TLS")
    def select_encryption_type_tls(self):
        self.page.get_by_text("TLS").click()

    @allure.step("SSL")
    def select_encryption_type_ssl(self):
        self.page.get_by_text("SSL").click()

    @allure.step("设置主题")
    def set_theme(self, value):
        self.page.locator("div").filter(has_text=re.compile(self.__theme)).get_by_role("textbox").fill(value)

    @allure.step("设置收件人")
    def set_receiver(self, num, value):
        """
        :param num: 收件人序号
        :param value: 收件人地址
        :return: 无
        """
        receiver = f"收件人{num}"
        self.page.locator("div").filter(has_text=re.compile(f"^{receiver}$")).get_by_role("textbox").fill(value)

    @allure.step("点击报警邮件复选框")
    def click_alarm_email_checkbox(self):
        self.page.get_by_text("报警邮件").click()

    @allure.step("点击健康测试邮件复选框")
    def click_health_email_checkbox(self):
        self.page.get_by_text("健康测试邮件").click()

    # ONVIF设置
    @allure.step("切换至ONVIF设置页面")
    def switch_to_onvif_setting(self):
        self.page.get_by_role("tab", name="ONVIF").click()

    @allure.step("ONVIF校验开关")
    def onvif_check_switch(self):
        self.page.get_by_role("switch").locator("span").click()

    @allure.step("ONVIF端口设置")
    def set_onvif_port(self, value):
        self.page.get_by_role("textbox").fill(value)

    # MQTT设置
    @allure.step("切换至MQTT设置页面")
    def switch_to_mqtt_setting(self):
        self.page.get_by_role("tab", name="MQTT").click()

    @allure.step("启用开关")
    def mqtt_enable_switch(self):
        self.page.get_by_role("switch").locator("span").click()

    @allure.step("设置主机名称")
    def set_mqtt_host_name(self, value):
        self.page.locator("div").filter(has_text=re.compile(r"^主机名称$")).get_by_role("textbox").fill(value)

    @allure.step("设置服务器地址")
    def set_mqtt_server_address(self, value):
        self.page.locator("div").filter(has_text=re.compile(r"^服务器地址$")).get_by_role("textbox").fill(value)

    @allure.step("设置服务器端口")
    def set_mqtt_server_port(self, value):
        self.page.locator("div").filter(has_text=re.compile(r"^服务器端口 1025~65535$")).get_by_role("textbox").fill(value)

    @allure.step("设置用户名")
    def set_mqtt_username(self, value):
        self.page.locator("div").filter(has_text=re.compile(r"^用户名$")).get_by_role("textbox").fill(value)

    @allure.step("设置密码")
    def set_mqtt_password(self, value):
        self.page.locator("input[type=\"password\"]").fill(value)

    # 28181
    @allure.step("切换至28181设置页面")
    def switch_to_28181_setting(self):
        self.page.get_by_role("tab", name="28181").click()

    @allure.step("启用开关")
    def gb_enable_switch(self):
        self.page.get_by_role("switch").locator("span").click()

    @allure.step("设置SIP服务器编号")
    def set_sip_server_number(self, value):
        self.page.locator("div").filter(has_text=re.compile(r"^SIP服务器编号$")).get_by_role("textbox").fill(value)

    @allure.step("设置SIP服务器IP")
    def set_sip_server_ip(self, value):
        self.page.locator("div").filter(has_text=re.compile(r"^SIP服务器IP$")).get_by_role("textbox").fill(value)

    @allure.step("设置设备编号")
    def set_device_number(self, value):
        self.page.locator("div").filter(has_text=re.compile(r"^设备编号$")).get_by_role("textbox").fill(value)

    @allure.step("设置本地SIP服务器端口")
    def set_local_sip_server_port(self, value):
        self.page.locator("div").filter(has_text=re.compile(r"^本地SIP服务器端口$")).get_by_role("textbox").fill(value)

    @allure.step("设置心跳周期")
    def set_heartbeat_period(self, value):
        self.page.locator("div").filter(has_text=re.compile(r"^心跳周期$")).get_by_role("textbox").fill(value)

    @allure.step("UDP")
    def select_protocol_udp(self):
        self.page.locator("div").filter(has_text=re.compile(self.__protocol)).get_by_role("textbox").click()
        self.page.get_by_text("UDP").click()

    @allure.step("TCP")
    def select_protocol_tcp(self):
        self.page.locator("div").filter(has_text=re.compile(self.__protocol)).get_by_role("textbox").click()
        self.page.get_by_text("TCP", exact=True).click()

    @allure.step("通道1")
    def select_channel_1(self):
        self.page.locator("div").filter(has_text=re.compile(self.__channel)).get_by_placeholder("请选择").click()
        self.page.get_by_text("通道1").click()

    @allure.step("通道2")
    def select_channel_2(self):
        self.page.locator("div").filter(has_text=re.compile(self.__channel)).get_by_placeholder("请选择").click()
        self.page.get_by_text("通道2").click()

    @allure.step("设置SIP域")
    def set_sip_domain(self, value):
        self.page.locator("div").filter(has_text=re.compile(r"^SIP域$")).get_by_role("textbox").fill(value)

    @allure.step("设置SIP服务器端口")
    def set_sip_server_port(self, value):
        self.page.locator("div").filter(has_text=re.compile(r"^SIP服务器端口$")).get_by_role("textbox").fill(value)

    @allure.step("设置注册密码")
    def set_register_password(self, value):
        self.page.locator("input[type=\"password\"]").fill(value)

    @allure.step("设置注册有效期")
    def set_register_validity(self, value):
        self.page.locator("div").filter(has_text=re.compile(r"^注册有效期$")).get_by_role("textbox").fill(value)

    @allure.step("设置最大心跳超时次数")
    def set_max_heartbeat_timeout_times(self, value):
        self. page.locator("div").filter(has_text=re.compile(r"^最大心跳超时次数$")).get_by_role("textbox").fill(value)

    # 平台接入
    @allure.step("切换至平台接入页面")
    def switch_to_platform_access(self):
        self.page.get_by_role("tab", name="平台接入").click()

    @allure.step("启用开关")
    def platform_access_enable_switch(self):
        self.page.get_by_role("switch").locator("span").click()

    @allure.step("高德质感")
    def guide_protocol(self):
        self.page.get_by_placeholder("请选择").click()
        self.page.get_by_text("高德智感").click()

    @allure.step("其他协议")
    def other_protocol(self):
        self.page.get_by_placeholder("请选择").click()
        self.page.get_by_text("其他协议").click()

    @allure.step("设置服务器地址")
    def set_server_address(self, value):
        self.page.locator("div").filter(has_text=re.compile(r"^服务器地址$")).get_by_role("textbox").fill(value)

    @allure.step("设置端口")
    def set_port(self, value):
        self.page.locator("div").filter(has_text=re.compile(r"^端口$")).get_by_role("textbox").fill(value)

    @allure.step("设置用户名")
    def set_username(self, value):
        self.page.locator("div").filter(has_text=re.compile(r"^用户名$")).get_by_role("textbox").fill(value)

    @allure.step("设置密码")
    def set_password(self, value):
        self.page.locator("input[type=\"password\"]").fill(value)

    # NTP设置
    @allure.step("切换至NTP设置页面")
    def switch_to_ntp_setting(self):
        self.page.get_by_role("tab", name="NTP设置").click()

    @allure.step("启用")
    def ntp_enable_switch(self):
        self.page.get_by_role("switch").locator("span").click()

    @allure.step("设置服务器地址")
    def set_ntp_server_address(self, value):
        self.page.get_by_role("textbox").fill(value)

    # 白名单设置
    @allure.step("切换至白名单设置页面")
    def switch_to_whitelist_setting(self):
        self.page.get_by_role("tab", name="白名单").click()

    @allure.step("启用开关")
    def whitelist_enable_switch(self):
        self.page.get_by_role("switch").locator("span").click()

    @allure.step("添加IP")
    def add_ip(self, value):
        """调用后直接添加IP"""
        self.page.get_by_role("button", name="添加 IP/MAC").click()
        self.page.get_by_label("添加").locator("form").get_by_role("textbox").fill(value)
        self.click_confirm()

    @allure.step("添加IP网段")
    def add_ip_segment(self, ip1, ip2):
        """调用后直接添加IP网段"""
        self.page.get_by_role("button", name="添加 IP/MAC").click()
        self.page.get_by_placeholder("请选择").click()
        self.page.get_by_text("IP网段").click()
        self.page.get_by_role("textbox").nth(1).fill(ip1)
        self.page.get_by_role("textbox").nth(2).fill(ip2)
        self.click_confirm()

    @allure.step("添加MAC")
    def add_mac(self, value):
        """调用后直接添加MAC"""
        self.page.get_by_role("button", name="添加 IP/MAC").click()
        self.page.get_by_placeholder("请选择").click()
        self.page.get_by_text("MAC地址").click()
        self.page.get_by_label("添加").locator("form").get_by_role("textbox").fill(value)
        self.click_confirm()

    @allure.step("确定")
    def click_confirm(self):
        self.page.get_by_label("添加").get_by_role("button", name="确定").click()

    @allure.step("取消")
    def click_cancel(self):
        self. page.get_by_role("button", name="取消").click()

    @allure.step("序号全选框")
    def select_all(self):
        self.page.get_by_role("row", name="序号 IP/MAC 操作").locator("span").nth(1).click()

    @allure.step("点击清空")
    def click_clear(self):
        self.page.get_by_role("button", name="清空").click()

    @allure.step("点击默认")
    def click_default(self):
        self.page.get_by_role("button", name="默认").click()

    @allure.step("点击刷新")
    def click_refresh(self):
        self.page.get_by_role("button", name="刷新").click()

    @allure.step("点击确定")
    def click_ok(self):
        self.page.get_by_role("button", name="确定").click()





























