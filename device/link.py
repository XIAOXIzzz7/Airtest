from airtest.core.api import *
from device.number import appid, modelid
from log.local_log import log_run
from airtest.report.report import simple_report

log_run = log_run()
"链接手机"


def link_1():
    "引入设备号"
    serialno = appid()
    model = modelid()
    auto_setup(__file__, logdir=f'{log_run}', devices=['Android://127.0.0.1:5037/{serial}'.format(serial=serialno)])
    print(f'手机已连接:{model}')


def link_report():
    simple_report(__file__, logpath=f"{log_run}", logfile=f'{log_run}/log.txt', output=f"{log_run}/log.html")


if __name__ == "__main__":
    link_1()
    # link_report()