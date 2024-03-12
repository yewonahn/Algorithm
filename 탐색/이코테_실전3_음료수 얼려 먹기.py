# DFS
import sys

def dfs(y, x):
    if 0 <= y < n and 0 <= x < m:
        # 인접한 0 찾고, visited 표시
        if lst[y][x] == 0:
            lst[y][x] = 1
            dfs(y - 1, x)
            dfs(y, x - 1)
            dfs(y, x + 1)
            dfs(y + 1, x)


input = sys.stdin.readline

# 세로 n, 가로 m
n, m = map(int, input().split())
lst = [list(map(int, input().strip())) for _ in range(n)]
# print(lst)

visited = []
result = 0

for i in range(n):
    for j in range(m):
        if lst[i][j] == 0:
            dfs(i, j)
            result += 1

print(result)
