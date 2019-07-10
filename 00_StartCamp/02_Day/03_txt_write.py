#1. 파일 쓰기(옛날 방식)

# f = open('ssafy.txt', 'w') # ssafy.txt 파일을 만들겠다(쓰기 모드).
# for i in range(10):
#     f.write(f'This is line {i}. \n')

# f.close() # 파일을 열었으면 필수로 닫아줘야 한다.

#2-1. 파일 쓰기(최신 방식)

# with open('with_ssafy.txt', 'w') as f:
#     for i in range(10):
#         f.write(f'This is line {i}.\n')

# close() 필요없음

#2-2. 파일 쓰기(최신 방식)

with open('writelines_ssafy.txt', 'w') as f:
    f.writelines(['0\n', '1\n', '2\n', '3\n'])