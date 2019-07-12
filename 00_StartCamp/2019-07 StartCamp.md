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
import requests

requests.get('https://naver.com').text			# 주소에 요청해서 정보 받아서 text만 얻어옴
requests.get('https://naver.com').status_code	# 요청을 잘 보내면 200을 받음
```



#### 3.2.5. Selector

```python
import bs4

text = bs4.BeautifulSoup(문서)	
text.select('selector')			# 문서 안에 있는 특정 내용을 뽑아줘(select)
text.select_one('selector')	# 문서 안에 있는 특정 내용을 하나만 뽑아줘(select_one)
```



#### 3.2.6. 코스피 지수 크롤링

```python
import requests
from bs4 import BeautifulSoup # bs4 module 에서 BeautifulSoup 함수를 가져옴

url = 'https://finance.naver.com/sise/'

html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
kospi = soup.select_one('#KOSPI_now').text
print(f'오늘의 코스피 지수는 {kospi}입니다.')
```

`ctrl + shift + c` 를 이용해서 selector를 쉽게 얻을 수 있음



#### 3.2.7. 원/환율 크롤링

```python
import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/marketindex/'

html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
exchange = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value')
print(f'현재의 원/달러 환율은 {exchange.text}입니다')
```



#### 3.2.8. 실시간 검색어 크롤링

```python
import requests
from bs4 import BeautifulSoup

url = 'https://www.naver.com/'
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
names = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li .ah_k')

for idx, name in enumerate(names):
    print(f'{idx+1}위: {name.text}')
```



#### 3.2.9. 정리

**API는 충분히 친절하다.**

우리가 hacking 할 수 있다면 얼마든지 가져다 쓸 수 있다. 하지만 모두 무료는 아니다.

Python Package 는 더 쉬운 방법이다.



**API vs Package**

프로그래밍 하라고 준 데이터 쓰기 vs 제 ㅡ발 쓰라고 주는 코드(함수) 덩어리



**Summary**

이 세상에는 수 많은 데이터들이 있고, 우리는 그 데이터를 가져다가 Hacking 할 수 있다. >_<

(zoomit)



### 3.3. 파일

#### 3.3.1. 파일 쓰기

#### 3.3.2. 파일 읽기



### 3.4. Package



## 4. 마크다운(typora) 사용법

### 4.1. Text

#### 4.1.1. Italic

*기울임체를 사용하기 위해 사용한다.*

특수문자 `*` 그리고 `_` 를 사용하거나, `ctrl + i` 단축키를 사용해도 된다.

```
*기울임체를 사용하려면 이렇게 하세요*
_기울임체를 사용하려면 이렇게 하세요_
```



#### 4.1.2. Bold

**글자를 굵은 글꼴로 바꿀 때 사용한다.**

특수문자 `**` 를 사용하거나, `ctrl + b` 단축키를 사용해도 된다.

```
**볼드체를 사용하려면 이렇게 하세요**
```



#### 4.1.3. Strikethrough

~~글자에 취소선을 넣을 때 사용한다.~~

특수문자 `~` 를 사용하거나, `alt + shift + 5` 단축키를 사용해도 된다.

```
~~취소선을 넣으려면 이렇게 하세요~~
```



### 4.2. Headers

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



### 4.3. Quotation

인용문을 사용할 때 사용한다.

각 행에서 맨 앞에 `>` 을 넣어 사용할 수 있다.



> *The gratification comes in the doing, not in the results." - James dean*
>
> *만족은 결과가 아니라 과정에서 찾아온다. - 제임스 딘*



### 4.4. Code

#### 4.4.1. Short source code

간단한 소스코드를 한 줄 입력할 때 사용한다.

소스코드에 `` ` `` 를 둘러싸서 사용한다. 단축키는 ``ctrl + shift +` ``

`print('Hello, SSAFY!')`



#### 4.4.2. Complete source code

긴 소스코드를 입력할 떄 사용한다.

소스코드를 ` ``` ` 입력하고 `enter`를 친 후 넣으면 된다. 단축키는 `ctrl + shift + K` 

```c++
#include <iostream>
using namespace std;

int main(int argc, char** argv)
{
    cout << "Hello, SSAFY!" << '\n';
    return 0;
}
```



### 4.5. Link

markdown 문서에 링크를 걸고 싶을 때 사용한다.

#### 4.5.1. 일반 링크

일반 링크는 하나의 링크를 연결할 때 사용한다.

`[링크 이름](실제 주소)` 의 규칙으로 작성하면 된다.

