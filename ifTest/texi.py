startPlace = input("출발지를 입력하세요 : ")
endPlace = input("목적지를 입력하세요: ")
Distance = float(input("이동 거리를 입력하세요 : "))
BoardingTime = int(input("탑승 시간을 입력하세요 : "))
isChildren = input("어린이 동반 탑승 여부를 입력하세요 (y / n) : ")

if isChildren == "y":
    nomalPrice = 0
else:
    nomalPrice = 4800

nomalDistance = 2000
totalDistance = Distance * 1000

if totalDistance > nomalDistance:
    ditancePrice = int(totalDistance - nomalDistance)
else:
    ditancePrice = 0

if BoardingTime > 22 or BoardingTime < 4:
    nightPrice = int((nomalPrice + ditancePrice) * 0.2)
else:
    nightPrice = 0

print("=" * 60)
print(f"출발지 : {startPlace}")
print(f"목적지 : {endPlace}")
print(f"이동거리 : {Distance}km")
print(f"탑승시간 : {BoardingTime}시")
print("=" * 60)
if isChildren == "y":
    print(f"{"어린이 동반 탑승으로 기본요금 : "}{nomalPrice:<10,}원")
else:
    print(f"{"기본요금 : "}{nomalPrice}원")
if totalDistance > nomalDistance:
    print(f"{"거리요금 : "}{ditancePrice:<10,}원")
else:
    print(f"기본요금입니다.")
if BoardingTime > 22 or BoardingTime < 4:
    print(f"{"심야할증 : "}{nightPrice:<10,}원 (20% 적용)")
else:
    print(f"심야할증 적용 X")
print("-" * 60)
print(f"{"최종요금 : "}{nomalPrice + ditancePrice + nightPrice:<10,}원")
print("=" * 60)

