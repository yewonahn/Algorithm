from collections import deque
import sys
input = sys.stdin.readline

def bfs(color):
    global visited, dq, cnt, visited_color, dq_color, cnt_color
    dy, dx = [0, 0, -1, 1], [-1, 1, 0, 0]
    # 적록색약인 사람
    if color:
        cnt_color += 1
        while dq_color:
            y, x = map(int, dq_color.popleft())
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < n and 0 <= nx < n and visited_color[ny][nx] == 0 and pic_color[ny][nx] == pic_color[y][x]:
                    dq_color.append([ny, nx])
                    visited_color[ny][nx] = 1
    # 적록색약 아닌 사람
    else:
        cnt += 1
        while dq:
            y, x = map(int, dq.popleft())
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < n and 0 <= nx < n and visited[ny][nx] == 0 and pic[ny][nx] == pic[y][x]:
                    dq.append([ny, nx])
                    visited[ny][nx] = 1

n = int(input())
pic = []
pic_color = []  # 적록색약
colors = []
for _ in range(n):
    colors = list(input().strip())
    pic.append(colors[:])
    for a in range(n):
        if colors[a] == 'G':
            colors[a] = 'R'
    pic_color.append(colors)

#print(pic)
#print(pic_color)

# 방문할
dq_color = deque()  # 적록색약
dq = deque()
# cnt
cnt_color = 0   # 적록색약
cnt = 0
# 방문 여부
visited_color = [[0] * n for _ in range(n)] # 적록색약
visited = [[0] * n for _ in range(n)]

for b in range(n):
    for a in range(n):
        color = False
        if visited[b][a] == 0:
            dq.append([b, a])
            visited[b][a] = 1
            bfs(color)
        if visited_color[b][a] == 0:
            color = True
            dq_color.append([b, a])
            visited_color[b][a] = 1
            bfs(color)

print(cnt, cnt_color)