[hyunny0463님의 github](https://github.com/hyunny0463)



#### 4.5.2. 참조 링크

참조 링크는 하나의 링크를 여러번 참조하고 싶을 때 사용한다.

`[링크 이름][숫자]` 로 링크를 작성하고, 추가적으로 `[숫자]:{실제 주소}` 로 원하는 링크를 입력한다.

[hyunny0463님의 github][1]

[몰라유][1]

[1]:https://github.com/hyunny0463



### 4.6. Image

markdown 문서에 이미지를 넣을 때 사용한다.

`![그림 설명](이미지 링크)` 를 입력해서 사용할 수 있다.

이미지가 깨진다면 `repository > issue > new issue > 이미지 드래그&드롭 > [주소]` 를 활용한다.

![보노보노](https://user-images.githubusercontent.com/12672315/60955063-0e4f8080-a33b-11e9-94de-a91306b579d0.jpeg)



### 4.7. etc

`ctrl + shift + 1 ~ 3`		:	파일의 목차와 파일트리를 볼 수 있다.

`ctrl + /`								:	markdown 문서로 작성된 문서의 소스코드를 볼 수 있다.

`---` `___` `***`						:	아래와 같은 horizontal rule을 생성할 때 사용할 수 있다.	

***

___

---





## 5. Git

> 분산 버전 관리 프로그램으로 코드의 history를 관리하는 도구
>
> 프로젝트 이전 버전을 복원, 변경, 분석 및 병합까지 가능하다.



### 5.1. Git initialization

#### 5.1.1 Git에 내 정보 설정

* `$ git config --global user.name 'seohyun'`

* `$ git config -- global user.email 'hyunny0463@gmail.com'`
* `$ git config --global --list`
  * git에 설정된 유저 정보 보기



#### 5.1.2. 새로운 Git 파일 생성

- `$ git init`
  - git 초기화, 지금 위치한 폴더를 git으로 관리하겠다는 의미



#### 5.1.3. Git Clone

- `$ git clone https://github.com/hyunny0463/TIL.git` 
  - 주소로 부터 현재 폴더에 git repository를 내려받는다.
  - `git clone` 해 오면 git 폴더로 설정되어 추가적으로 `git init`, `git remote add` 할 필요가 없다.



### 5.2. Git command

#### 5.2.1. status

현재의 폴더에 있는 git 상태를 확인할 때 사용한다.

* `$ git status` 
  * 현재 폴더의 git 상태 확인
  * untracked(`{unstaged}`새로 생성된 파일), new file(`{staged}`새로 생성된 파일)
  * (빨강색)modified(`{unstaged}`수정된 파일), (초록색)modified(`{staged}`수정된 파일)

#### 5.2.2. add

* `$ git add [파일 이름]`
* 각각의 파일을 추가해주기 위해서는 `[파일 이름]`으로 추가해준다.
* `$ git add .`
  * 새로 만든 파일이거나 수정된 모든 파일을 `{unstaged}` 에서 `{staged}` 상태로 변경해준다.



#### 5.2.3. commit

* `$git commit`	커밋(create a snapshot) 만들기
* `push`	현재까지의 역사 (commits)가 기록되어 있는 곳에 새로 생성한 커밋들 반영하기



`$git commit -m` 	-로 시작하면 보통 short name 옵션

`$git config --global user.name "John"`	--로 시작하면 보통 long name 옵션





`$git add . `

`$git status`

`$git commit -m "first commit"`

`$git remote add origin [주소]`

`$git push origin master`



### 5.3. gitignore

github 사이트에서 gitignore를 정해둔게 있음, google에 python gitignore로 가지고 와도 됨



csv = comma seperated value



## HTML (Hyper Text Markup Language)

> 옛날에는 글을 선형적으로(순서대로) 읽었습니다.
>
> 여기서 하이퍼 텍스트라는 것은 링크로 넘나든다는 것입니다. 



## CSS (Cascade Style Sheet)

>
>
>HTML을 스타일링 해주는 친구



## BOOTSTRAP

>
>
>



## Flask

> $ pip install flask --user



> $ FLASK_APP=Hello.py flask run



어제

오전 : 가장 기본적으로 hello world 플라스크 설치하고 서버를 키고 특정 주소로 들어가니까 헬로 월드가 떴죠

랜덤 샘플을 가지고 음식중에 몇개만 선택했고 그 중에 variable routing 을 사용했다

필요하다면 templates에서 가져다 사용할 수 있게했다. render_templates를 이용해서 .html을 보여주는 것을 했고, render_templates를 이용해서 사용하고 싶은 변수를 인자를 넘겨줌 그래서 html에서도 사용가능 했죠

ascii artii 실습했죠 정해진 방식에 맞게 요청을 보내고 요청을 받아서 그 데이터를 이용함

그 때 사용한 것이 request와 respond.

그리고 dictionary 문제를 풀어봤음. dictionary에서 사용하는 method를 사용했음 .items(), keys(), values()

key를 가져올 때 [] 사용해서 가져오는 것과 .get을 이용해서 가져오는 2가지 방법을 사용했음

어제는 [] 만 썼지만 이제는 .get 으로 대부분 가져올 것이다. []는 중간에 데이터가 없다면 error가 나지만 .get으로 가져온다면 error가 나지 않는다 error가 난다는 것은 프로그램이 중간에 멈추는 것이다.



오늘은 telegram chatbot을 만들 것입니다. telegram은 kakaotalk보다 훨씬 보안이 우수합니다.

오늘 우리가 하는 내용에는 굉장히 다양하고 많은 내용이 담겨있습니다. 그걸 해보기에 telegram chatbot이 굉장히 좋습니다. 보여주기 좋습니다. 어제한 flask에서 html 보여주는 것만이 아니라 telegram chatbot 같은 것도 웹 서비스입니다.

앞으로는 우리가 token을 받게 될 것입니다. token은 하루에 정보를 요청할 수 있는 횟수일 수도 있습니다. 우리가 token을 받고 github 사이트에 올리면 다른 사람들이 볼 수 있게 되겠죠? 이런 것도 문제가 발생할 수 있는데 해커들이 이런 소스를 긁어올 수 있는데 우리가 사용하지 않아도 이런 해커들 때문에 계속 요금이 발생할 수 있습니다. 이것을 예방하기 위해서 .gitignore에 글자를 적어넣어 이런 token을 github에 올리지 않도록 합니다.

오늘은 지금까지 한 것과는 차원이 다른 외계어 같은 것을 하게 됩니다. 하지만 뒤에 돌아와서는 이해가 될 지도 모르겠습니다.

token의 보안이 중요하니깐 .env 파일에 token을 적어 놓는다 이 파일을 git이 관리하지 않는다.



웹훅?

