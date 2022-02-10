# inha_sugang_macro_v1
> 인하대학교 수강신청 "학습용" 봇입니다.
<hr>

### 목적
> Selenium을 통한 크롤링과, 웹 브라우징 도구를 통해 어느정도까지 테스트가 가능한 지 알아보기 위해서 제작되었습니다.

> 어디까지나 학습용으로 제작되었으며, 불법에 동조하기 위해 제작된 프로그램이 아님을 사전에 밝힙니다.

> 추후 문제가 될 시 즉시 비공개 처리하도록 하겠습니다.
<hr>

### 주의사항
> 해당 메크로는 교칙에 의거하여 실제 사용하는 것을 금하며, 학습용으로 사용하길 권장합니다. 본 프로그램은 학습용이며 실제 사용시 발생하는 불이익에 제작자가 책임을 지지 않습니다.

> 인터넷 속도에 따라 반응속도가 늦을 수 있습니다.

> ~~백그라운드 환경은 테스트 되지 않았습니다. 되도록 백그라운드가 아닌 상태에서 실행하길 권장합니다.~~

> 백그라운드 환경이 테스트 되었습니다. (2022-02-10) 백그라운드 환경에서 사용하길 권장합니다.

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

![image](https://user-images.githubusercontent.com/59782504/153318378-a948b7ae-11f7-44f3-8705-8e090bff8467.png)

1. 본 프로그램은 크롤링 학습용 프로그램입니다. 아래 동의사항에 동의합니다.

![image](https://user-images.githubusercontent.com/59782504/153318532-823f6670-5f04-4ef8-84f6-bebd05704c79.png)

2. 백그라운드에서 실행 여부를 묻습니다. Y나 N을 누르시면 됩니다. (Y를 권장합니다.)

![image](https://user-images.githubusercontent.com/59782504/153318633-ba7a54bc-4da3-42ff-b534-570f898a8b68.png)

3. 아이디와 비밀번호를 묻습니다. 실제 로그인 되는 비밀번호로 입력하셔야 하며, 해당 프로그램은 로그인을 시도할 뿐 로그인 실패를 알아내지 못합니다. 따라서 사전에 아이디와 비밀번호가 로그인 가능한지 확인하셔야 합니다.

![image](https://user-images.githubusercontent.com/59782504/153318795-d21b0592-dce2-4836-ba0c-f8a23c1f42a4.png)

4. 수강신청 시작 시각을 묻습니다. 10시 00분에 시작한다면 위의 예시처럼 10, 00을 차례대로 입력합니다.

![image](https://user-images.githubusercontent.com/59782504/153318940-f53e51eb-e652-4566-be0c-0e178e11026f.png)

5. 남은 시간이 나옵니다. 타이머가 끝날 경우 자동적으로 수강신청 시도를 시작합니다.

<hr>

### 알려진 버그
> 백그라운드가 아닌 상황에서 실행 시 윈도우 터미널에서 그냥 종료시 크롬 창이 무한생성되는 버그가 있습니다. (Ctrl + C로 종료시 해당 문제는 없어집니다.)

> 창이 무한생성 될 때 로그오프을 하셨다가 다시 로그온 하시거나, 컴퓨터를 재부팅하시면 해결됩니다. 
<hr>

### 릴리즈 (0.1 Beta)
> Windows: https://github.com/YangTaeyoung/inha_sugang_macro_v1/raw/master/Release/(Windows)%20InhaSugangTryBot%20V0.1%20Beta.exe

> Mac Os: https://github.com/YangTaeyoung/inha_sugang_macro_v1/raw/master/Release/(Mac)%20InhaSugangTryBot%20V0.1%20Beta
