# 행렬 곱셈 방법 참조
# 출력 방법 참조
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = [list(map(int, input().strip().split())) for _ in range(n)]
m, k = map(int, input().split())
B = [list(map(int, input().strip().split())) for _ in range(m)]
C = [[0] * k for _ in range(n)]

# y축 갱신
for y in range(n):
    # x축 갱신
    for x in range(k):
        # 더하기 루프 하나
        for p in range(m):
            C[y][x] += A[y][p] * B[p][x]

# 기존 풀이 출력 방법
# for y in range(n):
#     for x in range(k):
#         print(C[y][x], end=' ')
#     print()

# 출력 방법 참조
for r in C:
    print(*r)
