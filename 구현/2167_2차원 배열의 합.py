# [풀이 참조]
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# 풀이 참조
lst = [list(map(int, input().split())) for _ in range(n)]

k = int(input())
for b in range(k):
    i, j, x, y = map(int, input().strip().split())
    result = 0

    for c in range(i - 1, x):
        for d in range(j - 1, y):
            result += lst[c][d]

    print(result)
