import sys
input = sys.stdin.readline

n = int(input())
length = list(map(int,input().split())) #도로의 길이
cost = list(map(int,input().split())) #가격

minCost = cost[0]
total = 0

for i in range(n-1):
    
    if minCost > cost[i]:
        minCost = cost[i]

    total += (minCost * length[i])

print(total)
