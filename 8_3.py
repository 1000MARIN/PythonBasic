# 파일 입출력

# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# 존재하는 파일에 계속 쓰기
# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# 파일 출력 (모두 출력)
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="")    # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="")    # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="")    # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="")    # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# score_file.close()

# 파일이 총 몇줄인지 모를때, 반복문으로 파일 내용 출력
# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline() 
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

# list를 이용하여 파일 내용 출력
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()  # list 형태로 저장
for line in lines:
    print(line, end="")
    score_file.close()