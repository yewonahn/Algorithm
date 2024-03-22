# 1~N 구역
# 2 개의 선거구

# <조건>
# 1. 모든 구역 -> 두 개의 선거구 중 하나에 포함
# 2. 각 선거구는 적어도 하나의 구역을 포함
# 3. 같은 선거구 내의 구역은 연결 되어 있어야 함

# Q. 두 선거구에 포함된 인구의 차이의 최소값
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

# 각 구역의 인구 수
population = list(map(int, input().strip().split()))

graph = [[0] * n for _ in range(n)]
# 연결 안된 쌍 저장
lst = deque()
# 인접한 구역 정보
for a in range(1, n+1):
    # 인접 행렬
    dq = deque(map(int, input().strip().split()))
    dq.popleft()
    for i in range(1, n+1):
        # 1 = 연결
        if i in dq:
            graph[a][i], graph[a][i] = 1, 1
        # -1 = 연결 x
        else:
            graph[a][i], graph[a][i] = -1
            lst.append([a, i])

# 중복 되는 부분 문제 -> 인구 수 누적 저장 dp 테이블

# 조건1. 같은 선거구 내의 구역끼리는 연결 되어 있어야 함
# 가능한 케이스 1. (중간 연결 구역이 있는 경우) 같은 선거구 가능
# 가능한 케이스 2. 다른 선거구로 편성

for i in lst:
    for a in range(1, n+1):
        i[0]
