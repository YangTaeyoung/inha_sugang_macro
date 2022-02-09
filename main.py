import sys

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


def login(driver, id, password):
    driver.switch_to.frame("ifrm")
    driver.switch_to.frame("MenuFrame")
    driver.implicitly_wait(3)
    driver.find_element(by=By.ID, value="txtCode").send_keys(id)
    driver.find_element(by=By.ID, value="txtPassword").send_keys(password)
    driver.find_element(by=By.ID, value="ibtnLogin").click()


def wait_alert(driver):
    while True:
        try:
            if alert := driver.switch_to.alert:
                alert.accept()
                break
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
        # 수강신청이 성공되었습니다./인원이 가득 찼습니다. alert창 무효화
        wait_alert(driver)


print("제작자: 양태영")
print("#########################################################################")
print("프로그램을 종료할 때는 꼭 Ctrl + C를 통해 종료해주세요!!")
print("############################# 주의사항 ##################################")
print("해당 프로그램은 학습용이며, 교칙에 의거하여 실제로 사용하는 것을 금합니다.")
print("이를 어길 시 모든 책임은 사용자 본인에게 있습니다.")
print("#########################################################################")
flag = input("인지하셨습니까? (Y/N): ")

if flag.lower() != "y":
    sys.exit()

# 아이디, 비밀번호 입력 받는 곳
id = input("유저 정보를 입력 받습니다.\n아이디를 입력해주세요: ")
pw = input("비밀번호를 입력해주세요: ")
# 현재 날짜 가져오기 (년도, 월, 일 만)
today = datetime.datetime.now()
# 수강 신청 시작 시간 세팅
hours = int(input("수강신청 시작 시는 언제입니까? (0~24): "))
minute = int(input("수강신청 시작 분은 언제입니까? (0~59): "))
times = datetime.time(hour=hours, minute=minute, second=0)
start_time = datetime.datetime.combine(today, times)
print(f"설정된 시각: {start_time.isoformat()}")

# 전체 수강신청 흐름 담당
driver = set_chrome_driver()
# 원격으로 시간 정보 받아오는 담당
driver_time = set_chrome_driver(headless=True)
# 수강 신청 사이트 오픈 (유저에게 보이게 설정)
driver.get("https://sugang.inha.ac.kr/sugang/")
# 시간 보는 사이트 오픈 (유저에게 보이지 않게 설정)
driver_time.get("https://time.navyism.com/?host=sugang.inha.ac.kr")

# 로그인
login(driver, id, pw)

while True:
    if (rest := (start_time - get_now(driver_time))).seconds <= 0:
        break
    print(f"남은 시간: {rest.seconds}초")

# 수강신청 페이지로 이동
driver.execute_script('moveUrl("SU_53001/Sugang_Save.ASPX")')
driver.switch_to.parent_frame()
driver.switch_to.frame("MainFrame")

# 수강신청 페이지에서 첫 alert창 기다렸다 무효화
wait_alert(driver)

# 수강신청 대기 리스트가 있으면 수강신청 시도 계속하기
while len(driver.find_elements(by=By.XPATH, value='//*[@id="dgList2"]/tbody//*')) // 11:
    try_sugang(driver)

print("모든 수강신청이 종료되었습니다. 축하합니다!")