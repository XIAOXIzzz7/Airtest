

"设定报告路径"
def log_report():
    from airtest.report.report import simple_report
    simple_report(__file__, logpath="D:/test/log", output="D:/test/log/log.html")


if __name__ == "__main__":
    log_report()
