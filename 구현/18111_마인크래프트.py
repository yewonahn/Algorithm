# [풀이 참조] 완전 탐색

import sys
input = sys.stdin.readline

# 세로, 가로, 블록 개수
n, m, b = map(int, input().split())
# 각 칸의 높이
height = [list(map(int, input().strip().split())) for _ in range(n)]

# 변화 값 : 높이 (범위) 0 <= 높이 <= 256
# 구해야 할 것 : (최소) 시간
times = {}
# 모든 높이 순회
for fix in range(0, 257):
    # (높이 고정) -> 모든 칸 순회
    time = 0
    for j in range(n):
        for i in range(m):
            # 시간 구하기
            h = height[j][i]
            # 1. 블록 제거
            if h - fix >= 0:
                time += (h - fix) * 2
            # 블록 추가
            # 2. 시간 구하기
            else:
                time += fix - h
    if time in times:
        if fix > times[time]:
            times[time] = fix
    else:
        times[time] = fix

result_t = min(times.keys())
result_h = times[result_t]

print(result_t, result_h)
