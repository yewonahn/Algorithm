import sys

n = int(sys.stdin.readline())

DP = [0] * 1001
DP[1] = 1
DP[2] = 3

for i in range(3,1001):
    DP[i] = DP[i-2] * 2 + DP[i-1]

print(DP[n] % 10007)
