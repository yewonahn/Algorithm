# [풀이 참조] DP 테이블
# for 문 써서 구현으로 풀면 시간 초과

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]

# (0, 0) 부터 임의의 점 (p, q) 까지의 누적 합을 저장해 줄 리스트
dp = [[0] * (m + 1) for _ in range(n + 1)]
# dp (누적합) 채우기
for a in range(1, n + 1):
    for b in range(1, m + 1):
        dp[a][b] = dp[a-1][b] + dp[a][b-1] - dp[a-1][b-1] + lst[a-1][b-1]

k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    result = dp[x][y] - dp[i-1][y] - dp[x][j-1] + dp[i-1][j-1]
    print(result)
