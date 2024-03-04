def divide(n):
    # 자릿수로 케이스 나누기
    if n < 10:
        return n
    elif n < 100:
        remainder = n % 10
        s = n // 10 + remainder
        return s
    elif n < 1000:
        remainder = n % 100
        s = n // 100 + divide(remainder)
        return s
    elif n < 10000:
        remainder = n % 1000
        s = n // 1000 + divide(remainder)
        return s

# d(n) 의 결과
# num : 셀프 넘버가 아닌 케이스
num = []

n = 1
result = 0

while result <= 10000:
    # result : d(n)
    result = n + divide(n)
    num.append(result)
    # print("n : ", n, "result: ", result)
    n += 1

for i in range(1, 10000):
    # 셀프 넘버 여부(생성자 없는 숫자)
    isSelfNum = True
    for j in num:
        # 생성자가 있는 경우 break
        if j == i:
            isSelfNum = False
            break
    # 셀프 넘버인 경우 출력 (생성자 없는 경우)
    if isSelfNum:
        print(i)




