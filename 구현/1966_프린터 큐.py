# 풀이 참조
# 궁금 문서 인덱스 변화 적용

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
    count = 1

    while dq:
        if dq[0] == max(dq):
            dq.popleft()
            m -= 1
            if m < 0:
                print(count)
                break
            else:
                count += 1
        else:
            dq.append(dq.popleft())
            if m > 0:
                m -= 1
            else:
                m = len(dq) - 1
