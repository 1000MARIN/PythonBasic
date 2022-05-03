# 표준 입출력
# print("Python", "Java", sep=", " , end="? ")
# print("무엇이 더 재밌을까요?")

# import sys
# print("Python", "Java", file=sys. stdout)
# print("Python", "Java", file=sys.stderr)

# 시험 성적
# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":")   # 과목(왼쪽정렬) 점수(오른쪽 정렬)

# 은행 대기순번표
# 001, 002, 003, ...
# for num in range(1, 201):
#     print("대기번호 : " + str(num).zfill(3)) # zfill(3) : 3자리 확보

answer = input("아무 값이나 입력하세요 : ")
print(type(answer)) # 사용자 입력으로 값을 받게 되면 항상 문자열 형태로 저장
print("입력하신 값은 " + answer + "입니다.")

