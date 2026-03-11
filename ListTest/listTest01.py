# 리스트 = 배열과 같은 역할을 한다.
# 리스트 [숫자, 문자, 혼합] 사용가능
# 동적 = 고정길이가 아니다.
# 속도는 조금 느림

heroes = []
# 리스트 추가하는 방법
# 1. append('추가할 문자') => 맨 뒤에 추가
# 2. insert(인덱스 번호, '추가할 문자') => 인덱스번호에 추가할 문자 추가
heroes.append("아이언맨")
heroes.append("닥터 스트레인지")
heroes.insert(1,"왕과 사는 남자")
print(heroes)

# 리스트 삭제
# 1. remove('삭제할 문자')
# 2. del heroes[삭제할 인덱스 번호] => 인덱스 번호에 해당하는 데이터 삭제
# 3. pop() => 맨 마지막 데이터 삭제
heroes.remove("왕과 사는 남자")
print(heroes)
del heroes[1]
print(heroes)
heroes.pop()
print(heroes)
heroes.append("a")
heroes.append("b")
heroes.append("c")
heroes.append("d")
print(heroes)

# for 문을 이용해서 출력
for hero in heroes:
    print(hero, end = " ")
print()
# 리스트 slice
# heroes[0:3] => 0번째부터 3글자
# heroes[:3] => 처음부터 3글자
# heroes[3:] => 3번째부터 마지막까지
# heroes[:] => 전체 출력 => 굳이 안씀
# cut = heroes[0:2] # => ['a', 'b']
cut = heroes[3:]  # => ['d']
print(cut)

# 문제 - movieTitle = [] 에 아래 영화 제목 4개를 추가하세요
movieTitle = []
movieTitle.append("아이언맨")
movieTitle.append("토르")
movieTitle.append("헐크")
movieTitle.append("스칼렛 위치")

for m in movieTitle:
    print(m, end=" ")
print()

# 문제 - movieTitle에서 토르가 존재하면 삭제하고 출력
if "토르" in movieTitle:
    movieTitle.remove("토르")

movieTitle.sort(reverse=True)

for m in movieTitle:
    print(m, end=" ")
print()