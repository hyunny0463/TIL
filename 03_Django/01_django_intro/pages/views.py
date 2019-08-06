from django.shortcuts import render
from datetime import datetime
import random
import requests

# 1. 기본 로직
def index(request):
    return render(request, 'index.html')

def introduce(request):
    return render(request, 'introduce.html')

def image(request):
    return render(request, 'image.html')

# 2. Template Variable(템플릿 변수)
def dinner(request):
    menu = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menu)
    context = {'pick': pick}
    return render(request, 'dinner.html', context)

# 3. Variable Routing(동적 라우팅)
def hello(request, name, age):
    menu = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menu)
    context = {
        'name': name,
        'age': age,
        'pick': pick
    }
    return render(request, 'hello.html', context)

# 4. 실습
# 4-1. 동적 라우팅을 활용해서(name과 age를 인자로 받아) 자기소개 페이지
def master(request, name, age):
    context = {
        'name': name,
        'age': age
    }
    return render(request, 'master.html', context)

# 4-2. 두 개의 숫자를 인자로 받아(num1, num2) 곱셈 결과를 출력
def mul(request, num1, num2):
    result = num1 * num2
    context = {
        'num1': num1,
        'num2': num2,
        'result': result
    }
    return render(request, 'mul.html', context)

# 4-3. 반지름을 인자로 받아 원의 넓이를 구하시오.
def circle_area(request, rad):
    context = {
        'rad': rad,
        'area': 3.14 * rad ** 2
    }
    return render(request, 'circle_area.html', context)

# 5. DTL(Django Template Language)
def template_language(request):
    menus = ['짜장면', '탕수육', '짬뽕', '양장피']
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'mango']
    datetimenow = datetime.now()
    empty_list = []

    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'empty_list': empty_list,
        'datetimenow': datetimenow,
    }
    return render(request, 'template_language.html', context)

# 6. 실습
# 6-1. isbirth

def isbirth(request):
    today = datetime.now()
    context = {
        'mon': today.month,
        'day': today.day,
    }
    return render(request, 'isbirth.html', context)

# 6-2. 회문판별(palindrome)
def ispal(request, words):
    context = dict()
    context['bool'] = 'True' if words == words[::-1] else 'False'
    return render(request, 'ispal.html', context)

# 6-3. 로또 번호 추첨
# lottos -> 1 ~ 45까지의 번호 중 6개를 랜덤으로 pick한 리스트
# real_lottos -> [21, 24, 30, 32, 40, 42]
# 1. lottos 번호를 하나씩 출력(DTL-for문)
# 2. 컴시기가 뽑은 로또 번호와 실제 로또 당첨 번호를 비교해보기(DTL-if문)
def lotto(request):
    lottos = sorted(random.sample(range(1, 46), 6))
    context = {
        'real_lottos': [21, 24, 30, 32, 40, 42],
        'lottos': lottos,
    }
    return render(request, 'lotto.html', context)

# 7. Form - GET
def throw(request):
    return render(request, 'throw.html')

def catch(request):
    message = request.GET.get('message')
    message2 = request.GET.get('message2')
    context = {
        'message': message,
        'message2': message2,
    }
    return render(request, 'catch.html', context)

def ping(request):
    return render(request, 'ping.html')


def pong(request):
    pong1 = request.GET.get('pong1')
    pong2 = request.GET.get('pong2')
    context = {
        'pong1': pong1,
        'pong2': pong2,
    }
    return render(request, 'pong.html', context)

# 8. From - GET 실습(아스키 아티)
def art(request):
    return render(request, 'art.html')

def result(request):
    #1. form으로 날린 데이터를 받는다.(GET)
    word = request.GET.get('word')

    #2. ARTII api로 요청을 보내 응답 결과를 fonts에 저장
    fonts = requests.get('http://artii.herokuapp.com/fonts_list').text

    #3. fonts(str)를 fonts(list)로 바꾼다.
    fonts = fonts.split('\n')

    #4. fonts(list)안에 들어있는 요소 중 하나를 선택해서
    #   font라는 변수에 저장(str)
    font = random.choice(fonts)

    #5. 위에서 사용자에게 받은 word와 font를 가지고 다시
    #   요청을 보낸다. 그리고 응답 결과를 result에 저장한다.
    result = requests.get(f'http://artii.herokuapp.com/make?text={word}&font={font}').text
    
    context = {
        'result': result,
    }
    return render(request, 'result.html', context)

# 9. From - POST
def user_new(request):
    return render(request, 'user_new.html')

def user_create(request):
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    context = {
        'name': name,
        'password': pwd,
    }
    return render(request, 'user_create.html', context)