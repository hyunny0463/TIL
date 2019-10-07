# Django

## 1. Intro

### 1.1. Django의 특징

|     특징     |    의미    |
| :------: | :----------: |
|  Versatile   | 다양성 있음 |
|    Secure    | 안정성 있음 |
|   Scalable   | 확장성 있음 |
|   Complete   | 완결성 있음 |
| Maintainable | 유지가 잘됨 |
|   Portable   | 연결이 잘됨 |



### 1.2. Django의 성격

|      성격      |                             의미                             |
| :------------: | :----------------------------------------------------------: |
|  Opinionated   | 독선적 (일을 쉽게 수행할 수 있도록 설계되어 있어 편리하고 쉽게 개발 할 수 있다) |
| Un-opinionated | 관용적 (많은 유연성을 제공해서 문제를 해결하는 방법을 다양하게 할 수 있다) |



Django는 MTV pattern을 띈다.

Model  데이터를 관리

Template 사용자가 보는 화면

View 중간 관리자

![Django request-response cycle](https://user-images.githubusercontent.com/12672315/62436519-e2c58780-b77a-11e9-8221-9d29ab0714ed.png)



### 1.3. Django 기본 설정

가상환경 설정: `python -m venv venv`, `source venv/Scripts/activate`

가상환경 내부에 Django 설치: `pip install django`

가상환경 종료: `deactivate`



vs-code 켤 때 자동으로 가상환경 설정되게 하는 법

1. 작업할 폴더에서 vscode를 켠다.

2. `F1` 또는 `ctrl + shift + P`를 눌러서 `select interpreter` 를 적는다.

3. `'venv': venv` 가 있는 설정을 선택한다.

   



`django-admin startproject django_intro .`  현재 폴더에 `django_intro`라는 프로젝트를 만듦

`python manage.py runserver` 서버를 실행함

`python manage.py startapp pages` pages라는 app을 실행시킨다.

app 등록 시 project의 `setting.py` --> `INSTALLED_APPS`에 등록을 한다

`settings.py` --->`LANGUAGE = 'ko-kr'`, `TIME_ZONE = 'Asia/Seoul'`

app 폴더 내에 templates 폴더를 만들고 모든 `.html` 파일을 넣어둔다.







---

정적 파일

`.html` 파일 가장 위에 `{% load static %}` 추가함

`pages` 폴더 안에 `static` 폴더를 생성

`static` 폴더 안에 `images`, `stylesheets` 폴더를 생성

```html
<!-- 정적 파일 불러올 때 -->
<link rel="stylesheet" href="{% static 'stylesheets/style.css' %}">
<img src="{% static 'images/bart.png' %}" alt="">
```



---

url 분리

이유: 같은 이름의 `.html` 파일이 `templates`폴더 안에 있으면 `INSTALLED_APP`에 등록된 순서대로 파일을 띄워주기 때문에 각각의 namespace 를 구분해 주어야 한다.

똑같은 index.html 파일이 pages app 에도 있고, utilities app에도 있다면 installed_app에서 상위에 위치한 utilities app의 templates에 있는 index.html을 보여주는 현상이 있는데 이를 막으려면 app과 동일한 폴더를 templates 폴더 하위에 만들어서 모든 html을 넣는다.

하지만 templates 폴더 바로 하위에 있지 않기 때문에 기존의 소스코드는 오류가 난다.

그러므로 views.py에 `return render(request, 'index.html')`에서 `return render(request, 'utilities/index.html')` 로 변경해준다.



수 많은 소스코드에서 직접경로로 설정한 주소들을 바꾸기 위해 직접 하나하나 바꿔야 하는 어려움이 있다.

이 문제를 해결하기 위한 방법 ( 경로에 대한 의존성을 없애기 위한 방법 )

```python
# urls.py
app_name = 'articles'
urlpatterns = [ path('', views.index, name='index') ]
```

```html
<!-- detail.html -->
<a href "{% url 'index' %}">[메인 페이지]</a>
<a href "{% url 'delete' article.pk %}">[글 삭제]</a>
```

```python
# views.py
return redirect('articles:index')
return redirect('articles:detail', article.pk)
```



---

Template Inheritance(템플릿 상속, 확장)

템플릿을 상속하기 위한 테스트

프로젝트 폴더내에 templates 폴더를 만들고 base.html이라는 파일을 만들었다.

base.html 파일에는 html의 기본 폼에 bootstrap을 추가해주었다.

settings.py파일에 TEMPLATES 라는 리스트에

`'DIRS': [os.path.join(BASE_DIR, 'django_intro', 'templates'),],` 를 넣어주었다.

APP_DIRS: True는 templates 폴더에서 알아서 .html 파일을 찾아준다는 의미



템플릿 상속할 html  파일에서

최상단에 `{% extends 'base.html' %}` 를 넣고

템플릿을 적용할 파일들을 block으로 가둬준다.

```html
{% extends 'base.html' %}

{% block body %}
	<h1>당신이 궁금해 한 원의 넓이는?</h1>
	<h2>원의 넓이: {{ area }}, 반지름 길이: {{ rad }}</h2>
{% endblock %}
```

---



데이터 베이스

구성요소: 개체(entity), 속성(attribute), 관계(relation)

RDBMS(relation database management system)

SQLite: 서버가 아닌 응용 프로그램에 넣어 사용하는 비교적 가벼운 데이터베이스이다.



기본용어

스키마(scheme) 데이터베이스에서 자료의 구조, 표현방법, 관계등을 정의한 구조

열(column) 각 열에는 고유한 데이터 형식이 지정된다. (integer, text, null 등) 하지만 비면 안된다.

행(row:레코드) 

SQL: 관계형 데이터베이스 관리시스템의 데이터를 관리하기 위해 설계된 특수 목적의 프로그래밍 언어

테이블에 데이터 삽입(INSERT) 데이터 삭제(행삭제) (DELETE) 데이터 갱신(UPDATE) 데이터 검색(SELECT)

ex) SELECT * FROM table

