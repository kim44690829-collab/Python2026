# while True:
#     id = input("아이디 입력 (4 ~ 12자) : ")
#     if 4 > len(id) or len(id) > 12:
#         print("아이디는4자 이상12자 이하여야 합니다. 다시 입력하세요. ")
#         continue
#     else:
#         while True:
#             pw = input("비밀번호 입력(8자 이상, 숫자 포함) : ")
#             if len(pw) < 8:
#                 print("비밀번호는8자 이상이어야 합니다. 다시 입력하세요.")
#                 continue
#             else:
#                 while True:
#                     email = input("이메일 입력 : ")
#                     if email in ('@'):
#                         print("유효성 검사 통과! API 요청을 전송합니다.")
#                         break
#                     else:
#                         print("올바른 이메일 형식이 아닙니다. 다시 입력하세요.")
#                         continue

# id 검사 4 이상 12 이하 len() 사용
while True:
    userid = input("아이디 입력 (4 ~ 12자) : ")
    # len(userid) >= 4 and len(userid) <= 12
    if len(userid) >= 4 and len(userid) <= 12:
        # 조건을 만족하면 반복문 종료
        break
    print("아이디는4자 이상12자 이하여야 합니다. 다시 입력하세요.")

#비밀번호 검사 =>
while True:
    pw = input("비밀번호 입력(8자 이상, 숫자 포함) : ")
    # 8자보다 작으면 다시 입력
    if len(pw) < 8:
        print("비밀번호는8자 이상이어야 합니다. 다시 입력하세요.")
        continue
    # 숫자 포함되어 있는지 존재 유무 확인을 위한 boolean 
    digit = False
    # in 사용 => if @ in 변수 => @가 변수 안에 포함되어있냐
    #            for i in pw => i값이 변수까지 반복해서 pw안에 포함되어있냐
    for ch in pw:
        # 문자가 '0'이상이고 '9'이하이면 숫자
        if ch >= '0' and ch <= '9':
            digit = True # 숫자가 포함되어있으면 true
            break # 숫자를 찾았으니까 반복 종료
    # 숫자가 하나도 없으면 다시 입력
    if not digit:
        print("비밀번호는 숫자가 포함되어야 합니다.")
        continue
    # 모든 조건을 만족하면 반복문 종료
    break

while True:
    email = input("이메일 입력 : ")
    if "@" in email:
        break
    print("올바른 이메일 형식이 아닙니다. 다시 입력하세요.")

print("유효성 검사 통과! API 요청을 전송합니다.")