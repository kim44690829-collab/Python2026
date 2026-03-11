transactions = [
    ['2024-01', 3200000],
    ['2024-01', 1500000],
    ['2024-02', 2800000],
    ['2024-02', 900000],
    ['2024-03', 4100000],
    ['2024-03', 2200000],
    ['2024-04', 1800000],
    ['2024-04', 3300000],
    ['2024-05', 5000000],
    ['2024-06', 2100000]
]

transactionsSum = {}

for trans in transactions:
    month = trans[0]
    print(month)
    # if trans[0] in transactionsSum:
    #     transactionsSum[trans[0]] += trans[1]
    # else:
    #     transactionsSum[trans[0]] = trans[0]

# print(transactionsSum)

total = 0
print("=== 월별 매출 ===")
for i in range(len(transactions)):
    print(f"{transactions[i][0]} : {transactions[i][1]}원")
    if i == 0:
        max = transactions[i][1]
        maxDay = transactions[i][0]
        min = transactions[i][1]
        minDay = transactions[i][0]
    else:
        if transactions[i][1] > max:
            max = transactions[i][1]
            maxDay = transactions[i][0]
        if transactions[i][1] < min:
            min = transactions[i][1]
            minDay = transactions[i][0]
    total += transactions[i][1] / len(transactions)
print()
print(f"최고 매출 월 : {maxDay} ({max:,}원)")
print(f"최저 매출 월 : {minDay} ({min:,}원)")
print(f"월 평균 매출 : {total:,.0f}원")
