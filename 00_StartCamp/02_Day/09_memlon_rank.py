import requests
from bs4 import BeautifulSoup

headers = { # 브라우저가 헤더를 보내주는 경우도 있지만 직접 보내야 하는 경우도 있음
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}

response = requests.get('https://www.melon.com/chart/index.htm', headers = headers)
# 4로 시작한 오류는 클라이언트 오류 5로 시작하면 서버오류
response.encoding = 'utf-8'
res = response.text

soup = BeautifulSoup(res, 'html.parser')
songs = soup.select('.lst50')

# csv 파일로 옮기기

with open('melon.csv', 'w', encoding='utf-8') as f:
    for song in songs:
        rank = song.select_one('#lst50 > td:nth-child(2) > div > span.rank').text
        name = song.select_one('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').text
        artitst = song.select_one('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank02 > a').text
        f.write(f'{rank}위 : {name} / {artitst}\n')