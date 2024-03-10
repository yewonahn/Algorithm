import sys
input = sys.stdin.readline

n = int(input())

a = n // 5  # 5 최대
b = 0   # 2 개수
check = 0

while a >= 0:
    check = (n - (5 * a)) % 2
    if check == 0:
        b = (n - (5 * a)) // 2
        print(a + b)
        break
    else:
        a -= 1

if a == -1 and check == 1:
    print(-1)
