end = 21
n1 = 0
n2 = 1
while n1 <= end:
    print(f"{n1} ", end="")
    n2 += n1
    n1 = n2 - n1
