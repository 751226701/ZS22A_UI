import os
import logging
import inspect
import colorlog
from Config.Config import Config
from logging.handlers import RotatingFileHandler

LOG_PATH = Config.logs    # 日志路径
PREFIX_NAME = ""          # 日志前缀名
LOG_INFO = "info.log"     # 日志名称
LOG_ERROR = "error.log"   # 日志名称


class Logger:
    def __init__(self, console_output=True, file_output=True):
        """
        :param console_output: 是否输出到控制台
        :param file_output: 是否写入到日志文件
        """
        if os.path.exists(LOG_PATH):
            pass
        else:
            os.mkdir(LOG_PATH)
        self.info_logger = logging.getLogger("info")  # 创建info级别日志记录器
        self.error_logger = logging.getLogger("error")  # 创建error级别日志记录器
        self.format = logging.Formatter('[%(asctime)s][%(levelname)s] - %(message)s')  # 格式化输出
        # 指定文件位置文件名以及输出格式
        if file_output:
            info_file_handler = RotatingFileHandler(
                "%s/%s%s" % (LOG_PATH, PREFIX_NAME, LOG_INFO),
                maxBytes=1024 * 1024 * 10,  # 每个日志文件最大10MB
                backupCount=5  # 保留5个旧日志文件
            )
            info_file_handler.setFormatter(self.format)

            error_file_handler = RotatingFileHandler(
                "%s/%s%s" % (LOG_PATH, PREFIX_NAME, LOG_ERROR),
                maxBytes=1024 * 1024 * 10,  # 每个日志文件最大10MB
                backupCount=5  # 保留5个旧日志文件
            )
            error_file_handler.setFormatter(self.format)

            self.info_logger.addHandler(info_file_handler)
            self.error_logger.addHandler(error_file_handler)
        # 创建控制台处理器,将日志同步输出到控制台
        if console_output:
            console_handler = logging.StreamHandler()
            console_formatter = colorlog.ColoredFormatter(
                '%(log_color)s[%(asctime)s][%(levelname)s] - %(message)s',
                log_colors={
                    'DEBUG': 'cyan',
                    'INFO': 'green',
                    'WARNING': 'yellow',
                    'ERROR': 'red',
                    'CRITICAL': 'bold_red',
                }
            )
            console_handler.setFormatter(console_formatter)
            self.info_logger.addHandler(console_handler)  # 添加控制台处理器
            self.error_logger.addHandler(console_handler)  # 添加控制台处理器
        # 指定日志的最低输出级别
        self.info_logger.setLevel(logging.DEBUG)
        self.error_logger.setLevel(logging.ERROR)

    def debug(self, msg, *args, **kwargs):
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


if __name__ == "__main__":
    log = Logger()
    log.debug(11111)
    log.info(222222)
    log.warning(333)
    log.error(44444)
    log.critical(55)
