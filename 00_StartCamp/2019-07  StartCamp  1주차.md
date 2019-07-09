# 2019-07 | StartCamp | 1주차

## 1. 4차산업혁명과 소프트웨어

## 2. 파이썬 프로그래밍의 개념과 문법

1. 프로그래밍 개념

2. 프로그래밍 문법

   - 저장
    무엇을 저장하는가? 숫자, 글자, 참 거짓
     어디에?	변수
     어떻게?	리스트 << 순서가 존재한다.
     				 딕셔너리 << 키와 밸류가 존재한다. 키를 이용하여 밸류를 꺼낸다.

     

   - 조건
   
   - 반복

## 3. 파이썬 프로그래밍 심화

### 3.1. API(Application Programming Interface)

서로 다른 서비스가 데이터를 주고받을 때 사용한다.

*ex) 다른 사이트에서 네이버, 페이스북 계정으로 로그인, 미세먼지 데이터를 받아올 때 사용*



### 3.2. Crawling(크롤링)

웹 브라우저에서 원하는 데이터를 받아 오는 것을 크롤링이라고 한다.

크롤링을 하더라도 모든 정보를 받아올 수 있는 것이 아니고 원하는 정보만 얻어 오는 것이 아니므로,

받아온 데이터를 정제하는 과정이 필요하다.



#### 3.2.1. 웹브라우저 열기

```python
import webbrowser				# 크롬에서는 모두 새 창이 열리는 동작을 함

webbrowser.open('주소')			# 웹 브라우저를 열어줘
webbrowser.open_new('주소')		# 웹 브라우저를 새 윈도우에서 열어줘
webbrowser.open_new_tab('주소')	# 웹 브라우저를 새 탭에서 열어줘
```



#### 3.2.2. List의 내용 검색창에 띄우기

```python
import webbrowser

idol = ['bts', 'ioi', 'mamamoo', 'IU', 'winner', 'red velvet']
for i in idol:
    webbrowser.open('https://search.naver.com/search.naver?query=' + i)
```



#### 3.2.3. 크롤링에 필요한 모듈 설치

>$ pip install requests --user
>$ pip list
>$ pip install bs4 --user



#### 3.2.4. 정보 스크랩

```python
# 정보 스크랩
import requests

requests.get('https://naver.com').text			# 주소에 요청해서 정보 받아서 text만 얻어옴
requests.get('https://naver.com').status_code	# 요청을 잘 보내면 200을 받음
```



#### 3.2.5. 

```python
import bs4

text = bs4.BeautifulSoup(문서)	
text.select('selector')			# 문서 안에 있는 특정 내용을 뽑아줘(select)
text.select_one('selector')	# 문서 안에 있는 특정 내용을 하나만 뽑아줘(select_one)

```



### 3.3. Package



## 4. 마크다운(typora) 사용법

### 1.1. Text

#### 1.1.1. Italic

*기울임체를 사용하기 위해 사용한다.*

특수문자 `*` 그리고 `_` 를 사용하거나, `ctrl + i` 단축키를 사용해도 된다.

```
*기울임체를 사용하려면 이렇게 하세요*
_기울임체를 사용하려면 이렇게 하세요_
```



#### 1.1.2. Bold

**글자를 굵은 글꼴로 바꿀 때 사용한다.**

특수문자 `**` 를 사용하거나, `ctrl + b` 단축키를 사용해도 된다.

```
**볼드체를 사용하려면 이렇게 하세요**
```



#### 1.1.3. Strikethrough

~~글자에 취소선을 넣을 때 사용한다.~~

특수문자 `~` 를 사용하거나, `alt + shift + 5` 단축키를 사용해도 된다.

```
~~취소선을 넣으려면 이렇게 하세요~~
```



### 1.2. Headers

문서 제목을 표현할 때 사용한다.

각 행에서 맨 앞에 `#` 을 넣어 사용할 수 있다.

```
# This is a H1			# Ctrl + 1
## This is a H2			# Ctrl + 2
### This is a H3		# Ctrl + 3
#### This is a H4		# Ctrl + 4
##### This is a H5		# Ctrl + 5
###### This is a H6		# Ctrl + 6
```



### 1.3. Quotation

인용문을 사용할 때 사용한다.

각 행에서 맨 앞에 `>` 을 넣어 사용할 수 있다.



> *The gratification comes in the doing, not in the results." - James dean*
>
> *만족은 결과가 아니라 과정에서 찾아온다. - 제임스 딘*



### 1.4. Code

