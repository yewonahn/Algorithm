import sys
from collections import deque

input = sys.stdin.readline

# 테스트 케이스
test = int(input())
for _ in range(test):
    # 문서 개수, 궁금 문서 인덱스
    n, m = map(int, input().split())
    # 중요도 차례 대로
    dq = deque(map(int, input().split()))

    while len(dq) == 0:
        for i in range(1, len(dq)):
            if dq[0] < dq[i]:
                dq.append(dq.popleft())
                break

    # 중요도 같은 거 없
    # 중요도 같은 거 있