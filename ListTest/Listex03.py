orders = [
    {'id': 1, 'product': '노트북', 'amount': 1200000, 'status': 'PAID'},
    {'id': 2, 'product': '마우스', 'amount': 35000, 'status': 'PENDING'},
    {'id': 3, 'product': '모니터', 'amount': 450000, 'status': 'PAID'},
    {'id': 4, 'product': '키보드', 'amount': 89000, 'status': 'CANCELLED'},
    {'id': 5, 'product': '웹캠', 'amount': 75000, 'status': 'PAID'},
]

cart = []
sum = 0

for i in range(len(orders)):
    if orders[i]["status"] == "PAID":
        cart.append(orders[i])
    
print("=== 결제 완료 주문 ===")
for i in range(len(cart)):
    print(f"{cart[i]["id"]}번 주문 / 상품 : {cart[i]["product"]} / 금액 : {cart[i]["amount"]:,}원")
    sum += cart[i]["amount"]
print()
print(f"총 결제 금액 : {sum:,}원")