member = {
'name' : '김파이썬',
'email' : 'python@example.com',
'age' : 40,
'grade' : 'GOLD'
}

ageText = ''
phoneNum = ''

print("=== 회원 정보 ===")
for mem in member.keys():
    print(f"{mem} : {member[mem]}")

if member["age"] < 20:
    ageText = '주니어'
elif member["age"] < 40:
    ageText = "일반"
else:
    ageText = "시니어"

if "phone" in member.keys():
    phoneNum = member["phone"]
else:
    phoneNum = "미등록"

print()
print(f"연령 구간 : {ageText}")
print(f"전화번호 : {phoneNum}")
