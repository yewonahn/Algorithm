# 한 줄에 하나씩 출력 참고 -> print(*home, sep='\n')
# 가중치 없 / 칸 안에 있는 상태 변화 X
# 뭉치 찾기
# 1. 단지수 구하기
# 2. 단지 내의 집의 수 cnt (오름차순)
from collections import deque
import sys
input = sys.stdin.readline

# 단지 순회 하면서 단지 수 구하기
def bfs(y, x):
    global q, home
    # 이미 첫번째 집이 발견 돼서 들어온 것 이므로 cnt 시작 1
    cnt = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dx[i]
            nx = x + dy[i]
            if 0 <= ny < n and 0 <= nx < n and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                if map[ny][nx] == 1:
                    cnt += 1
                    q.append([ny, nx])
    home.append(cnt)

# 지도 한 변
n = int(input())

# 입력 값 사이에 공백 없음 -> input().strip()
map = [list(map(int, input().strip())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
danji = 0
home = []
# 그래프 탐색
for i in range(n):
    for j in range(n):
        q = deque()
        if map[i][j] == 1 and visited[i][j] == 0:
            danji += 1
            q.append([i, j])
            visited[i][j] = 1
            bfs(i, j)

# 출력
# 1. 단지수
print(danji)
# 2. 각 단지에 속하는 집의 수 (오름 차순)
home.sort()
print(*home, sep='\n')
