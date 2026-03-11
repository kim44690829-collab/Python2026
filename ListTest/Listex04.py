response = {
'code' : 200,
'message': 'success',
'data' : [
    {'userId': 'user01', 'name': '이자바', 'score': 95},
    {'userId': 'user02', 'name': '박리액트', 'score': 82},
    {'userId': 'user03', 'name': '최스프링', 'score': 91},
    {'userId': 'user04', 'name': '정마이바티스', 'score': 78},
]
}

highScore = []
count = 0

print("=== 전체 성적 ===")
for res in response['data']:
    print(f"{res['name']} ({res['userId']}) : {res['score']}점")
    if res['score'] >= 90:
        highScore.append(res)
        count += 1
print()
print(f"=== 우수 수강생 (90점 이상) : {count}명 ===")
for i in range(len(highScore)):
    print(f"★ {highScore[i]['name']} : {highScore[i]['score']}점")