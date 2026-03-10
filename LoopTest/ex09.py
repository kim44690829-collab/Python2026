
question1 = input("[1/5] DB 마이그레이션 완료 여부 (Y/N) : ").upper()
if question1 == "Y":
    print("-> 완료")
else:
    print("-> 미완료")
question2 = input("[2/5] application-prod.properties 설정 확인 (Y/N) : ").upper()

question3 = input("[3/5] JWT Secret Key 변경 여부 (Y/N) : ").upper()

question4 = input("[4/5] CORS 허용 도메인 설정 완료 (Y/N) : ").upper()

question5 = input("[5/5] API 엔드포인트 테스트 통과 (Y/N) : ").upper()


