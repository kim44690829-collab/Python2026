# 기준 날짜 (연체 확인용)
today = '2025-06-10'

# 도서 목록
books = [
{'id':'B001','title':'파이썬 완전정복','author':'홍길동','genre':'IT','total':3,'available':3},
{'id':'B002','title':'데이터분석 입문','author':'김데이','genre':'IT','total':2,'available':2},
{'id':'B003','title':'알고리즘의 이해','author':'이알고','genre':'IT','total':2,'available':1},
{'id':'B004','title':'채식주의자','author':'한강','genre':'소설','total':4,'available':4},
{'id':'B005','title':'82년생 김지영','author':'조남주','genre':'소설','total':3,'available':3},
]

# 대출 기록
loans = [
{'loan_id':'L000','member':'박지수','book_id':'B003','loan_date':'2025-05-20','due_date':'2025-06-03','returned':False},
{'loan_id':'L001','member':'최우진','book_id':'B001','loan_date':'2025-05-25','due_date':'2025-06-08','returned':False},
]

status = ""

# 도서 목록 조회
def show_books():
    print("도서ID\t제목\t\t\t저자\t\t장르\t전체\t가능\t상태")
    
    for book in range(len(books)):
        # print(books[book]['id'])
        global status
        if books[book]['available'] == 0:
            status = "대출 불가"
        else:
            status = "대출 가능"
        books[book]['status'] = status
        print(f"{books[book]['id']}\t{books[book]['title']}\t\t{books[book]['author']}\t\t{books[book]['genre']}\t{books[book]['total']}\t{books[book]['available']}\t{books[book]['status']}")

loanId = 'L00'
loanIdNum = len(loans) + 1

bookIndex = -1
year = '2025'
month = '6'
if int(month) < 10:
    month = (f"0{month}")
else:
    month = (f"{month}")
day = '10'

# 도서 대출
def loan_book():
    global loanId
    global loanIdNum
    global bookIndex
    global year
    global month
    global day

    name = input('회원명을 입력하세요 : ')
    bookId = input('대출할 도서 ID를 입력하세요 : ')

    # 현재 대출할 도서의 index번호 추출
    for i in range(len(books)):
        if books[i]['id'] == bookId:
            bookIndex = i
            break
    
    if bookIndex == -1:
        print("등록되지 않은 도서입니다.")
        return

    for book in range(len(books)):
        # 도서ID가 있을때
        # 대출 가능한 수량이 없을때 => 현재 대출 가능한 도서가 없습니다.
        if books[bookIndex]['available'] == 0:
            print("현재 대출 가능한 도서가 없습니다.")
            return
        else:
        # 대출 가능한 수량이 있을때
            if len(loans) + 1 > 9:
                loanId = 'L0'
            elif len(loans) + 1 > 99:
                loanId = 'L'
            else:
                loanId = 'L00'
            loanid = (f"{loanId}{loanIdNum}")
            loanIdNum += 1

            loansDate = (f"{year}-{month}-{day}")

            after_14day = int(day) + 14

            if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                if after_14day > 31:
                    int(month) + 1
            else:
                if after_14day > 30:
                    int(month) + 1
            if int(month) > 12:
                int(year) + 1
            
            after_14 = (f"{year}-{month}-{after_14day}")

            loansId = 'loan_id'
            loansMem = 'member'
            loansBookId = 'book_id'
            loansdate = 'loan_date'
            loansDueDate = 'due_date'
            loansReturn = 'returned'
            loans.append({loansId : loanid, loansMem : name, loansBookId : bookId, loansdate : loansDate, loansDueDate : after_14, loansReturn : False})
            print(f"[대출 완료] {name} 님이 '{books[bookIndex]['title']}'을(를) 대출하였습니다.")
            print(f"대출번호 : {loanid} | 반납 예정일 : {after_14}")
            books[bookIndex]['available'] -= 1
            break

# 도서 반납
def return_book():
    index = -1

    loanNum = input('대출 번호를 입력하세요 : ')

    for i in range(len(loans)):
        if loans[i]['loan_id'] == loanNum:
            index = i
            break

    if index == -1:
        print('해당 대출 기록이 없습니다.')
        return

    bookNum = loans[index]['book_id']
    
    for j in range(len(books)):
        if books[j]['id'] == bookNum:
            index2 = j
            break

    if loans[index]['returned'] == False:
        print(f"[반납 완료] '{books[index2]['title']}' 이(가) 반납되었습니다.")
        books[index2]['available'] += 1
        loans[index]['returned'] = True
    else:
        print("이미 반납된 도서입니다.")
returnStatus = ''

# 대출 현황 조회
def show_loans():
    global returnStatus
    print("대출번호\t회원명\t도서제목\t\t대출일\t\t반납예정일\t반납여부")
    for loan in range(len(loans)):
        if loans[loan]['returned'] == False:
            returnStatus = '대출중'
        else:
            returnStatus = '반납완료'
        for i in range(len(books)):
            if books[i]['id'] == loans[loan]['book_id']:
                index = i
                break
        loans[loan]['returnStatus'] = returnStatus
        print(f"{loans[loan]['loan_id']}\t\t{loans[loan]['member']}\t{books[index]['title']}\t\t{loans[loan]['loan_date']}\t{loans[loan]['due_date']}\t{loans[loan]['returnStatus']}")


# 연체 현황 조회
def show_overdue():
    global year
    global month
    global day
    loansDate = (f"{year}-{month}-{day}")
    print(f"=== 연체 현황 (기준일 : {loansDate}) ===")
    print("대출번호\t회원명\t도서제목\t반납예정일")
    print("-" * 60)
    for i in range(len(loans)):
        loans[i]['due_day_detail']
# # 장르별 통계
# def show_genre_stats():

run = True

while run:
    print("=== 도서관 대출 관리 시스템 ===")
    print("1. 도서 목록 조회\n2. 도서 대출\n3. 도서 반납\n4. 대출 현황 조회\n5. 연체 현황 조회\n6. 장르별 통계\n0. 종료\n")
    sel = int(input("메뉴를 선택하세요 : "))
    if sel == 1:
        show_books()
    elif sel == 2:
        loan_book()
    elif sel == 3:
        return_book()
    elif sel == 4:
        show_loans()
    elif sel == 5:
        show_overdue()
    # elif sel == 6:
    #     show_genre_stats()
    elif sel == 0:
        print("시스템을 종료합니다.")
        run = False
    else:
        print("0 ~ 6 사이의 번호를 선택해주세요.")
    print()