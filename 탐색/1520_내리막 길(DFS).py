# 특정 점에서 목적지 까지 갈 수 있는 경로 찾을 땐 dfs 이용
# 특정 점에서 목적지 까지 가능 경로 수 구하는 반복 수행 안하기 위해 경로 수 누적 저장 -> dp
# dp 에 저장 되는 값 = 해당 점에서 목적지 점까지 이동 하는데 가능한 경로 수
# 재귀 돌아 오면서 dp 이용 하므로 목적지에서 가까운 점부터, dp에 누적 저장

import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline

# 세로, 가로
m, n = map(int, input().strip().split())
map = [list(map(int, input().strip().split())) for _ in range(m)]

def dfs(y, x):
    # 목적지 점 (m-1. n-1)
    # 목적지 점 -> 목적지 점 까지 가는 방법 = 1 이니까
    if y == m - 1 and x == n - 1:
        dp[y][x] = 1
        return
    # 방문 했는지 여부 확인 해서
    # 1. 방문한 적 있는 점이면 dp에 저장 되어 있는 값 return
    if visited[y][x] == 1:
        # 다른 케이스 (경로) 에서 이미 해당 점에서 목적지까지 가는 경로 cnt 했으면 중복 수행 안하기 위해
        return
    visited[0][0] = 1
    # 2. 처음 방문 하는 점인 경우
    # 해당 점의 상하좌우 돌면서
    visited[y][x] = 1
    dy, dx = [0, 0, -1, 1], [-1, 1, 0, 0]
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        # 갈 수 있는 점인지 확인
        if 0 <= ny < m and 0 <= nx < n and map[ny][nx] < map[y][x]:
            dfs(ny, nx)
            dp[y][x] += dp[ny][nx]


visited = [[0] * n for _ in range(m)]
# 경로의 수 저장
dp = [[0] * n for _ in range(m)]
dfs(0, 0)
# dp에 저장 되는 값은 해당 점에서 목적지 점까지 가능한 경로의 수 이므로
# dp[m-1][n-1] 이 아닌 dp[0][0] 출력 해야 함
print(dp[0][0])
