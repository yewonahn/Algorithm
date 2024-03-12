import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
lst = [[0] * (m + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    nums = list(map(int, input().strip().split()))
    for e in range(1, m + 1):
        lst[a][e] = nums[e - 1]

k = int(input())
for b in range(k):
    i, j, x, y = map(int, input().strip().split())
    result = 0

    for c in range(i, x + 1):
        for d in range(j, y + 1):
            result += lst[c][d]

    print(result)
