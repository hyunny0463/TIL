# python code로 telegram message 보내기
from decouple import config
import requests # requests 모듈을 이용해서 parameter 내용 보내기

api_url = 'https://api.telegram.org'
token = config('TELEGRAM_BOT_TOKEN')
chat_id = config('CHAT_ID')
text = '크라운 빅파이와 크라운 국희 땅콩샌드'

send_message = requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')

print(send_message.text)