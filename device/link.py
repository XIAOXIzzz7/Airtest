from airtest.core.api import *
from device.number import appid, modelid



"链接手机"
def link_1():
    "引入设备号"
    serialno = appid()
    model = modelid()
    auto_setup(__file__, devices=['Android://127.0.0.1:5037/{serial}'.format(serial=serialno)])
    print(f'手机已连接:{model}')


if __name__ == "__main__":
    link_1()