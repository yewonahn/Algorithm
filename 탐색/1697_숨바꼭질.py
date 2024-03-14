import sys
from collections import deque
input = sys.stdin.readline

# 수빈, 동생
n, k = map(int, input().split())

# 구해야 하는 것 : 최소 시간
# (탐색) 이동할 수 있는 모든 점 구하기
# 임의의 점까지 이동할 수 있는 최소 시간 누적 or new 최소 시간으로 변경
visited = [0] * 100001  # (d < 0) IndexError로 추가
next = deque()

# 자신, 부모
next.append([n, n])
while len(next) != 0:
    # 현재 점 위치
    n = next[0][0]
    # print('n :', n)
    next.popleft()
    # 현재 점에서 이동할 수 있는 점 케이스
    d = [n - 1, n + 1, 2 * n]
    for i in d:
        if i < 0 or i > 100000:
            continue
        if visited[i] == 0:
            # print('차례 : ', i)
            next.append([i, n])
            visited[i] = visited[n] + 1
        else:
            if visited[i] > visited[n] + 1:
                visited[i] = visited[n] + 1

# print(visited)
print(visited[k])
