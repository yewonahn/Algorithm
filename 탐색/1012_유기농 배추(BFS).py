# [BFS]
from collections import deque
import sys
input = sys.stdin.readline

def bfs(b, a):
    global visited
    q = deque()
    q.append([b, a])
    visited[b][a] = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            # location[ny][nx] == 1 조건 누락 주의
            if 0 <= ny < n and 0 <= nx < m and location[ny][nx] == 1 and visited[ny][nx] == 0:
                q.append([ny, nx])
                visited[ny][nx] = 1


# 배추 뭉치 수를 구하면 됨
# 테스트 케이스 누락 주의
t = int(input())
for _ in range(t):
    # 가로, 세로, 배추 개수
    m, n, k = map(int, input().split())
    # 배추 위치
    location = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        location[y][x] = 1

    visited = [[0] * m for _ in range(n)]
    cnt = 0

    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    for b in range(n):
        for a in range(m):
            if location[b][a] == 1 and visited[b][a] == 0:
                cnt += 1
                bfs(b, a)

    print(cnt)
