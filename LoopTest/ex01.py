code = int(input("상태코드를 입력하세요 : "))
status = ''
status02 = ''

if code == 200:
    status = "OK - 요청 성공"
elif code == 201:
    status = "Created - 리소스 생성 성공"
elif code == 400:
    status = "Bad Request - 잘못된 요청"
elif code == 401:
    status = "Unauthorized - 인증 필요"
elif code == 403:
    status = "Forbidden - 접근 권한 없음"
elif code == 404:
    status = "Not Found - 리소스 없음"
elif code == 500:
    status = "Internal Server Error - 서버 내부 오류"
else:
    status = "Unknown Status Code"

if 200 <= code and code < 300:
    status02 = "2xx(성공)"
elif 400 <= code and code < 500:
    status02 = "4xx(클라이언트 오류)"
elif 500 <= code and code < 600:
    status02 = "5xx(서버 오류)"


print(f"상태 : {status}")
print(f"계열 : {status02}")