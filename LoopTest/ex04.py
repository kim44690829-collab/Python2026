token = int(input("토큰 수를 입력하세요 : "))
dangerToken = 0
normalToken = 0

for i in range(1, token+1):
    time = int(input(f"토큰 {i} 잔여시간(분) : "))
    if time <= 0:
        print("[만료] 즉시 재발급 필요")
        dangerToken += 1
    elif 1 <= time and time <= 10:
        print("[위험] 곧 만료됩니다. 갱신 권장")
        dangerToken += 1
    elif 11 <= time and time <= 30:
        print("[주의] 만료가 가까워지고 있습니다.")
        dangerToken += 1
    else:
        print("[정상] 유효한 토큰")
        normalToken += 1
print("--- 요약 ---")
print(f"정상 토큰 : {normalToken}개 / 위험·만료 토큰 {dangerToken}개")
