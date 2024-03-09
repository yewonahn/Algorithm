# 풀이 참조

import sys
input = sys.stdin.readline

n = int(input())
# 길이 100 도화지
# 2차원 배열
# 중복 색칠 되는 case 여러 번 count 하지 않도록,
# visited 같은 방문 여부 리스트 활용
total = [[0] * 100 for _ in range(100)]

for _ in range(n):
    y, x = map(int, input().split())
    # 색종이 길이 10
    for y1 in range(y, y + 10):
        for x1 in range(x, x + 10):
            # [전체 사각형 = 작은 정사각형 모임] 으로 생각
            total[y1][x1] = 1

# total 에서 값 = 1 인 개수 count
# 2차원 배열 count
result = 0
for i in range(100):
    result += total[i].count(1)

print(result)