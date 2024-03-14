from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append(n)

    while q:
        now = q.popleft()

        if now == k:
            return
        for next in (now-1, now+1, 2*now):
            if 0 <= next <= 100000 and visited[next] == 0:
                visited[next] = visited[now] + 1
                q.append(next)


# 수빈, 동생
n, k = map(int, input().split())
visited = [0] * 100001

bfs()
print(visited[k])
