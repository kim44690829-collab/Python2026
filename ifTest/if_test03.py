# 다중 if
# if 조건식 :
#    print("출력문")
# elif 조건식 :
#    print("출력문")
# else :
#    print("출력문")

# 정수를 입력받아서 0이면 0이다, 0보다 크면 양수이다. 아니면 음수이다.

num = int(input("정수를 입력해주세요 : "))

if num == 0:
    print("0입니다.")
elif num > 0:
    print("양수입니다.")
else :
    print("음수입니다.")