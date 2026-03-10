# while 조건:
#   실행 구문
# 파이썬은 break, continue 사용가능
# 단, return 사용은 함수에서만 가능
response = "아니"
# while response == "아니":
#     response = input("엄마, 다 됐어?")
    
# print("먹자")

# 파이썬에서 boolean은 반드시 True, False 로 첫 글자를 대문자로 입력해야함
while True:
    response = input("엄마, 다 됐어?")
    if response != "아니":
        print("먹자")
        break