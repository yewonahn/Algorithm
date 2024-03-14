from collections import deque
import sys
input = sys.stdin.readline

# 최소 날짜 출력, 가중치 없음 -> bfs
# 가로, 세로 / 2 ≤ M,N ≤ 1,000
m, n = map(int, input().split())

# 1은 익은 / 0은 안 익 / -1은 안 들어있
# 여기에 날짜도 저장 하면 되므로 따로 날짜 저장 리스트 안 만들어도 됨
# 단, 당일은 0일. 보관 후 다음날 부터 1일차로 count 이므로 결과 출력 시 -1 필요
lst = [list(map(int, input().strip().split())) for _ in range(n)]

# 탐색할 점 저장
q = deque()
for i in range(n):
    for j in range(m):
        if lst[i][j] == 1:
            q.append([i, j])

# [[y-1, x], [y+1, x], [y, x-1], [y, x+1]]
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
while q:
    y, x = q.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        # 0부터 시작이니까 n, m 포함 x
        if 0 <= ny < n and 0 <= nx < m and lst[ny][nx] == 0:
            q.append([ny, nx])
            # 날짜 누적 저장
            lst[ny][nx] = lst[y][x] + 1

# 토마토 상태 확인
for i in lst:
    for j in i:
        # j == 토마토 상태
        # 1. 안 익은 토마토 있
        if j == 0:
            print(-1)
            exit()

# 2. 이미 다 익어 있는 경우 (lst 에 1 or -1) 이므로 max() -> 1 이므로 print(0) 됨
# 3. 최소 날짜 출력
print(max(map(max, lst)) - 1)
