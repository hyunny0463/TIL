# csv 파일 read의 두 가지 방법

#1. split

# with open('lunch.csv', 'r', encoding='utf-8') as f:
#     lines = f.readlines()
#     for line in lines:
#         # print(line.strip())
#         print(line.strip().split(','))  # , 를 기준으로 잘라서 리스트를 만들겠다.

#2. csv reader

import csv

with open('lunch.csv', 'r', encoding='utf-8') as f:
    lines = csv.reader(f)

    for line in lines:
        print(line)