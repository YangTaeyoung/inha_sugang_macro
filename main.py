import sys
import time
from util.crawler import *
from util.time_util import *

inha_browser, time_browser = get_drivers()
USER_MODE = True
is_general = False
if USER_MODE:
    print_shop_line()
    print("인하대학교 수강신청 봇")
    print("제작자: 양태영, 버그 리포트: 0130yang@gmail.com")
    print("################################# 주의사항 #####################################")
    print("해당 프로그램은 학습용이며, 교칙에 의거하여 \"실제로 사용하는 것을 금합니다.\"")
    print("이를 어길 시 모든 책임은 사용자 본인에게 있습니다.")
    print_shop_line()
    flag = input("동의하십니까? (Y/N): ")
    if flag.lower() != "y":
        sys.exit()
    console_clear()
    print_shop_line()
    print("해당 화면은 콘솔창만 보이게 됩니다.")
    print("실제로 창은 보이지 않으나, 수강신청을 자동으로 시도합니다.")
    print("백그라운드에서 작업을 시도하므로 다른 작업을 하셔도 무관합니다.")
    print_shop_line()
    print("해당 프로그램에 의해 발생한 피해(수강신청 실패 등)은 제작자가 책임지지 않습니다.")
    print_shop_line()
    time.sleep(4)
    console_clear()
    print("수강신청 시각을 자동으로 가져옵니다.")
    print_shop_line()
    inha_browser.switch_to.frame("ifrm")
    inha_browser.switch_to.frame("MainFrame")
    # 수강신청 목록 가져오기
    plans = find_sugang_date_automatically(inha_browser)
    print("가져오기를 성공하였습니다. 아래의 리스트에서 해당하는 수강신청 시작 시각을 골라주세요")
    print_single_line()
    for i, plan in enumerate(plans):
        print(f"{i + 1}. {plan[1].strftime('%Y-%m-%d %H:%M')} | {plan[0]}")
    print("0. 해당하는 시각 없음(직접 입력)")
    print_single_line()
    flag = int(input("어떤 시각을 고르시겠습니까?(숫자만 입력):")) - 1
    if flag == -1:
        print_shop_line()
        print("직접 시작시각을 입력받습니다.")
        year = int(input("연도를 입력하세요(ex. 2022): "))
        month = int(input("월을 입력하세요(1~12): "))
        day = int(input("일을 입력하세요(1~31)"))
        hour = int(input("시를 입력하세요(0~23):"))
        minute = int(input("분을 입력하세요(0~59): "))
        start_time = datetime.datetime(
            year=year, month=month,
            day=day, hour=hour,
            minute=minute, second=0
        )
    else:
        # 수강 신청 시작 시간 세팅
        start_time = plans[flag][1]
        if "일반" in plans[flag][0]:
            is_general = True
    print_shop_line()
    print(f"설정된 시각: {start_time.isoformat()}")
console_clear()
inha_browser.switch_to.parent_frame()
inha_browser.switch_to.frame("MenuFrame")
time.sleep(1)
# 로그인
login(inha_browser)
print_shop_line()
print("로그인을 성공하였습니다. ")

print_shop_line()
if USER_MODE:
    print("설정한 시각에 따라 3초 후 타이머가 시작됩니다.")
    time.sleep(3)
    go_timer(start_time, time_browser)

# 수강신청 페이지로 이동
inha_browser.execute_script('moveUrl("SU_53001/Sugang_Save.ASPX")')
inha_browser.switch_to.parent_frame()
inha_browser.switch_to.frame("MainFrame")

# 수강신청 페이지에서 첫 alert창 기다렸다 무효화
if not is_general:
    wait_alert(inha_browser)
print("INFO: 첫 알림 메시지를 무효화 합니다.")
# 수강신청 대기 리스트가 있으면 수강신청 시도 계속하기
while count := (len(inha_browser.find_elements(by=By.XPATH, value='//*[@id="dgList2"]/tbody//*')) // 11):
    print(f"INFO: 수강신청 항목이 {count}개 남았습니다. 계속 시도합니다.")
    try_sugang(inha_browser)
print("수강신청이 성공적으로 종료되었습니다. 축하합니다.")
