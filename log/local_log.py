import os



"自动生成日志文件夹"
def util_local_log(log_path, number):

    while True:
        log_file = f'/log_{number}'
        decide = os.path.exists(log_path + log_file)

        if not decide:
            path = (log_path+log_file)
            print(f'创建日志目录{path}')
            os.makedirs(path)

            return path

        else:
            number += 1
            continue


def log_run():
    path = 'D:/log'
    # print(util_local_log(path, 1))
    return util_local_log(path, 1)


if __name__ == '__main__':

    log_run()




















