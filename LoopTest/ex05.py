count = int(input("측정횟수 : "))

fast = 0
normal = 0
slow = 0
critical = 0

sum = 0
avg = 0
max = 0

for i in range(1, count+1):
    time = int(input(f"응답 시간 {i} : "))
    if time <= 100:
        print("FAST")
        fast += 1
    elif 101 < time and time <= 300:
        print("NORMAL")
        normal += 1
    elif 301 < time and time <= 1000:
        print("SLOW")
        slow += 1
    else:
        print("CRITICAL")
        critical += 1
    sum += time
    
    if max < time:
        max = time

    min = max

    if min > time:
        min = time

avg = sum / count
print(f"평균 응답 시간 : {avg:.1f}ms")
print(f"최대 : {max}ms | 최소 : {min}ms")
if count * 0.1 < critical:
    print("SLA 위반! 서버 점검이 필요합니다.")