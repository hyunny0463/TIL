#1. 각각의 라인을 list의 요소로 불러오기
with open('writelines_ssafy.txt', 'r') as f:
    lines = f.readlines()

#2. 뒤집기
lines.reverse()

#3. line을 작성하기
with open('reverse_ssafy.txt', 'w') as f:
    for line in lines:
        f.write(line)


# with open('writelines_ssafy.txt', 'r+') as f:
#     lines = f.readlines()
#     lines.reverse()
#     f.seek(0)
#     f.writelines(lines)

# method와 function의 차이는 원본을 바꾸느냐 아니냐 바뀐 복제본을 리턴하느냐 아니냐 차이
# 리턴없음  리턴있음