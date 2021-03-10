import logging

"设定日志只显示错误信息"
def log_logger():
    logger = logging.getLogger('airtest')
    logger.setLevel(logging.ERROR)

if __name__ == "__main__":
    log_logger()