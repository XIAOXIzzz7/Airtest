from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

"实例化"
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


"初始化"
auto_setup(__file__)
"获取手机序列号"


def appid():
    a = poco.adb_client.get_device_info()
    print(f'手机信息:{a}')
    return a['serialno']


"获取手机型号"
def modelid():
    b = poco.adb_client.get_device_info()
    return b['model']


if __name__ == "__main__":
    appid()
    modelid()
