# 문제)
# 연도가 4로 나누어 떨어지면 윤년
# 연도가 100으로 나누어 떨어지는 년도는 제외

year = int(input("연도를 입력해주세요 : "))

if ((year % 4 == 0) and not(year % 100 == 0)) or year % 400 == 0:
    print("윤년입니다.")
else:
    print("윤년이 아닙니다.")