# inha_sugang_macro_v1
> 인하대학교 수강신청 **"학습용"** 봇입니다.
<hr>

### 목적
> Selenium을 통한 크롤링과, 웹 브라우징 도구를 통해 어느정도까지 테스트가 가능한 지 알아보기 위해서 제작되었습니다.

> 어디까지나 학습용으로 제작되었으며, **불법에 동조하기 위해 제작된 프로그램이 아님**을 사전에 밝힙니다.

> 추후 문제가 될 시 즉시 비공개 처리하도록 하겠습니다.
<hr>

### 주의사항
> 해당 메크로는 교칙에 의거하여 실제 사용하는 것을 금하며, 학습용으로 사용하길 권장합니다. 본 프로그램은 학습용이며 실제 사용시 발생하는 불이익에 제작자가 책임을 지지 않습니다.

> 인터넷 속도에 따라 반응속도가 늦을 수 있습니다.

> ~~백그라운드 환경은 테스트 되지 않았습니다. 되도록 백그라운드가 아닌 상태에서 실행하길 권장합니다.~~

> 백그라운드 환경이 테스트 되었습니다. (2022-02-10) 수강신청의 전 과정은 백그라운드에서 진행됩니다.

> 수강신청 봇은 수강신청 장바구니 기능을 통해 담겨져 있는 후보군에 대해서만 수강신청을 시도합니다. 장바구니에 담겨져 있지 않은 것은 수강신청 시도 대상이 아니며, 우선수강신청으로 인해 이미 성공한 것을 구분하지 못합니다. 따라서 수강신청 장바구니를 정리하고 시도하길 권장합니다.

<hr>

### 환경설정

> Python 환경에서 제작되었습니다.'

> 추가적인 환경설정은 하지 않아도 됩니다.

> 코드를 직접 실행하실 분은 아래와 같은 모듈을 필요로 합니다.

```python
pip install selenium
pip install webdriver_manager
```
<hr>

### How To Use

<img width="652" alt="image" src="https://user-images.githubusercontent.com/59782504/154207529-6fc68bd7-9588-4309-a740-3e3c18e7cfae.png">


> 1. 본 프로그램은 크롤링 학습용 프로그램입니다. 아래 동의사항에 동의합니다.

![image](https://user-images.githubusercontent.com/59782504/153318633-ba7a54bc-4da3-42ff-b534-570f898a8b68.png)

> 2. 수강신청 시각을 자동으로 가져옵니다. 아래 시간에서 번호에 맞는 시간을 고릅니다. (직접 지정할 수 있습니다.)

<img width="646" alt="image" src="https://user-images.githubusercontent.com/59782504/154207631-0443f09b-c596-4eea-ac97-5412baad9d12.png">

> 아이디와 비밀번호를 입력하여 로그인합니다. (따로 저장하지 않으니 안심하고 사용할 수 있습니다.)

<img width="251" alt="image" src="https://user-images.githubusercontent.com/59782504/154210307-6a9ac7a8-0ac6-4dbf-ad57-923d3a79e4c3.png">

> 4. 수강신청 시작 시각을 묻습니다. 10시 00분에 시작한다면 위의 예시처럼 10, 00을 차례대로 입력합니다.

![image](https://user-images.githubusercontent.com/59782504/153318940-f53e51eb-e652-4566-be0c-0e178e11026f.png)

> 5. 남은 시간이 나옵니다. 타이머가 끝날 경우 자동적으로 수강신청 시도를 시작합니다.

<img width="540" alt="image" src="https://user-images.githubusercontent.com/59782504/154210542-fd5d6bd7-f475-40b7-ad19-b7ffcf4cf110.png">

<hr>


### V1 

> 아이디, 비밀번호 틀릴 시 식별하도록 설정할 예정입니다.

> 백그라운드 외에서의 실행을 제한할 예정입니다.

> 수강신청 목록을 인식하고, 수강신청시 해당 수강신청 성공/실패 여부를 반영할 예정입니다.

<hr>


### Release V1 수정 내용
> 수강 신청 목록 1개가 남았을 때 신청되지 않던 에러를 수정하였습니다.

> 아이디 비밀번호가 틀렸을 때 구분하게 바뀌었습니다.

> 수강신청 시간 목록을 자동으로 가져오는 기능을 추가하였습니다

### Download Release
> **Windows** (11 Tested): https://github.com/YangTaeyoung/inha_sugang_macro_v1/raw/master/Release/(Windows)%20InhaSugangTryBot%20V0.1%20Beta.exe

> **Mac OS** (Monetery 12.2 Tested): https://github.com/YangTaeyoung/inha_sugang_macro_v1/raw/master/Release/(Mac)%20InhaSugangTryBot%20V0.1%20Beta
