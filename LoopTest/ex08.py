targetSales = int(input("목표 일 매출액 : "))

day1, day2, day3, day4, day5, day6, day7 = "월", "화", "수", "목", "금", "토", "일"

totalPay = 0
dayAvg = 0
count = 0
# max = 0
# maxDay = ''
# minDay = ''

for i in range(1, 8):
    if i == 1:
        i = day1
    elif i == 2:
        i = day2
    elif i == 3:
        i = day3
    elif i == 4:
        i = day4
    elif i == 5:
        i = day5
    elif i == 6:
        i = day6
    else:
        i = day7
    
    daySales = int(input(f"{i}요일 매출 : "))

    if targetSales < daySales:
        print("-> 목표 달성")
        count += 1
    elif targetSales * 0.7 < daySales and targetSales > daySales:
        print("-> 분발 필요")
    else:
        print("-> 목표 미달")

    if i == "월":
        max = daySales
        min = daySales
        maxDay = i
        minDay = i
    else:
        if max < daySales:
            max = daySales
            maxDay = i

        if min > daySales:
            min = daySales
            minDay = i
    
    totalPay += daySales

dayAvg = totalPay / 7

print(f"총 매출 : {totalPay:,} | 일 평균 : {dayAvg:,.0f}")
print(f"최고 매출 : {maxDay}요일 {max:,}원 | 최저 매출 : {minDay}요일 {min:,}원")
print(f"목표 달성 : {count}일")