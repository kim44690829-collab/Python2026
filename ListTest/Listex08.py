subjectList = [
    {'subject' : 'Python 프로그래밍', 'score' : 92, 'credit' : 3},
    {'subject' : 'SpringBoot 개발', 'score' : 88, 'credit' : 3},
    {'subject' : 'React 프론트엔드', 'score' : 76, 'credit' : 2},
    {'subject' : '데이터베이스', 'score' : 95, 'credit' : 3},
    {'subject' : '알고리즘', 'score' : 68, 'credit' : 2},
]

pointSum = 0
rankSum = 0

countAplus = 0
countA = 0
countBplus = 0
countB = 0
countCplus = 0
countC = 0
countD = 0
countF = 0

rankDistribution = {}

print("=== 성적표 ===")
print(f"{"과목"} {"점수":>30}{"학점":>10}{"학점포인트":>10}{"이수학점":>10}")
for subList in subjectList:
    if subList['score'] >= 95:
        rank = 'A+'
        point = 4.5
        countAplus += 1
        rankDistribution += {rank : countAplus}
    elif subList['score'] >= 90:
        rank = 'A'
        point = 4.0
        countA += 1
        rankDistribution += {rank : countA}
    elif subList['score'] >= 85:
        rank = 'B+'
        point = 3.5
        countBplus += 1
        rankDistribution += {rank : countBplus}
    elif subList['score'] >= 80:
        rank = 'B'
        point = 3.0
        countB += 1
        rankDistribution += {rank : countB}
    elif subList['score'] >= 75:
        rank = 'C+'
        point = 2.5
        countCplus += 1
        rankDistribution += {rank : countCplus}
    elif subList['score'] >= 70:
        rank = 'C'
        point = 2.0
        countC += 1
        rankDistribution += {rank : countC}
    elif subList['score'] >= 60:
        rank = 'D'
        point = 1.0
        countD += 1
        rankDistribution += {rank : countD}
    else:
        rank = 'F'
        point = 0
        countF += 1
        rankDistribution = {rank : countF}
    pointSum += point * subList['credit']
    rankSum += subList['credit']

    

    print(f"{subList['subject']:>11} {subList['score']:>20} {rank:>10} {point:>10}{subList['credit']:>10}학점")
    
print(f"GPA : {(pointSum/rankSum):.2f} / 4.50 (총 {rankSum}학점)")
print(f"학점 분포 : {rankDistribution}")
