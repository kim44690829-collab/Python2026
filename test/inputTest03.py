name = input("이름을 입력하세요 : ")
Height = int(input("키를 입력하세요(cm) : "))
Weight = int(input("현재 체중을 입력하세요(kg) : "))

nomalWeight = (Height - 100) * 0.9
bmi = (Weight / nomalWeight) * 100

print("-" * 50)
print(f"{name}님의 비만도는 {bmi:.2f}% 입니다.")
print("-" * 50)