import sys

N = int(sys.stdin.readline())

DP = [[0]*3 for _  in range(N+1)]
DP[1][0] = 1
DP[1][1] = 1
DP[1][2] = 1

for i in range(2, N+1):
    for k in range(3):
        if k == 0:
            DP[i][k] = (DP[i-1][k] + DP[i-1][k+1] + DP[i-1][k+2]) % 9901
            
        elif k == 1:
             DP[i][k] = (DP[i-1][k-1] + DP[i-1][k+1]) % 9901
        else:
            DP[i][k] = (DP[i-1][k-1] + DP[i-1][k-2]) % 9901

print(sum(DP[N]) % 9901)
