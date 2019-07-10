#1-1. 파일 읽기(옛날 방식) - read()

# f = open('ssafy.txt.', 'r')
# all_text = f.read()
# print(all_text)
# f.close()

#1-2. 파일 읽기(최신 방식) - read()

# with open('with_ssafy.txt', 'r') as f:
#     print(f.read())

#2-1. 파일 읽기(옛날 방식) - readlines()

# f = open('ssafy.txt', 'r')
# lines = f.readlines()

# for line in lines:
#     print(line)

# f.close()

#2-2. 파일 읽기(최신 방식) - readlines()

# with open('with_ssafy.txt', 'r') as f:
#     lines = f.readlines()
#     for line in lines:
#         print(line.strip()) # .strip() 양 끝 개행문자를 생략시킴, print 함수 자체가 개행을 함