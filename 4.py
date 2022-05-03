# \n : 줄바꿈
print("백문이 불여일견\n백견이 불여일타")

# 문자열에 따옴표 넣기
print("저는 \"이철진\" 입니다.")
print('저는 "이철진" 입니다.')
print("저는 \'이철진\'입니다.")

# \\ : 문장 내에서 \ (하나로 인식)
print("C:\\Users\snc\\Desktop\\PytonWorkspace")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")

#  \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")

# \t : 탭
print("Red\tApple")

print("==================================")

url = "http://daum.net"
# 규칙 1
my_str = url.replace("http://", "") # http:// 을 빈칸으로 바꾸기
print(my_str)
# 규칙 2
my_str = my_str[:my_str.index(".")] # my_str문자열에서 처음 나오는 .직전까지 (my_str[0:5])
print(my_str)
# 규칙 3
pw = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0} 의 비밀번호는 {1} 입니다.".format(url, pw))



