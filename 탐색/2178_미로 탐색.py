from collections import deque
import sys
input = sys.stdin.readline

# 세로 n / 가로 m
n, m = map(int, input().split())

# 입력 값 사이에 공백 없음
miro = [list(map(int, input().strip())) for _ in range(n)]

# 구해야 하는 것 : 목적지에 도착하기 위해 지나야 하는 **최소 칸**
# -> visited 테이블에 이동 칸 수 누적 기록 (부모에 저장되어 있는 값 + 1)
visited = [[0] * m for _ in range(n)]
# 문제 (1, 1) -> (N, M)
# 풀이 (0, 0) -> (n-1, m-1)
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
q = deque()
# 시작 위치 (0, 0)
q.append([0, 0])
while q:
    y, x = q.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < m and miro[ny][nx] == 1 and visited[ny][nx] == 0:
            visited[ny][nx] = visited[y][x] + 1
            q.append([ny, nx])

# 이동 칸 수 : 시작, 도착 위치 포함
print(visited[n-1][m-1] + 1)
