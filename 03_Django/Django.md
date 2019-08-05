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
2.  `F1` 또는 `ctrl + shift + P`를 눌러서 `select interpreter` 를 적는다.
3. `'venv': venv` 가 있는 설정을 선택한다.



`django-admin startproject django_intro .`  현재 폴더에 `django_intro`라는 프로젝트를 만듦

`python manage.py runserver` 서버를 실행함

`python manage.py startapp pages` pages라는 app을 실행시킨다.

app 등록 시 project의 `setting.py` --> `INSTALLED_APPS`에 등록을 한다

`settings.py` --->`LANGUAGE = 'ko-kr'`, `TIME_ZONE = 'Asia/Seoul'`

app 폴더 내에 templates 폴더를 만들고 모든 `.html` 파일을 넣어둔다.