```sqlite
SELECT * FROM table
```



| SQL         | CRUD   |
| ----------- | ------ |
| SELECT      | READ   |
| INSERT INTO | CREATE |
| UPDATE      | UPDATE |
| DELETE      | DELETE |



ORM(Object-Relational Mapping)

객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템간에 데이터를 변환하는 프로그래밍 기술

![](https://miro.medium.com/max/1400/0*UkOqM_a_agYwUOoV)



SQL 문법을 몰라도 쿼리(데이터베이스에 정보 요청)를 조작할 수 있다.

즉, Python의 Class로 DB를 조작할 수 있다.



```python
# models.py 테이블 정의
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=10) # 제목의 최대길이 설정 (필수 인자)
    content = models.TextField() # 내용의 길이 설정 (필수인자 없음)
    created_at = models.DateTimeField(auto_now_add=True) # 최초로 글을 쓸 때 자동 저장
    updated_at = models.DateTimeField(auto_now=True) # 업데이트마다 시간 저장
```



설계도를 자동으로 만들기

```
$ python manage.py makemigrations
```

아직은 데이터베이스에 반영되지는 않았음 



migrate commit 메시지 보기

```
$ python manage.py sqlmigrate articles 0001
```



migrate 상태보기(데이터베이스에 반영되었다면 앞에 [X] 표시가 뜸)

``````
$ python manage.py showmigrations
``````



데이터베이스에 반영하기

```
$ python manage.py migrate
```



sqlite 문서를 볼 수 없으니깐 보조 프로그램 설치 > sqlite3

```
F1 > SQLite: Open Database > EXPLORER에 SQLITE EXPLORER
```



django shell 접속

```
$ python manage.py shell
```



test - db에 저장된 것 보기

```python
from articles.models import Article

Article.objects.all()
```



test - db 테이블에 세팅 첫 번째 방법

```python
article = Article()
article.title = 'first'
article.content = 'django'
article.save() # DB에 저장
```



test - db 테이블에 세팅 두 번째 방법

```python
article = Article(title='second', content='django!')
article.save()
```



test - db 테이블에 세팅 세 번째 방법

```python
Article.objects.create(title='third', content='django!') # 바로 저장함
```



삭제방법

```python
article.delete()
```



db 확인하기

```python
Article.objects.all()
```



공백체크 및 규격체크

```python
article.full_clean()
```

```
django.core.exceptions.ValidationError: {'title': ['이 값이 최대 10 개의 글자인지 확인하세요(입력값 48 자).'], 'content': ['이 필드는 빈 칸으로 둘 수 없습니다.']}
```



필터 사용 - title이 'first'인 행이 2개 들어있음

```python
Article.objects.filter(title='first') # title이 first인 2개가 선택됨
Article.objects.filter(title='first').first() # 첫 번째 것만 선택됨
Article.objects.filter(title='first').last() # 마지막 것만 선택됨 first, last만 가능
```

```python
Article.objects.filter(pk=1) # QuerySet으로 반환해서 id, content 등 조회 불가능
```





get 사용 - 고유한 정보에만 사용한다.

```python
Article.objects.get(pk=1) # primary key가 1인 것을 가져옴
```

* 존재하지 않는 인덱스를 접근하거나 하나만 가져오는 get함수에서 여러개 가져오는 행위를 할 때 오류가 생기는데 filter는 빈 QuerySet을 반환하고 get은 오류를 발생시킴



order_by

```python
Article.objects.order_by('-id') # 내림차순으로 정렬된 QuerySet을 반환함
```



인덱싱

```python
Article.objects.all()[2] # 3번글을 Article 클래스로 반환한다.
```



인덱스 슬라이싱

```python
Article.objects.all()[1:3] # 2번과 3번글을 QuerySet 형태로 반환한다.
```



QuerySet으로 반환

```python
Article.objects.filter(title__contains='fir') # title에 'fir'이 포함되어 있으면 반환
```

```python
Article.objects.filter(title__startswith='first') # title이 'fitst'로 시작하면 반환
```



```python
Article.objects.filter(content__endswith='!') # content 마지막에 '!'이 있으면 반환
```



관리자 계정 생성: `python manage.py createsuperuser`

```python
# admin.py
from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at', 'updated_at')

admin.site.register(Article, ArticleAdmin)
```



`$ pip install django-extensions ipython`

```python
# settings.py
INSTALLED_APP = [
    'django_extension',
]
```

`$ python manage.py shell_plus`

--> import Article 하지 않아도 알아서 잡아줌



CRUD

Create -> Read -> Delete -> Update

render의 목적: 계층 구조를 만든다. html 파일을 사용자에게 보여줘야 할 때

리-다이렉트: html 파일을 보여주더라도 해당 주소로 요청을 보내주어도 될 때

```python
# views.py
from django.shortcuts import render, redirect
def create(request):
    return redirect('/articles/')
```



### 1.4. REST API

#### 1.4.0. REST 구성



1.4.0. REST 특징

| 구분                                    |                             비고                             |
| --------------------------------------- | :----------------------------------------------------------: |
| Uniform                                 | Uniform Interface<br/>지정한 리소스에 대한 조작을 통일되고 한정적인 인터페이스로 활용 |
| Stateless(무상태성)                     | 무상태성 성격을 가지고 있으며, 세션 정보나 쿠키 정보를 별도로 저장하지 않고 관리하여 단순하게 요청만을 처리 |
| Cacheable(캐시가능)                     |                HTTP의 캐시 기능이 적용 가능함                |
| Self-descriptiveness<br> (자체표현구조) |   REST API 메시지만 보고 상태와 행위를 쉽게 이해할 수 있음   |
| Client - Server 구조                    |  클라이언트 서버에서 개발할 내용이 명확하고 의존성이 줄어듬  |
| 계층형 구조                             |           REST 서버는 다중 계층으로 구성될 수 있음           |



#### 1.4.0. REST 중심 규칙

URI는 정보의 자원을 표현해야 한다.

ex) `GET /users/1/read/` 는 불필요한 행위인 `read`가 포함되어 있음 자원을 표현하는데만 중점을 둬야함

ex) `GET /users/1/create/` 에는 GET 메소드가 적절하지 않음

자원에 대한 행위는 HTTP Method 로 표현한다.



#### 1.4.1. HTTP 기본속성

|             |                             비고                             |
| :---------: | :----------------------------------------------------------: |
|  Stateless  | 상태정보가 저장되지 않음. 즉, 요청 사이에는 연결고리가 없음.<br>클라이언트가 서버와 상호작용하기 위해서 HTTP 쿠키를 만들고,<br>상태가 있는 세션을 활용할 수 있도록 보완 |
| Connectless |      서버에 요청을 하고 응답을 한 이후에 연결은 끊어짐.      |



1.4.2. URL(Uniform Resource Locator)

행위를 의미함

1.4.3. URI(Uniform Resource Identifier)

자원을 의미함



1.4.4. HTTP 요청 메시지



1.4.5. HTTP 응답 메시지



### 1.5. RESTful(Representational State Transfer)