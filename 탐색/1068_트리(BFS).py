from collections import deque
import sys
input = sys.stdin.readline

# 노드 개수
n = int(input())
# 부모가 없다면 (루트 노드) -1
# 노드 번호 0번 부터 시작
parent = list(map(int, input().strip().split()))
k = int(input())
# visited 테이블
removes = [0] * n
removes[k] = 1
# 지워질 노드의 자식 노드 removes[] = 1 처리 먼저 해야됨
dq = deque()
dq.append(k)

def bfs():
    global dq, removes
    while dq:
        now = dq.popleft()
        for i in range(n):
            if parent[i] == now and removes[i] == 0:
                dq.append(i)
                removes[i] = 1


bfs()

# 지워질 노드가 마지막 노드인 상황 고려
parent[k] = 100
cnt = 0

for i in range(n):
    # 1. 지워질 노드 인지 확인
    # 2. 마지막 노드 인지 확인
    if removes[i] == 0 and i not in parent:
        #print(i, '번째 노드 확인 : ', '2')
        cnt += 1

print(cnt)
