# 딕셔너리 => 오브젝트
# 딕셔너리 => key : value 가 쌍으로 존재한다.
# 딕셔너리 출력하는 방법 => dict['key'] => 절대로 dict.key로 출력할수 없다.
# phone_book = {'name' : '홍길동', 'age' : 7, 'class' : '고급'}
phone_book = {}
phone_book['홍길동'] = '010-1234-5678'
phone_book['강감찬'] = '010-1234-1234'
phone_book['이순신'] = '010-5678-5678'

print(phone_book)

# 모든 key만 출력
print(phone_book.keys())
# 모든 value만 출력
print(phone_book.values())

# 문제 - phone_book을 강감찬 010-1234-1234 형식으로 출력 (for문 사용)
for keyName in phone_book.keys():
    print(keyName, phone_book[keyName])
