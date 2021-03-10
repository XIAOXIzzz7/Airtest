from airtest.core.api import *
from device.number import appid

"引入设备号"
serialno = appid()
"链接手机"


def link_1():
    auto_setup(__file__, devices=['Android://127.0.0.1:5037/{serial}'.format(serial=serialno)])


if __name__ == "__main__":
    link_1()