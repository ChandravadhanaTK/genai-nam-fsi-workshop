import os
import sys
import logging
from enum import Enum


class LogLevel(Enum):
    """
    Enum for log level
    """
    CRITICAL = 50
    ERROR = 40
    WARNING = 30
    INFO = 20
    DEBUG = 10
    NOTSET = 0


def init_logger():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] : %(message)s'))

    logging.basicConfig(level=get_log_level(),
                        handlers=[console_handler])


def get_log_level():
    """
    Return the current log level
    :return: log_level
    """
    _level = os.getenv('LOG_LEVEL', 'INFO')
    return int(str(LogLevel[_level].value))
