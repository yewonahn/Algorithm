from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline

# 1-1. 입력 (구역 개수)
n = int(input())

# 1-2. 입력 (구역 연결 상태)
# 인구 (인덱스 = 구역 번호 - 1)
popul = list(map(int, input().strip().split()))
# 해당 구역과 직접 연결된 구역 저장 (인덱스 = 구역 번호 - 1)
graph = [list(map(int, input().strip().split())) for _ in range(n)]

#print(popul)
#print(graph)

# ex) color :  (0, 1, 2)
def bfs(color):
    # 해당 케이스 안에 있는 임의의 한 구역에서 시작해서 이동 가능한 구역 count
    # count 한 값이 len(color) 와 다르면, 이동 불가능한 구역이 있음을 의미
    #print('진입')
    dq = deque()
    dq.append(color[0])

    # 방문 여부 = 이동 가능 여부
    visited = [False] * n
    visited[color[0]-1] = True
    popul_cnt = popul[color[0]-1]
    result = False

    while dq:
        now = dq.popleft()
        #print('now : ', now)

        # 이동 가능한 구역을 count 해야 하므로, graph 순회 (= 현재 구역에서 이동 가능한 구역)
        for i in graph[now - 1]:
            if i in color and visited[i-1] == False:
                visited[i - 1] = True
                dq.append(i)
                popul_cnt += popul[i - 1]

    if visited.count(True) == len(color):
        result = True

    return result, popul_cnt


min = 1001
cnt = 0
# 2. 두 선거구가 둘 다 각각 적어도 하나의 구역 포함하는 케이스만 뽑기 -> 조합
for i in range(1, n//2 + 1):
    #1.  조합으로 케이스 뽑기 (nCi 로 가능한 케이스 다 나옴)
    # 구역 번호 = 실제 구역 번호
    reds = deque(combinations(range(1, n+1), i))    # ** combinations(range)
    #print('reds : ', reds)

    # 2. 케이스 하나 선택 (각 케이스 돌면서 조건2 만족 하는지 확인 -> BFS)
    while reds:
        red = reds.popleft()
        red_result, red_cnt = bfs(red)
        blue = deque(i for i in range(1, n + 1) if i not in red)  # ** blue 요소 채우기
        #print('red : ', red)
        #print('blue : ', blue)
        blue_result, blue_cnt = bfs(blue)
        if red_result and blue_result:
            if abs(red_cnt - blue_cnt) < min:
                min = abs(red_cnt - blue_cnt)

if min != 1001:
    print(min)
else:
    print(-1)