#### 1.4.1. Short source code

간단한 소스코드를 한 줄 입력할 때 사용한다.

소스코드에 ` `` ` 를 둘러싸서 사용한다.

`print('Hello, SSAFY!')`



#### 1.4.2. Complete source code

긴 소스코드를 입력할 떄 사용한다.

소스코드를 ` ``` ` 입력하고 `enter`를 친 후 넣으면 된다.

```c++
#include <iostream>
using namespace std;

int main(int argc, char** argv)
{
    cout << "Hello, SSAFY!" << '\n';
    return 0;
}
```



### 1.5. Link

markdown 문서에 링크를 걸고 싶을 때 사용한다.

#### 1.5.1. 일반 링크

일반 링크는 하나의 링크를 연결할 때 사용한다.

`[링크 이름](실제 주소)` 의 규칙으로 작성하면 된다.

[hyunny0463님의 github](https://github.com/hyunny0463)



#### 1.5.2. 참조 링크

참조 링크는 하나의 링크를 여러번 참조하고 싶을 때 사용한다.

`[링크 이름][숫자]` 로 링크를 작성하고, 추가적으로 `[숫자]:{실제 주소}` 로 원하는 링크를 입력한다.

[hyunny0463님의 github][1]

[몰라유][1]

[1]:https://github.com/hyunny0463



### 1.6. Image

markdown 문서에 이미지를 넣을 때 사용한다.

`![그림 설명](이미지 링크)` 를 입력해서 사용할 수 있다.

![보노보노](https://w.namu.la/s/fbe29c52a03345a112f33d89632e39735b30e9cd3d85346db314841d27e13f5148542ea262ae9fcd04c1a5c86c1a07586e381983ef8c4ce600ea9378fe4066a25cc2e64018bafc2c25079d9da6f45d9e40df135269a0c1d669fcb7079620552f)



### 1.7. etc

`ctrl + /`	:	markdown 문서로 작성된 문서의 소스코드를 볼 수 있다.

### 9일

Python IDE ( Integrated Development Enviroment) : 파이썬 통합 개발 환경

Python IDLE : python으로 내 컴퓨터를 조작하는 툴



#### 크롤링

```python
# 현재의 코스피 지수 받아오기
import requests
from bs4 import BeautifulSoup # bs4 module 에서 BeautifulSoup 함수를 가져옴

url = 'https://finance.naver.com/sise/'

html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
kospi = soup.select_one('#KOSPI_now').text
print(f'오늘의 코스피 지수는 {kospi}입니다.')
```

`ctrl + shift + c` 를 이용해서 selector를 쉽게 얻을 수 있음



```python
# 현재의 원/환율 받아오기
import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/marketindex/'

html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
exchange = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value')
print(f'현재의 원/달러 환율은 {exchange.text}입니다')
```



```python
# 실시간 검색어 받아오기
import requests
from bs4 import BeautifulSoup

url = 'https://www.naver.com/'
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
names = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li .ah_k')

for idx, name in enumerate(names):
    print(f'{idx+1}위: {name.text}')
```





**API는 충분히 친절하다.**

- 우리가 hacking 할 수 있다면 얼마든지 가져다 쓸 수 있다.(무료라고는 안함)

**하지만 더 쉬운 방법이 있는데. 그것은 파이썬 패키지**



**API vs Package**

프로그래밍 하라고 준 데이터 쓰기 vs 제 ㅡ발 쓰라고 주는 코드(함수) 덩어리



**Summary**

이 세상에는 수 많은 데이터들이 있고, 우리는 그 데이터를 가져다가 Hacking 할 수 있다. >_<

(zoomit)



## GIT

분산 버전 관리 프로그램으로 코드의 history를 관리하는 도구

프로젝트 이전 버전을 복원, 변경, 분석 및 병합까지 가능하다.



`add`	커밋할 목록에 추가

`commit`	커밋(create a snapshot) 만들기

`push`	현재까지의 역사 (commits)가 기록되어 있는 곳에 새로 생성한 커밋들 반영하기



`$git add helloworld.py`

`$git commit -m` 	-로 시작하면 보통 short name 옵션

`$git config --global user.name "John"`	--로 시작하면 보통 long name 옵션



### git initialization

`$git config --global user.name 'seohyun'`

`$git config -- global user.email 'hyunny0463@gmail.com'`

`$git config --global --list`

`$git add . `

`$git status`

`$git commit -m "first commit"`

`$git remote add origin`

`$git push origin master`

`$git clone [주소]`



### gitignore





