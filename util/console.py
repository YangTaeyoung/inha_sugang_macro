import os
import platform
# 콘솔 지우는 함수
def console_clear():
    clear_commands = {
        "Darwin": "clear",
        "Windows": "cls"
    }
    os.system(clear_commands[platform.system()])


def print_shop_line():
    print("################################################################################")


def print_single_line():
    print("--------------------------------------------------------------------------------")
