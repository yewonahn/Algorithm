import sys

# 배추 땅 뭉치 개수 구하기
# 이미 기록 되어 있는 뭉치에 인접하지 않은, 새로운 위치의 배추 발견하면 뭉치 개수 + 1
# 현재 위치의 상하좌우에 1이 있는지 체크 필요
def dfs(X, Y):
    global graph, visited, count
    # 상하좌우에 1이 없으면 count + 1

input = sys.stdin.readline
T = int(input())
# 가로, 세로, 배추 개수
M, N, K = map(int, input().split())

# 그래프
graph = [[0 for _ in range(M)] for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

# 인접한 배추 뭉치 개수
count = 0

# 배추 위치 기록
for _ in range(K):
    X, Y = map(int, input().split())
    graph[X][Y] = 1
    dfs(X, Y)