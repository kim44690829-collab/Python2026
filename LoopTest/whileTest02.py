# 문제
# 1 ~ 50까지의 합 => while
# num = 1
# result = 0
# while num <= 50:
#     result += num
#     num += 1
# print(result)

# 다중 while문 => 구구단 2단 ~ 9단
num2 = 2
num3 = 1
while num2 <= 9:
    while num3 <= 9:
        print(f"{num2} X {num3} = {num2 * num3}")
        num3 += 1
    print()
    num2 += 1
    num3 = 1
    