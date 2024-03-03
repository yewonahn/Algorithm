# 컴퓨터의 수 (100 이하 양의 정수, 1부터 번호 매김)
import sys

def dfs(idx):
    global virus, graph, visited
    visited[idx] = True
    for next in range(1, N + 1):
        if not visited[next] and graph[idx][next]:
            dfs(next)
            virus = virus + 1

input = sys.stdin.readline
N = int(input())    # 컴퓨터 개수
M = int(input())    # 연결된 컴퓨터 쌍의 수

# 그래프
graph = [[False] * (N + 1) for _ in range(N + 1)]
visited = [False] * (N + 1)

# 연결된 쌍 그래프에 기록
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

virus = 0
dfs(1)
print(virus)