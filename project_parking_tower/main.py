# 주차타워 구현!
#  조건: 1층 ~ 5층, 층별로 1대만 주차
#        차량번호: 숫자4자리
#  기능:
#    1) 차량입고
#    2) 차량출고
#    3) 차량조회
#    4) 프로그램 종료

# 설정
max_car = 5  # 최대 5대

# 주차 타워 생성
# 1.List Comprehension
tower = ["" for i in range(max_car)]

# 2.for + list.append()
# tower = []
# for i in range(max_car):
#     tower.append("")
# 결과: ["", "", "", "", ""]

while True:
    print("=" * 50)
    print("== 주차 타워 시스템 ver1.1 ==")
    print("=" * 50)
    print("= 1.입고")
    print("= 2.출고")
    print("= 3.조회")
    print("= 4.종료")
    print("=" * 50)

    while True:
        select_num = int(input(">>번호: "))
        if 4