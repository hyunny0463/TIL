lunch = {
    '양자강' : '02-557-4211',
    '김밥카페' : '02-553-3181',
    '순남시레기' : '02-508-0887'
}

#1. 방법 1.

with open('lunch.csv', 'w', encoding='utf-8') as f:
    for item in lunch.items():          # .items() tuple로 생성됨
        f.write(f'{item[0]}, {item[1]}\n')