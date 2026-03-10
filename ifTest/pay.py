name = input("이름을 입력하세요 : ")
pay1Hour = int(input("시급을 입력하세요(원) : "))
workTime = int(input("하루 근무 시간을 입력하세요(h) : "))
workDay = int(input("근무 일수를 입력하세요(일) : "))
workStartTime = int(input("근무 시작 시간을 입력하세요(0 ~ 23) : "))

#총 근무 시간
totalWorkTime = float(workTime) * workDay
nightPay = int(pay1Hour * 1.5)


# 야간 근무
if 22 <= workStartTime:
    totalPay = (24 - workStartTime) * nightPay
    time = workTime - (24 - workStartTime)
    if time <= 6:
        totalPay += time * nightPay
    else:
        totalPay += (time * nightPay) + ((time - 6) * pay1Hour)
elif workStartTime < 6:
    totalPay = (6 - workStartTime) * nightPay
    time2 = workTime - (6 - workStartTime)
    if time2 > 0:
        totalPay += time2 * pay1Hour
else:
    totalPay = pay1Hour * workTime

totalPay *= workDay
#야간근무 x
# totalPay = (pay1Hour * workTime) * workDay

if totalWorkTime >= 15 and (22 < workStartTime or workStartTime < 6):
    plusOneDay = pay1Hour * workTime
elif totalWorkTime >= 15 and (6 <= workStartTime or workStartTime < 22):
    plusOneDay = nightPay * workTime
else:
    plusOneDay = 0


print("=" * 50)
print(f"{"급여 명세서":^50}")
print("=" * 50)
print(f"이름 : {name}")
print(f"{"시급 : "}{pay1Hour:<10,}원")
print(f"{"근무시간 : "}{totalWorkTime}시간 ({float(workTime)} x {workDay}일)")

if 22 <= workStartTime or workStartTime < 6:
    print(f"{"야간 근무 : 해당 있음. 시급 ("}{(nightPay):<10,})원 적용")
else:
    print(f"야간 근무 : 해당 없음.")
if totalWorkTime >= 15:
    print(f"주휴수당 : 해당 있음.")
else:
    print(f"주휴수당 : 해당 없음.")
print("=" * 50)
if 22 < workStartTime or workStartTime < 6:
    print(f"기본급 : {totalPay:<10,}원")
else:
    print(f"기본급 : {totalPay:<10,}원")
if totalWorkTime >= 15 and (22 < workStartTime or workStartTime < 6):
    print(f"주휴수당 : {plusOneDay:<10,}원")
elif totalWorkTime >= 15 and (6 <= workStartTime or workStartTime < 22):
    print(f"주휴수당 : {plusOneDay:<10,}원")
else:
    print(f"주휴수당 : 해당 없음.")
print(f"세금 (3.3%) : {int((totalPay + plusOneDay) * 3.3 * 0.01):<10,}원")
print("-" * 50)
print(f"실수령액 : {((totalPay + plusOneDay) - int((totalPay + plusOneDay) * 3.3 * 0.01)):<10,}원")
print("=" * 50)