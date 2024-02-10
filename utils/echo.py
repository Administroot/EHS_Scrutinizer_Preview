def format_print(status: str, msg: str) -> None:
    """人性化的终端输出信息
    :param status: 状态
    :param msg: 信息
    """
    if status == "ERROR":
        print(f"\033[31m[{status}]\033[0m {msg}")
    elif status == "WARN":
        print(f"\033[33m[{status}]\033[0m {msg}")
    elif status == "INFO":
        print(f"\033[34m[{status}]\033[0m {msg}")