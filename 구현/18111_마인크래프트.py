# [풀이 참조] 완전 탐색

import sys
input = sys.stdin.readline

# 세로, 가로, 블록 개수
n, m, b = map(int, input().split())
# 각 칸의 높이
height = [list(map(int, input().strip().split())) for _ in range(n)]

# 변화 값 : 높이 (범위) 0 <= 높이 <= 256
# 구해야 할 것 : (최소) 시간
time = sys.maxsize  # 최대 높이 비교 size
max_h = 0
# 모든 높이 순회
for fix in range(257):
    # (높이 고정) -> 모든 칸 순회
    remove_block, add_block = 0, 0
    for j in range(n):
        for i in range(m):
            # 1. 블록 제거
            if height[j][i] - fix > 0:
                remove_block += (height[j][i] - fix)
            # 2. 블록 추가
            else:
                add_block += (fix - height[j][i])
    # 조건) 제거 블록 + b >= 추가 블록
    if remove_block + b >= add_block:
        # 최대 높이 저장
        if remove_block * 2 + add_block <= time:
            time = remove_block * 2 + add_block
            max_h = fix

print(time, max_h)
