# a = [1,2,3,4,5] => 리스트, 일종의 배열과 같은 의미

# i = 1, i = 2, i = 3, i = 4, i = 5 이렇게 5번 반복
for i in [1,2,3,4,5]:
    print("반복문")

# for 변수 in range(종료값) => 변수가 0부터 시작해서 종료값 - 1 까지 반복
for i in range(5):
    print(f"{i} = range-1까지 반복")

# for 변수 in range(초기값, 종료값, 증감값)
# 1 ~ 5까지 반복하여 숫자 출력
# range(1,6,1) => 종료값은 무조건 -1까지 반복함
for i in range(1,6,1):
    print(f"{i} = range")