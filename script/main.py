from script.chapter_one import *
from device.link import link_1
from device.open_app import device_open_app
from log.logger import log_logger


def main_run():

    "设置日志只显示错误"
    log_logger()
    "链接手机"
    link_1()
    "打开app"
    device_open_app()
    "运行脚本"
    script_chapter_one()


if __name__ == '__main__':
    main_run()
