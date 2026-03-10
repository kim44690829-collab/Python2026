# 이스케이프 문자, 서식 문자 이용 => 영수증 출력
# 파이썬은 변수를 선언할 때 변수 선언 명령문이 존재하지 않는다.

# received가 총금액보다 작으면 "금액이 부족합니다." 아니면 거스름돈

# 데이터 준비
order_no = "12345678"
address = "서울시 종로구 종로3가"
name = "개나리"
phone = "010-1234-5678"

# 계산
# 파이썬은 변수 여러개를 나란히, 상수를 나란히 정의할 수 있다.
# ex) a, b, c = 1, 2, 3
item1, p1, q1 = "블루투스 이어폰", 85000, 2
item2, p2, q2 = "USB3.0 8G", 8000, 1

# 파이썬 사칙연산 => 자바와 동일
atm1 = p1 * q1
atm2 = p2 * q2

total = atm1 + atm2
received = 100000
change = received - total

# 서실 문자는 f-string => (현재 표준으로 사용)
# ^ => 가운데 정렬, 45 => 길이
print(f"{"파이썬 쇼핑몰":^45}")
print(f"번호: {order_no}")
print(f"주소: {address}")
print(f"성명: {name}")
print(f"전화: {phone}")

# "-" 를 60번 반복
print("-" * 60)

# <20 : 20칸 왼쪽
# >20 : 20칸 오른쪽
print(f"{"품명":<20} {"단가":>10} {"수량":>5} {"금액":>10}")
print("-" * 60)

# 천단위 콤마 : >10,
print(f"{item1:<20} {p1:>10} {q1:>7} {atm1:>10,}")
print(f"{item2:<30} {p2:>10} {q2:>7} {atm2:>10,}")
print("-" * 60)

# 결제 정보
print(f"{"소계":<45}{total:>10,}")
print("-" * 60)
print(f"{"청구금액":<43}{total:>10,}")
print(f"{"받은금액":<43}{received:>10,}")
if received > total:
    print(f"{"거스름돈":<43}{change:>10,}")    
else:
    print("금액이 부족합니다.")
print("-" * 60)