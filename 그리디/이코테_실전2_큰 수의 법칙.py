import sys
input = sys.stdin.readline

# 배열의 크기 / 숫자가 더해지는 횟수 / 최대 연속 갯수
n, m, k = map(int, input().split())
lst = list(map(int, input().strip().split()))
lst.sort()

top = lst[n - 1]
next = lst[n - 2]
result = 0
if top != next:
    result = (top * k + next) * (m // (k + 1)) + top * (m % (k + 1))
else:
    result = top * m
print(result)
