selectQ = 0
insertQ = 0
updateQ = 0
deleteQ = 0

while True:
    # input("쿼리 유형 입력 : ").upper() => 소문자를 입력해도 대문자로 출력
    # input("쿼리 유형 입력 : ").lower() => 대문자로 입력해도 소문자로 출력
    quary = input("쿼리 유형 입력 : ").upper()
    # exit입력시 종료
    if quary == "EXIT":
        break
    # 쿼리별 숫자 누적
    if quary == "SELECT":
        selectQ += 1
    elif quary == "INSERT":
        insertQ += 1
    elif quary == "UPDATE":
        updateQ += 1
    elif quary == "DELETE":
        deleteQ += 1
    else:
        print("알 수 없는 쿼리 유형입니다.")

    total = selectQ + insertQ + updateQ + deleteQ

    # REPORT 입력시 쿼리 실행 현황 출력
    if quary == "REPORT":
        print("--- 쿼리 실행 현황 ---")
        print(f"SELECT : {selectQ}회")
        print(f"INSERT : {insertQ}회")
        print(f"UPDATE : {updateQ}회")
        print(f"DELETE : {deleteQ}회")
        print(f"총 실행 : {total}회")
        if (total * 0.7) <= selectQ:
            print("SELECT 쿼리 비중이 높습니다. 캐싱을 고려하세요.")
    

print("--- 쿼리 실행 현황 ---")
print(f"SELECT : {selectQ}회")
print(f"INSERT : {insertQ}회")
print(f"UPDATE : {updateQ}회")
print(f"DELETE : {deleteQ}회")
print(f"총 실행 : {total}회")
if (total * 0.7) <= selectQ:
    print("SELECT 쿼리 비중이 높습니다. 캐싱을 고려하세요.")