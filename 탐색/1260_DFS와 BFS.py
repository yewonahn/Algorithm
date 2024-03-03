import sys

def dfs(idx) :
    global visited
    visited[idx] = True
    print(idx, end = ' ')
    # next 라는 노드가 방문된 적이 없고, 방문할 수 있는 노드 라면 방문 하기
    for next in range(1, N + 1):
        if not visited[next] and graph[idx][next]:
            dfs(next)   # 다음엔 next 노드를 방문하겠다는 걸 의미

def bfs() :
    global q, visited
    # q 가 빌 때 까지 실행 하겠다
    while q:
        cur = q.pop(0)  # q 에서 제일 위에 있는거 pop 해주기
        print(cur, end = ' ')
        for next in range(1, N + 1):
            if not visited[next] and graph[cur][next]:
                visited[next] = True
                q.append(next)

# 0. 입력 및 초기화
input = sys.stdin.readline
N, M, V = map(int, input().split())

# 초기 상태 만들어 주기
graph = [[False] * (N + 1) for _ in range(N + 1)] # graph 는 2차원 배열
visited = [False] * (N + 1)

# 1. graph 정보 입력
# 간선 정보를 graph 에 반영
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

# 2. dfs
dfs(V)  # V 노드 부터 함수를 실행 해라
print()

# 3. bfs
# visited 배열 초기화
visited = [False] * (N + 1)
# V 부터 방문하겠다는 걸 의미
q = [V]
visited[V] = True
bfs()