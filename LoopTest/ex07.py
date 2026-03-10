pw = input("비밀번호 입력 : ")
condition1 = "X"
condition2 = "X"
condition3 = "X"
condition4 = "X"
condition5 = "X"
count = 0
countText = ''

for ch in pw:
    if len(pw) >= 8:
        condition1 = "O"
    if ch >= 'A' and ch <= 'Z':
        condition2 = "O"
    if ch >= 'a' and ch <= 'z':
        condition3 = "O"
    if ch >= '0' and ch <= '9':
        condition4 = "O"
    if not(ch >= 'A' and ch <= 'Z') and not(ch >= 'a' and ch <= 'z') and not(ch >= '0' and ch <= '9'):
        condition5 = "O"

if condition1 == "O":
    count += 1
if condition2 == "O":
    count += 1
if condition3 == "O":
    count += 1
if condition4 == "O":
    count += 1
if condition5 == "O":
    count += 1

if count >= 5:
    countText = "매우 강함"
elif count >= 4:
    countText = "강함"
elif count >= 3:
    countText = "보통"
elif count >= 2:
    countText = "취약"
else:
    countText = "매우 취약"

print(f"[{condition1}] 길이8자 이상 여부")
print(f"[{condition2}] 대문자 포함")
print(f"[{condition3}] 소문자 포함")
print(f"[{condition4}] 숫자 포함")
print(f"[{condition5}] 특수문자 포함")
print(f"비밀번호 강도 : {countText}")