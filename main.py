import sys

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import datetime


def set_chrome_driver(headless=False):
    chrome_options = webdriver.ChromeOptions()
    if headless:
        chrome_options.add_argument("headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver


def get_now(driver_time):
    text = driver_time.find_element(by=By.ID, value="time_area").text
    time = datetime.datetime.strptime(text, "%Y년 %m월 %d일 %H시 %M분 %S초")
    return time


def login(driver):
    while True:
        # 아이디, 비밀번호 입력 받는 곳
        id = input("유저 정보를 입력 받습니다.\n학번을 입력해주세요: ")
        pw = input("비밀번호를 입력해주세요: ")

        driver.find_element(by=By.ID, value="txtCode").clear()
        driver.find_element(by=By.ID, value="txtCode").send_keys(id)
        driver.find_element(by=By.ID, value="txtPassword").clear()
        driver.find_element(by=By.ID, value="txtPassword").send_keys(pw)
        driver.find_element(by=By.ID, value="ibtnLogin").click()
        try:
            alert = driver.switch_to.alert
            alert.accept()
            print("비밀번호가 틀렸습니다. 다시 입력해주세요.")
        except selenium.common.exceptions.NoAlertPresentException:
            name = driver.find_element(by=By.XPATH, value='//*[@id="lblItis_KName"]').text
            print(f"{name}님 반갑습니다! 성공적으로 로그인 하였습니다.")
            break


def wait_alert(driver):
    while True:
        try:
            if alert := driver.switch_to.alert:
                text = alert.text
                alert.accept()
                return text
        except:
            continue


def try_sugang(driver):
    for i in range(1, len(driver.find_elements(by=By.XPATH, value='//*[@id="dgList2"]/tbody//*')) // 11 + 1):
        try:
            driver.find_element(by=By.XPATH,
                                value=f"/html/body/form/div[2]/div[2]/div[4]/table/tbody/tr[{i}]/td[9]/input").click()
        except:
            continue
        # 수강신청 하시겠습니까? alert창 무효화
        wait_alert(driver)
        print("수강신청 질문 창 무효화")
        # 수강신청이 성공되었습니다./인원이 가득 찼습니다. alert창 무효화
        wait_alert(driver)
        print("수강신청 성공/실패 창 무효화")


USER_MODE = False

if USER_MODE:
    print("################################################################################")
    print("인하대학교 수강신청 봇")
    print("제작자: 양태영, 버그 리포트: 0130yang@gmail.com")
    print("################################################################################")
    print("Windows: 프로그램을 종료할 때는 꼭 Ctrl + C를 통해 종료해주세요!! (명령 프롬프트 창에서)")
    print("Mac OS: 프로그램을 종료할 때는 터미널에서 Command + Q를 눌러 완전히 종료해주세요")
    print("################################# 주의사항 #####################################")
    print("해당 프로그램은 학습용이며, 교칙에 의거하여 \"실제로 사용하는 것을 금합니다.\"")
    print("이를 어길 시 모든 책임은 사용자 본인에게 있습니다.")
    print("################################################################################")
    flag = input("동의하십니까? (Y/N): ")
    if flag.lower() != "y":
        sys.exit()
    print("################################################################################")
    print("백그라운드에서 실행하실 수 있습니다. 크롬창이 보이지 않습니다만, \n 해당기능은 테스트가 완전히 실행되지 않았습니다.")
    print("따라서 불안정하게 동작할 수 있습니다.")
    print("단, 백그라운드에서 실행하실 경우 하시던 작업을 지속하실 수 있습니다.")
    print("제작자는 2개의 컴퓨터를 가진 경우 컴퓨터 하나에는 메크로를 백그라운드가 아닌 경우\n로 실행시키고, 본 컴퓨터에서 실제 수강신청을 하길 권장합니다.")
    flag = input("백 그라운드에서 실행하시겠습니까? (Y/N): ")
    print("################################################################################")
    print("해당 버전은 Beta 버전입니다.")
    print("오류가 발생할 수 있으며,")
    print("해당 프로그램에 의해 발생한 피해(수강신청 실패 등)은 제작자가 책임지지 않습니다.")
    print("################################################################################")

    # 현재 날짜 가져오기 (년도, 월, 일 만)
    today = datetime.datetime.now()
    # 수강 신청 시작 시간 세팅
    hours = int(input("수강신청 시작 시는 언제입니까? (0~24): "))
    minute = int(input("수강신청 시작 분은 언제입니까? (0~59): "))
    times = datetime.time(hour=hours, minute=minute, second=0)
    start_time = datetime.datetime.combine(today, times)
    print(f"설정된 시각: {start_time.isoformat()}")

    if flag.lower() == "y":
        headless = True
    else:
        headless = False
# 전체 수강신청 흐름 담당
driver = set_chrome_driver(headless=False)
# 원격으로 시간 정보 받아오는 담당
driver_time = set_chrome_driver(headless=True)
# 수강 신청 사이트 오픈 (유저에게 보이게 설정)
driver.get("https://sugang.inha.ac.kr/sugang/")
# 시간 보는 사이트 오픈 (유저에게 보이지 않게 설정)
driver_time.get("https://time.navyism.com/?host=sugang.inha.ac.kr")

    # while True:
    #     if (rest := (start_time - get_now(driver_time))).seconds <= 0:
    #         break
    #     print(f"남은 시간: {rest.seconds}초")

# 프레임 이동
driver.switch_to.frame("ifrm")
driver.switch_to.frame("MenuFrame")
driver.implicitly_wait(1)

# 로그인
login(driver)

# 수강신청 페이지로 이동
driver.execute_script('moveUrl("SU_53001/Sugang_Save.ASPX")')
driver.switch_to.parent_frame()
driver.switch_to.frame("MainFrame")

# 수강신청 페이지에서 첫 alert창 기다렸다 무효화
print(wait_alert(driver))
print("INFO: 첫 알림 메시지를 무효화 합니다.")
# 수강신청 대기 리스트가 있으면 수강신청 시도 계속하기
while count := (len(driver.find_elements(by=By.XPATH, value='//*[@id="dgList2"]/tbody//*')) // 11):
    print(f"수강신청 항목이 {count}개 남았습니다. 계속 시도합니다.")
    try_sugang(driver)

print("수강신청이 종료되었습니다.")
