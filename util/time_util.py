import datetime
from .crawler import get_now
from .console import console_clear


def get_diff_time_as_seconds(time1: datetime.datetime, time2: datetime.datetime):
    diff = time1 - time2
    return 86400 * diff.days + diff.seconds


def print_rest_time(seconds: int):
    day = seconds // 86400
    hour = seconds % 86400 // 3600
    minute = seconds % 3600 // 60
    second = seconds % 60
    print(f"남은시간: {day}일 {hour}시간 {minute}분 {second}초")


def go_timer(start_time: datetime.datetime, time_browser):
    while True:
        if (seconds := get_diff_time_as_seconds(start_time, get_now(time_browser))) <= 0:
            break
        console_clear()
        print_rest_time(seconds)
