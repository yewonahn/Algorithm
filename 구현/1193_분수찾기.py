import sys

# 1 부터 n 까지의 합
def add(a):
    result = 0
    for i in range(1, a + 1):
        result += i
    return result

# 짝 (, 1) 부터 시작
def even(order):
    # print("even")
    global a, b, n
    a = (n + 2) - order
    b = order

# 홀 (1, ) 부터 시작
def odd(order):
    # print("odd")
    global a, b, n
    a = order
    b = (n + 2) - order

input = sys.stdin.readline
x = int(input())

# 좌표 (a, b)
a = 0
b = 0

n = 1
# x 가 몇 번째 그룹에 속해 있는지 -> n + 1 번째 그룹
while True:
    if x == 1:
        a = 1
        b = 1
        break
    elif add(n) < x <= add(n + 1):
        break
    n += 1

# print("x 가 속해 있는 그룹 (n+1): ", n+1)

# (1, 1) 제외
if x != 1:
    # 그룹 안에서 몇 번째 인지
    order = x - add(n)
    # print("order : ", order)

    # n + 2 = (해당 그룹 요소의) 좌표 합
    # n + 2 짝수
    if (n + 2) % 2 == 0:
        # print("짝")
        even(order)
    # n + 2 홀수
    else:
        # print("홀")
        odd(order)

print(a, "/", b, sep='')
