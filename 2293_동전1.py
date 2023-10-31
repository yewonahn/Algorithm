import sys
input = sys.stdin.readline

n, k = map(int,input().split())
coin = [int(input()) for i in range(n)] # 코인의 종류
dp = [0 for i in range(k+1)]    # 사이즈 k+1 만큼의 리스트 선언
dp[0] = 1   # 동전 하나를 사용하는 경우
for i in coin:
    for j in range(i, k+1):
        if j-1 >= 0:
            dp[j] += dp[j-i]
print(dp[k])
