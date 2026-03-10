
totalPrice = 0
discountPrice = 0
totalCnt = 0
discount = 0

while True:
    rank = input("회원 등급 (END 종료) : ").upper()
    if rank == "END":
        break
    if rank not in ["BRONZE", "SILVER", "GOLD", "VIP"]:
        print("등록되지 않은 등급입니다.")
        continue

    price = int(input("구매 금액 : "))
    
    if rank == "BRONZE":
        discountPrice += 0
        discount = 0
        
    elif rank == "SILVER":
        discountPrice += int(price * 0.05)
        discount = int(price * 0.05)
        
    elif rank == "GOLD":
        discountPrice += int((price * 0.1) + 5000)
        discount = int((price * 0.1) + 5000)
        
    else:
        discountPrice += int((price * 0.2) + 10000)
        discount = int((price * 0.2) + 10000)
        
    print(f"할인금액 : {discount}원 -> 결제 금액 : {price - discount}원")
    totalPrice += price
    totalCnt += 1

print("--- 전체 주문 요약 ---")
print(f"주문 건수 : {totalCnt}건")
print(f"총 구매 금액 : {totalPrice:,}원  |  총 할인 : {discountPrice:,}원  |  총 결제 : {(totalPrice - discountPrice):,}원")