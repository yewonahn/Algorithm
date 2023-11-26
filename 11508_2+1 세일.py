from sys import stdin
n=int(input())
m=list(map(int, stdin.read().split()))
m.sort(reverse=True)
cost = 0
for i in range(n):
    if(i%3!=2):
        cost += m[i]
print(cost)
