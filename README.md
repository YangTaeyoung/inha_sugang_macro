# Hello Inha Sugang Macro 👋

- 인하대학교 수강신청 **"학습용"** 봇입니다.

---

# 목적

- Selenium을 통한 크롤링과, 웹 브라우징 도구를 통해 어느정도까지 테스트가 가능한 지 알아보기 위해서 제작되었습니다.
- 어디까지나 학습용으로 제작되었으며, **불법에 동조하기 위해 제작된 프로그램이 아님**을 사전에 밝힙니다.
- 추후 문제가 될 시 즉시 비공개 처리하도록 하겠습니다.

---

# 주의사항

- 해당 메크로는 교칙에 의거하여 실제 사용하는 것을 금하며, 학습용으로 사용하길 권장합니다.
- 본 프로그램은 학습용이며 실제 사용시 발생하는 불이익에 제작자가 책임을 지지 않습니다.
- 인터넷 속도에 따라 반응속도가 늦을 수 있습니다.
- 수강신청 봇은 수강신청 장바구니 기능을 통해 담겨져 있는 후보군에 대해서만 수강신청을 시도합니다.
- 장바구니에 담겨져 있지 않은 것은 수강신청 시도 대상이 아니며, 우선수강신청으로 인해 이미 성공한 것을 구분하지 못합니다. 따라서 수강신청 장바구니를 정리하고 시도하길 권장합니다.

---

# Getting Started

## How To Install

### Python 설치

- Python을 각자의 OS에 맞게 설치합니다.
    - [Python 다운로드](https://www.python.org/downloads/)

### Clone this repository

- 아래 명령어를 통해 해당 레포지토리를 복제합니다.
    ```bash
    $ git clone https://github.com/YangTaeyoung/inha_sugang_macro.git
    $ cd inha_sugang_macro
    ```

### Setup virtual environment

글로벌로 설정해도 상관 없지만, 가상환경을 사용하는 것을 권장합니다.

- virtualenv를 설치하고 셋업합니다.
    ```bash
    $ pip install virtualenv
    $ virtualenv venv
    ```

- 가상환경을 실행합니다.
    ```bash
    $ source venv/bin/activate
    ```

### Install dependencies

- 필요한 라이브러리를 설치합니다.
    ```bash
    $ pip install -r requirements.txt
    ```

## How To Use

### 1. 본 프로그램은 크롤링 학습용 프로그램입니다. 아래 동의사항에 동의합니다.

![image](https://user-images.githubusercontent.com/59782504/154207529-6fc68bd7-9588-4309-a740-3e3c18e7cfae.png)

### 2. 수강신청 시각을 자동으로 가져옵니다. 아래 시간에서 번호에 맞는 시간을 고릅니다.

> 0번을 선택하여 직접 지정할 수 있습니다.

![image](https://user-images.githubusercontent.com/59782504/154207631-0443f09b-c596-4eea-ac97-5412baad9d12.png)

### 3. 아이디와 비밀번호를 입력하여 로그인합니다.

> 따로 저장하지 않으니 안심하고 사용할 수 있습니다.

![image](https://user-images.githubusercontent.com/59782504/154210307-6a9ac7a8-0ac6-4dbf-ad57-923d3a79e4c3.png)

### 4. 남은 시간이 나옵니다. 타이머가 끝날 경우 자동적으로 수강신청 시도를 시작합니다.

![image](https://user-images.githubusercontent.com/59782504/153318940-f53e51eb-e652-4566-be0c-0e178e11026f.png)

![image](https://user-images.githubusercontent.com/59782504/154210542-fd5d6bd7-f475-40b7-ad19-b7ffcf4cf110.png)
