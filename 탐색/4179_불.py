# 칸의 상태 변화함, 가중치 없, 탈출 하는데 걸린 최소 시간 -> BFS
# 종속된 bfs 2개 (지훈이가 해당 칸에 갈 수 있는지 여부가 같은 시간 불의 위치에 영향 받음)
# 1. 불 bfs 먼저
# 2. 불 결과에 따른 지훈이 bfs
from collections import deque
import sys
input = sys.stdin.readline

# 행 / 렬
r, c = map(int, input().split())
# 공백 구분 안된 문자열
miro = [list(map(str, input().strip())) for _ in range(r)]

fire = deque()
visited_fire = [[0] * c for _ in range(r)]
for i in range(r):
    for j in range(c):
        if miro[i][j] == 'F':
            fire.append([i, j])
            visited_fire[i][j] = 1
            # 이중 for 문 다 나갔는지 확인
            #print('break')
            break

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
while fire:
    y, x = fire.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < r and 0 <= nx < c and miro[ny][nx] != '#' and visited_fire[ny][nx] == 0:
            # 자식 노드 시간 = 부모 노드 시간 + 1
            visited_fire[ny][nx] = visited_fire[y][x] + 1
            fire.append([ny, nx])

jh = deque()
visited_jh = [[0] * c for _ in range(r)]
for i in range(r):
    for j in range(c):
        if miro[i][j] == 'J':
            jh.append([i, j])
            visited_jh[i][j] = 1
            break

while jh:
    y, x = jh.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < r and 0 <= nx < c and miro[ny][nx] == '.' and visited_jh[ny][nx] == 0:
            # 불이 해당 칸에 아예 갈 수 없는 경우도 추가
            if visited_fire[ny][nx] > visited_jh[y][x] + 1 or visited_fire[ny][nx] == 0:
                visited_jh[ny][nx] = visited_jh[y][x] + 1
                jh.append([ny, nx])

# 탈출 -> 가장 자리 확인
result = set()
for i in range(c):
    result.add(visited_jh[0][i])
    result.add(visited_jh[r-1][i])
for i in range(1, r-1):
    result.add(visited_jh[i][0])
    result.add(visited_jh[i][c-1])

if result == {0}:
    print('IMPOSSIBLE')
elif 0 in result:
    result.remove(0)
    # 탈출 = 가장 자리 바깥으로 나감
    # 탈출 시간 = min(result) - 1 + 1
    print(min(result))
else:
    print(min(result))
