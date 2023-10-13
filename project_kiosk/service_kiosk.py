# 키오스크 기능들

# 사용자 메뉴 선택 기능!

def user_choice():
    while True:
        choice = int(input(">> 번호: "))
        if 3 >= choice >= 1 or choice == 99:
            break
        else:
            print("MSG: 올바른 번호를 입력하세요.")
