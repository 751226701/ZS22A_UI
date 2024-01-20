# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/1/20 14:55
# @File :log.py
# @Software : PyCharm


import os
import logging
import inspect
import colorlog
from Config.Config import Config

LOG_PATH = Config.logs    # 日志路径
PREFIX_NAME = ""          # 日志前缀名
LOG_INFO = "info.log"     # 日志名称
LOG_ERROR = "error.log"   # 日志名称


class Logger:
    def __init__(self):
        if os.path.exists(LOG_PATH):
            pass
        else:
            os.mkdir(LOG_PATH)
        self.info_logger = logging.getLogger("info")  # 创建info级别日志记录器
        self.error_logger = logging.getLogger("error")  # 创建error级别日志记录器
        self.format = logging.Formatter('[%(asctime)s][%(levelname)-8s] - %(message)s')  # 格式化输出
        # 指定文件位置文件名以及输出格式
        info_file_handler = logging.FileHandler("%s/%s%s" % (LOG_PATH, PREFIX_NAME, LOG_INFO))
        info_file_handler.setFormatter(self.format)
        error_file_handler = logging.FileHandler("%s/%s%s" % (LOG_PATH, PREFIX_NAME, LOG_ERROR))
        error_file_handler.setFormatter(self.format)
        # 创建控制台处理器,将日志同步输出到控制台
        console_handler = logging.StreamHandler()
        console_formatter = colorlog.ColoredFormatter(
            '%(log_color)s[%(asctime)s][%(levelname)-8s] - %(message)s',
            log_colors={
                'DEBUG': 'cyan',
                'INFO': 'green',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'bold_red',
            }
        )
        console_handler.setFormatter(console_formatter)
        # 将处理器添加到日志记录器中
        self.info_logger.addHandler(info_file_handler)
        self.error_logger.addHandler(error_file_handler)
        self.info_logger.addHandler(console_handler)  # 添加控制台处理器
        self.error_logger.addHandler(console_handler)  # 添加控制台处理器
        # 指定日志的最低输出级别
        self.info_logger.setLevel(logging.DEBUG)
        self.error_logger.setLevel(logging.ERROR)

    def debug(self, msg, *args, **kwargs):
        """
        记录调试级别的日志消息
        :param msg:要记录的消息
        :param args:传递给日志函数的额外位置参数
        :param kwargs:传递给日志函数的额外关键字参数
        :return:
        """
        caller_frame = inspect.currentframe().f_back
        caller_filename = os.path.basename(caller_frame.f_code.co_filename)
        caller_lineno = caller_frame.f_lineno
        message = f"{caller_filename}:{caller_lineno} - {msg}"
        self.info_logger.debug(message, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        caller_frame = inspect.currentframe().f_back
        caller_filename = os.path.basename(caller_frame.f_code.co_filename)
        caller_lineno = caller_frame.f_lineno
        message = f"{caller_filename}:{caller_lineno} - {msg}"
        self.info_logger.info(message, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        caller_frame = inspect.currentframe().f_back
        caller_filename = os.path.basename(caller_frame.f_code.co_filename)
        caller_lineno = caller_frame.f_lineno
        message = f"{caller_filename}:{caller_lineno} - {msg}"
        self.info_logger.warning(message, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        caller_frame = inspect.currentframe().f_back
        caller_filename = os.path.basename(caller_frame.f_code.co_filename)
        caller_lineno = caller_frame.f_lineno
        message = f"{caller_filename}:{caller_lineno} - {msg}"
        self.error_logger.error(message, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        caller_frame = inspect.currentframe().f_back
        caller_filename = os.path.basename(caller_frame.f_code.co_filename)
        caller_lineno = caller_frame.f_lineno
        message = f"{caller_filename}:{caller_lineno} - {msg}"
        self.error_logger.critical(message, *args, **kwargs)

    def ASSERT_EQ(self, value, expect):
        """
        断言是否相等
        :param value: 实际值
        :param expect: 期望值
        :return: 无
        """
        caller_frame = inspect.currentframe().f_back
        caller_filename = os.path.basename(caller_frame.f_code.co_filename)
        caller_lineno = caller_frame.f_lineno
        message = f"{caller_filename}:{caller_lineno}"
        try:
            assert value == expect
        except AssertionError:
            self.error_logger.error(f"{message}-{value}不等于{expect}")
        else:
            self.info_logger.info(f"{message}-{value}等于{expect}")


if __name__ == "__main__":
    log = Logger()
    log.debug(11111)
    log.info(222222)
    log.warning(333)
    log.error(44444)
    log.critical(55)
