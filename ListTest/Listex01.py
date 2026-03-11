products = ['노트북', '마우스', '키보드', '모니터', '웹캠']
stocks = [15, 3, 8, 22, 5]
sum = 0
print("===== 재고현황 =====")
for i in range(0,len(stocks)):

    product = products[i]
    stock = stocks[i]
    # f-string 을 사용하지 않았을때 기준
    # 파이썬은 문자와 숫자를 하나로 나열할수없음
    # str() 함수를 이용해 숫자를 문자열로 변환하여 나열
    msg = product + " : " + str(stock) + "개"
    if stock < 10:
        msg = msg + " (재고 부족)"
    print(msg)

    # if(stocks[i] >= 10):
    #     print(f"{products[i]} : {stocks[i]}개")
    # else:
    #     print(f"{products[i]} : {stocks[i]}개 (재고 부족)")
    # sum += stocks[i]
print()
total = 0
for stock in stocks:
    total += stock

print(f"전체 재고 합계 : {total:,}개")