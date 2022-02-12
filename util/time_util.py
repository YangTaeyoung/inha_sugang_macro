import datetime


def get_diff_time_as_seconds(time1: datetime.datetime, time2: datetime.datetime):
    diff = time1 - time2
    return 86400 * diff.days + diff.seconds


def print_rest_time(seconds: int):
    day = seconds // 86400
    hour = seconds % 86400 // 3600
    minute = seconds % 3600 // 60
    second = seconds % 60
    print(f"남은시간: {day}일 {hour}시간 {minute}분 {second}초")
