from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline

# 1-1. 입력 (구역 개수)
n = int(input())

# 1-2. 입력 (구역 연결 상태)
# 인구
popul = [0] + list(map(int, input().strip().split()))
# 해당 구역과 직접 연결된 구역 저장
graph = [[] for _ in range(n+1)]
for i in range(1, n+1):
    d = deque(map(int, input().strip().split()))
    d.popleft()
    graph[i] = list(d)

# ex) color :  (0, 1, 2)
def bfs(color):
    # 해당 케이스 안에 있는 임의의 한 구역에서 시작해서 이동 가능한 구역 count
    # count 한 값이 len(color) 와 다르면, 이동 불가능한 구역이 있음을 의미
    dq = deque()
    dq.append(color[0])

    # 방문 여부 = 이동 가능 여부
    visited = [False] * (n + 1)
    visited[color[0]] = True
    popul_cnt = popul[color[0]]
    result = False

    while dq:
        now = dq.popleft()

        # 이동 가능한 구역을 count 해야 하므로, graph 순회 (= 현재 구역에서 이동 가능한 구역)
        # -> 현재 구역에서 이동 가능한 구역을 모두 순회 하고
        for i in graph[now]:
            # 해당 구역이 color에 속하고 (= 현재 같은 선거구에 속해 있다면) 아직 방문 안했으면
            if i in color and visited[i] == False:
                # 방문 표시, 방문할 큐에 추가, 인구 누적
                visited[i] = True
                dq.append(i)
                popul_cnt += popul[i]

    # 같은 선거구에 속하고, 이동 가능한 구역들만 visited에 True 로 기록해뒀으므로
    if visited.count(True) == len(color):
        result = True

    return result, popul_cnt


min = 1001
cnt = 0
# 2. 두 선거구가 둘 다 각각 적어도 하나의 구역 포함하는 케이스만 뽑기 -> 조합
# ex) 8C2 = 8C6 이므로 n//2
for i in range(1, n//2 + 1):
    # -1. 조합으로 케이스 뽑기 (nCi 로 가능한 케이스 다 나옴)
    # 구역 번호 = 실제 구역 번호
    reds = deque(combinations(range(1, n+1), i))    # ** combinations(range)

    # -2. 케이스 하나 선택 (각 케이스 돌면서 조건2 만족 하는지 확인 -> BFS)
    while reds:
        red = reds.popleft()
        red_result, red_cnt = bfs(red)
        blue = deque(i for i in range(1, n + 1) if i not in red)  # ** blue 요소 채우기
        blue_result, blue_cnt = bfs(blue)
        if red_result and blue_result:
            if abs(red_cnt - blue_cnt) < min:
                min = abs(red_cnt - blue_cnt)

if min != 1001:
    print(min)
else:
    print(-1)
