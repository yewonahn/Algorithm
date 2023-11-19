import sys
input = sys.stdin.readline

n = int(input())
map = [list(input().rstrip()) for _ in range(n)]
current = [list(input().rstrip()) for _ in range(n)]

dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]

isMine = False

for i in range(n):
  for j in range(n):
    if current[i][j] == "x":
      if (map[i][j] == "*"):
        isMine = True
      cnt = 0
      for k in range(8):
        if (0<= i+dx[k] < n and 0 <= j+dy[k] < n and map[i + dx[k]][j + dy[k]] == "*"):
          cnt += 1
        current[i][j] = str(cnt)

if (isMine):
  for i in range(n):
    for j in range(n):
      if (map[i][j] == "*"):
        current[i][j] = "*"

for row in current:
    print("".join(row))
