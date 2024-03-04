import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
MAX = 50 + 10

# 배추 땅 뭉치 개수 구하기
# 이미 기록 되어 있는 뭉치에 인접하지 않은, 새로운 위치의 배추 발견하면 뭉치 개수 + 1
# 현재 위치의 상하좌우에 1이 있는지 체크 필요

dirR = [1, -1, 0, 0]
dirC = [0, 0, 1, -1]

def dfs(Y, X):
    global visited
    # 상하좌우에 1이 없으면 count + 1
    visited[Y][X] = True
    for dirIdx in range(4):
        newY = Y + dirR[dirIdx]
        newX = X + dirC[dirIdx]
        if graph[newY][newX] and not visited[newY][newX]:
            dfs(newY, newX)

T = int(input())
for _ in range(T):
    # 0. 입력 및 초기화
    # 가로, 세로, 배추 개수
    M, N, K = map(int, input().split())
    # 그래프
    graph = [[False] * MAX for _ in range(MAX)]
    visited = [[False] * MAX for _ in range(MAX)]

    # 1. 그래프 정보 입력
    for _ in range(K):
        X, Y = map(int, input().split())
        graph[Y + 1][X + 1] = True

    # 2. 방문하지 않은 지점부터 dfs 돌기
    # 인접한 배추 뭉치 개수
    count = 0
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if graph[i][j] and not visited[i][j]:
                dfs(i, j)
                count += 1
    print(count)