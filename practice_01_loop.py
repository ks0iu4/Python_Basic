# 문제1) 입력 된 단수를 출력하는 코드
#    dan = input("단수: ")
#    for i in range(1, 10):
#        print("{}x{}={}".format(int(dan), i, i * int(dan)))


# 문제2) 2단 9단까지 출력하는 코드
for i in range(2, 10):
    for j in range(1, 10):
        print("{}x{}={}".format(i, j, i * j))

# 문제3) list a의 평균값을 계산하세요.
a = [1, 2, 3, 4, 5, 99, 87, 54, 2, 5, 4]
# total => 총합
length = len(a)
total = 0
for i in a:
    total += i
result = total / length
print(round(result, 2)) # 평균값

# 문제4) list b에서 최소값 찾기!
b = [22, 1, 4, 7, 98]

print(num_min) # 1 출력