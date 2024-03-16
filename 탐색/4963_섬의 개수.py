# [BFS] 이동 방향 대각선 추가
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
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < h and 0 <= nx < w and jido[ny][nx] == 1 and visited[ny][nx] == 0:
                q.append([ny, nx])
                visited[ny][nx] = 1


while True:
    # 너비, 높이 1 ~ 50
    w, h = map(int, input().split())
    # 입력 마지막 줄 0 0 ->  종료
    if w == 0 and h == 0:
        break

    # 1 땅 / 0 바다
    jido = [list(map(int, input().strip().split())) for _ in range(h)]

    visited = [[0] * w for _ in range(h)]
    cnt = 0

    # 대각선, 상 하 좌 우
    dy, dx = [-1, 0, 1, -1, 0, 1, -1, 1], [-1, -1, -1, 1, 1, 1, 0, 0]
    for b in range(h):
        for a in range(w):
            if jido[b][a] == 1 and visited[b][a] == 0:
                cnt += 1
                bfs(b, a)

    print(cnt)
