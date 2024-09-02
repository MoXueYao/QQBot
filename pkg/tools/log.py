import time


class log:
    """
    日志模块。
    """

    def info(msg: str) -> None:
        """
        打印信息日志。
        """
        time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(f"[{time_str}] [INFO] {msg}")

    def warn(msg: str) -> None:
        """
        打印警告日志。
        """
        time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(f"\033[33m[{time_str}] [WARN] {msg}\033[0m")

    def error(msg: str) -> None:
        """
        打印错误日志。
        """
        time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(f"\033[31m[{time_str}] [ERROR] {msg}\033[0m")
