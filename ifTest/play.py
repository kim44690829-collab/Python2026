month = int(input("방문 월을 입력하세요(1~12) : "))
Adult = int(input("성인 인원수를 입력하세요 : "))
Teen = int(input("청소년 인원수를 입력하세요 : "))
Child = int(input("어린이 인원수를 입력하세요 : "))
Senior = int(input("경로 인원수를 입력하세요 : "))

AdultPrice = Adult * 55000
TeenPrice = Teen * 40000
if Child >= 3 and (month != 7 and month != 8):
    ChildPrice = 0
else:
    ChildPrice = Child * 28000
SeniorPrice = Senior * 15000

totalPerson = Adult + Teen + Child + Senior
totalPrice = AdultPrice + TeenPrice + ChildPrice + SeniorPrice
if totalPerson >= 5 and (month != 7 and month != 8):
    finalPrice = int(totalPrice - (totalPrice * 0.1))
else:
    finalPrice = totalPrice

print("=" * 50)
print("놀이공원 입장권 계산서")
print("=" * 50)
if month == 7 or month == 8:
    print(f"방문월 : {month}월 (성수기)")
else:
    print(f"방문월 : {month}월 (비수기)")
print("=" * 50)
print(f"성인\t{Adult}명 : {AdultPrice:<10,}원")
print(f"청소년\t{Teen}명 : {TeenPrice:<10,}원")
if Child >= 3 and (month != 7 and month != 8):
    print(f"어린이\t{Child}명 : 0원 (무료!)")
else:    
    print(f"어린이\t{Child}명 : {ChildPrice:<10,}원")
print(f"경로\t{Senior}명 : {SeniorPrice:<10,}원")
print("=" * 50)
print(f"소계 : {totalPrice:<10,}원")
if totalPerson >= 5 and (month != 7 and month != 8):
    print(f"단체 할인 : {-int(totalPrice*0.1):<10,}원")
else:
    print(f"단체 할인 : 0원")
print("-" * 50)
print(f"최종금액 : {finalPrice:<10,}원")
print("=" * 50)
print(f"총 인원 : {totalPerson}명")
print("=" * 50)