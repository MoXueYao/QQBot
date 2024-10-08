import time


def save_print_log(log_msg: str) -> None:
    """
    保存日志文件
    """
    with open("logs.txt", "a", encoding='utf-8') as fp:
        fp.write(log_msg.strip())
        fp.write("\r\n")
    print(log_msg)


class log:
    """
    日志模块。
    """

    def info(msg: str) -> None:
        """
        打印信息日志。
        """
        time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        log_msg = f"[{time_str}] [INFO] {msg}"
        save_print_log(log_msg)

    def warn(msg: str) -> None:
        """
        打印警告日志。
        """
        time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        log_msg = f"\033[33m[{time_str}] [WARN] {msg}\033[0m"
        save_print_log(log_msg)

    def error(msg: str) -> None:
        """
        打印错误日志。
        """
        time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        log_msg = f"\033[31m[{time_str}] [ERROR] {msg}\033[0m"
        save_print_log(log_msg)
