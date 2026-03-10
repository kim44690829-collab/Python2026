# 다중 for문을 이용해서 구구단 2단 ~ 9단 출력
for i in range(2,10,1):
    
    for j in range(1,10,1):
        print(f"{i} X {j} = {i*j}")
    # 한 단이 끝날때마다 빈칸
    print()