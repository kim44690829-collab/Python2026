ticket_no = "2026-0309-01"
place = "7관 (4층)"
movieName = "파이썬의 습격"
movieTime = "14:30 ~ 16:10"

personType1 ,price1, personQ1 = "일반 성인", 15000, 2
personType2 ,price2, personQ2 = "청소년", 10000, 1

sum1 = price1 * personQ1
sum2 = price2 * personQ2

total = sum1 + sum2

print("=" * 60)
print(f"{"PYTHON CINEMA":^60}")
print("=" * 60)
print(f"티켓번호 : {ticket_no}")
print(f"상영관 : {place}")
print(f"영화명 : {movieName}")
print(f"상영시간 : {movieTime}")
print("-" * 60)
print(f"{"구분":<20} {"단가":>10} {"인원":>10} {"금액":>10}")
print("-" * 60)
print(f"{personType1:<20} {price1:>10,} {personQ1:>10} {sum1:>10,}")
print(f"{personType2:<20} {price2:>10,} {personQ2:>10} {sum2:>10,}")
print("-" * 60)
print(f"{"총 결제 금액":<20} {total:>30,}")
print("=" * 60)