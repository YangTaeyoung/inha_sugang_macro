import sys

from .console import *
import selenium
import datetime
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


# 수강 신청일자를 가져오는 함수
def find_sugang_date_automatically(driver: webdriver.Chrome):
    i = 1
    plan_dates = list()
    while True:
        try:
            plan_text = driver.find_element(by=By.XPATH, value=f'//*[@id="dgSchedule"]/tbody/tr[{i}]/td[2]').text
        except selenium.common.exceptions.NoSuchElementException:
            break
        if "수강신청" in plan_text:
            plan_date = driver.find_element(by=By.XPATH,
                                            value=f'//*[@id="dgSchedule"]/tbody/tr[{i}]/td[1]').text.split()
            plan_date[0] = int(plan_date[0][:-1])
            plan_date[1] = int(plan_date[1][:-1])
            plan_date[2] = int(plan_date[2][:-3])
            plan_date[3] = list(map(int, plan_date[3].split(":")))
            plan_date = plan_date[:4]
            plan_date = datetime.datetime(
                year=plan_date[0],
                month=plan_date[1],
                day=plan_date[2],
                hour=plan_date[3][0],
                minute=plan_date[3][1]
            )
            plan_dates.append([plan_text, plan_date])
        i += 1
    return plan_dates


# 크롬 드라이버를 세팅하고, 실행시키는 함수
def set_chrome_driver(headless=False):
    chrome_options = webdriver.ChromeOptions()
    if headless:
        chrome_options.add_argument("headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver


# 드라이버를 가져오는 함수
def get_drivers():
    driver = set_chrome_driver(headless=True)
    driver.get("https://sugang.inha.ac.kr/sugang/")
    console_clear()
    driver_time = set_chrome_driver(headless=True)
    driver_time.get("https://time.navyism.com/?host=sugang.inha.ac.kr")
    console_clear()
    return driver, driver_time


# 현재 날짜를 가져오는 함수
def get_now(driver_time):
    text = driver_time.find_element(by=By.ID, value="time_area").text
    time = datetime.datetime.strptime(text, "%Y년 %m월 %d일 %H시 %M분 %S초")
    return time


# 로그인 시키는 함수, 비밀번호가 틀리면 다시 입력하라는 함수가 출력
def login(driver):
    print_shop_line()
    print("로그인을 시작합니다.")
    print_shop_line()
    while True:
        # 아이디, 비밀번호 입력 받는 곳
        id = input("유저 정보를 입력 받습니다.\n학번을 입력해주세요: ")
        pw = input("비밀번호를 입력해주세요: ")
        print_shop_line()
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


def try_sugang(start, driver: selenium.webdriver.Chrome):
    for i in range(start, len(driver.find_elements(by=By.XPATH, value='//*[@id="dgList2"]/tbody//*')) // 11 + start):
        try:
            if len(driver.find_elements(by=By.XPATH, value='//*[@id="dgList2"]/tbody//*')) // 11 == 1:
                until_tr = f"/html/body/form/div[2]/div[2]/div[4]/table/tbody/tr/"
            else:
                until_tr = f"/html/body/form/div[2]/div[2]/div[4]/table/tbody/tr[{i}]/"
            title = driver.find_element(by=By.XPATH,
                                        value=f"{until_tr}td[2]").text
            print(f"INFO: {title} 에 수강신청을 시도합니다.")
            button = driver.find_element(by=By.XPATH,
                                         value=f"{until_tr}td[9]/input")
            button.click()
            # 수강신청 하시겠습니까? alert창 무효화
            wait_alert(driver)
            print("INFO: 수강신청 질문 창을 무효화 합니다.")
            # 수강신청이 성공되었습니다./인원이 가득 찼습니다. alert창 무효화
            print(f"INFO: {title}: {wait_alert(driver)}")
        except selenium.common.exceptions.NoSuchElementException:
            try_sugang(start + 1, driver)
            return
