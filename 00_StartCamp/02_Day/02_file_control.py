# 파일 앞에 동일한 문자열 넣기
# import os

# os.chdir(r'C:\Users\student\TIL\00_StartCamp\02_Day\dummy')

# for filename in os.listdir('.'):
#     os.rename(filename, f'SAMSUNG_{filename}')

# 파일에 SAMSUNG을 빼고 SSAFY를 대신 넣기
import os

os.chdir(r'C:\Users\student\TIL\00_StartCamp\02_Day\dummy')

for filename in os.listdir('.'):
    os.rename(filename, filename.replace('SAMSUNG', 'SSAFY'))