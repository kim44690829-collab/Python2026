name = input("이름 : ")
kor = int(input("국어 : "))
eng = int(input("영어 : "))
math = int(input("수학 : "))

sum = kor + eng + math
avg = sum / 3

print("-" * 30)
print(f"이름 : {name}")
print(f"국어 : {kor}점")
print(f"영어 : {eng}점")
print(f"수학 : {math}점")
print("-" * 30)
print(f"총점 : {sum}점")
print(f"평균 : {avg:.2f}점")
if (kor < 40 or eng < 40 or math < 40) or avg < 60:
    print(f"학점 : F")
elif avg >= 90:
    print(f"학점 : A")
elif avg >= 80:
    print(f"학점 : B")
elif avg >= 70:
    print(f"학점 : C")
else :
    print(f"학점 : D")