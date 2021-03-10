from airtest.core.api import *


def device_open_app():
    "打开app"
    stop_app('com.road7.phoenix')
    start_app('com.road7.phoenix')
    print("app已打开")
    sleep(15)



if __name__ == '__main__':
    device_open_app()
